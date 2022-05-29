#include <Python.h>
#include <ccomplex>
#include <random>

#include "palette.h"
#include "ctpl_stl.h"

namespace mandelbrot {
    constexpr int max_iterate = 200;
    constexpr int palette_size = max_iterate;

    static pixel_t palette[palette_size];

    double translate(int value, int size, double minVal, double maxVal) {
        double valueScaled = value / (double) size;
        return minVal + valueScaled * (maxVal - minVal);
    }

    void GeneratePalette(const Gradient gradient) {
        for (int i = 0, region = 0; i < palette_size; i++) {
            const double pos = i / (double) palette_size;
            if (pos > gradient[region + 1].position) region++;

            const auto c1 = gradient[region].color;
            const auto c2 = gradient[region + 1].color;

            const double fr = (pos - gradient[region].position) / (
                    gradient[region + 1].position - gradient[region].position
            );

            const auto r = (uint8_t) ((c2.r - c1.r) * fr + c1.r);
            const auto g = (uint8_t) ((c2.g - c1.g) * fr + c1.g);
            const auto b = (uint8_t) ((c2.b - c1.b) * fr + c1.b);

            palette[i] = Color{r, g, b}.toRGBA();
        }
    }

    void GenerateRandomPalette() {
        std::random_device rd;
        std::mt19937 rng(rd());

        std::uniform_int_distribution<int> uni_i(128, 256);
        std::uniform_real_distribution<double> uni_r(0, 256);

        double redb = 2 * M_PI / uni_i(rng), redc = uni_r(rng);
        double greenb = 2 * M_PI / uni_i(rng), greenc = uni_r(rng);
        double blueb = 2 * M_PI / uni_i(rng), bluec = uni_r(rng);

        for (int i = 0; i < palette_size; i++) {
            uint8_t r = UINT8_MAX * (0.5 * std::sin(redb * i + redc) + 0.5);
            uint8_t g = UINT8_MAX * (0.5 * std::sin(greenb * i + greenc) + 0.5);
            uint8_t b = UINT8_MAX * (0.5 * std::sin(blueb * i + bluec) + 0.5);

            palette[i] = Color{r, g, b}.toRGBA();
        }
    }

    pixel_t CalculatePoint(double u, double v) {
        std::complex<double> const c(u, v);
        std::complex<double> z = c;

        int count = 0;
        while (count < max_iterate) {
            if (std::abs(z) > 2.0) {
                break;
            }

            z = z * z + c;
            count++;
        }

        if (count == max_iterate) {
            return 0xff000000;
        } else {
            const size_t colorPosition =
                    max_iterate >= palette_size ? count % palette_size :
                    (size_t) (palette_size * (count / (double) max_iterate));
            return palette[colorPosition];
        }
    }

    const pixel_t *CalculateImage(int width, int height, double xMin, double xMax, double yMin, double yMax) {
        static ctpl::thread_pool threadPool((int) std::thread::hardware_concurrency());

        static int prevWidth, prevHeight;
        static pixel_t *buffer;

        if (width > prevWidth || height > prevHeight) {
            delete buffer;
            buffer = new pixel_t[width * height];
            prevWidth = width;
            prevHeight = height;
        }

        std::future<void> futures[width];

        for (int x = 0; x < width; x++) {
            futures[x] = threadPool.push([=](int id) {
                for (int y = 0; y < height; y++) {
                    double re = translate(x, width, xMin, xMax);
                    double im = translate(y, height, yMax, yMin);

                    buffer[y * width + x] = CalculatePoint(re, im);
                }
            });
        }

        for (const auto &future: futures) {
            future.wait();
        }

        return buffer;
    }
}

static PyObject *calculate_point(PyObject *, PyObject *args) {
    double u, v;
    if (!PyArg_ParseTuple(args, "dd", &u, &v)) {
        return nullptr;
    }

    auto result = mandelbrot::CalculatePoint(u, v);
    return PyLong_FromUnsignedLong(result);
}

static PyObject *calculate_image(PyObject *, PyObject *args) {
    int width, height;
    double xMin, xMax, yMin, yMax;
    if (!PyArg_ParseTuple(args, "iidddd", &width, &height, &xMin, &xMax, &yMin, &yMax)) {
        return nullptr;
    }

    auto image = mandelbrot::CalculateImage(width, height, xMin, xMax, yMin, yMax);
    auto memoryView = PyMemoryView_FromMemory((char *) image, 4 * width * height, PyBUF_READ);
    return PyObject_CallMethod(memoryView, "cast", "(s(ii))", "I", width, height);
}

static PyMethodDef MandelbrotMethods[] = {
        {"calculate_point", calculate_point, METH_VARARGS, "Calculates the pixel color at an imaginary point."},
        {"calculate_image", calculate_image, METH_VARARGS, "Calculates the pixel colors for an image."},
        {nullptr,           nullptr, 0,                    nullptr}
};

static PyModuleDef MandelbrotModule = {
        PyModuleDef_HEAD_INIT,
        "mandelbrot",
        "A set of methods for calculating the Mandelbrot fractal.",
        -1,
        MandelbrotMethods
};

PyMODINIT_FUNC PyInit_mandelbrot() {
    mandelbrot::GenerateRandomPalette();
    return PyModule_Create(&MandelbrotModule);
}
