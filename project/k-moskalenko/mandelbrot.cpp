#include <Python.h>
#include <ccomplex>

namespace mandelbrot {
    constexpr int max_iterate = 5000;

    int CalculatePoint(double u, double v) {
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

        return count;
    }
}

static PyObject *calculate_point(PyObject *, PyObject *args) {
    double u, v;
    if (!PyArg_ParseTuple(args, "dd", &u, &v)) {
        return nullptr;
    }

    int result = mandelbrot::CalculatePoint(u, v);
    return PyLong_FromLong(result);
}

static PyMethodDef MandelbrotMethods[] = {
        {"calculate_point", calculate_point, METH_VARARGS, "Calculate the number of iterations at the point."},
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
    return PyModule_Create(&MandelbrotModule);
}
