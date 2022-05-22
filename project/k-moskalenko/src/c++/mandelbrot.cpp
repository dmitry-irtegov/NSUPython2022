#include <Python.h>
#include <ccomplex>
#include <random>

#include "ctpl_stl.h"

using pixel_t = uint32_t;

namespace mandelbrot {
    constexpr int max_iterate = 200;
    static pixel_t palette[UINT8_MAX];

    double translate(int value, int size, double minVal, double maxVal) {
        double valueScaled = value / (double) size;
        return minVal + valueScaled * (maxVal - minVal);
    }

    void GenerateRandomPalette() {
        std::random_device rd;
        std::mt19937 rng(rd());

        std::uniform_int_distribution<int> uni_i(128, 256);
        std::uniform_real_distribution<double> uni_r(0, 256);

        palette[0] = 0xff000000;

        double redb = 2 * M_PI / uni_i(rng), redc = uni_r(rng);
        double greenb = 2 * M_PI / uni_i(rng), greenc = uni_r(rng);
        double blueb = 2 * M_PI / uni_i(rng), bluec = uni_r(rng);

        for (int i = 1; i < UINT8_MAX; i++) {
            uint8_t r = UINT8_MAX * (0.5 * std::sin(redb * i + redc) + 0.5);
            uint8_t g = UINT8_MAX * (0.5 * std::sin(greenb * i + greenc) + 0.5);
            uint8_t b = UINT8_MAX * (0.5 * std::sin(blueb * i + bluec) + 0.5);

            palette[i] = (0xff << 24) | (b << 16) | (g << 8) | r;
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

        return palette[count % UINT8_MAX];
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
