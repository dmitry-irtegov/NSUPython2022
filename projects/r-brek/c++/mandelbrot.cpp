#include <Python.h>

#include <complex>
#include <numeric>
#include <algorithm>
#include <iostream>
#include <execution>
#include <vector>

namespace mandelbrot {
    namespace {
        constexpr std::uint32_t maxIterations = 255;
    }

    /**
     *
     * @param u
     * @param v
     * @return number of iterations needed or maxIterations
     */
    uint32_t getModelEstimation(std::complex<double> c) {
        std::complex<double> z = 0;

        int count = 0;
        while (count < maxIterations) {
            if (std::abs(z) > 2.0) {
                break;
            }

            z = z * z + c;
            count++;
        }

        return count;
    }

    /*
     * def calculateModelPoint(point, offset, screenDims, scale):
    x, y = point
    spanReal, spanImaginary = getSpansByOffsetAndScreen(offset, screenDims, scale)
    c = complex(spanReal[0] + (x / screenDims[0]) * (spanReal[1] - spanReal[0]),
                spanImaginary[0] + (y / screenDims[1]) * (spanImaginary[1] - spanImaginary[0]))
    est = getModelEstimation(c)
    color = estimationToColor(est)
    return color
     */

    using Span = std::pair<double, double>;

    std::pair<Span, Span> getSpansByOffsetAndScreen(
        std::pair<int32_t, int32_t>& offset,
        std::pair<uint32_t, uint32_t>& screenWH,
        double scale
    ) {
        scale = 1.0f / scale;
        double xMult = (1.0f / screenWH.first * 3) * scale;
        double yMult = (1.0f / screenWH.second * 2) * scale;
        double x = -0.5f + offset.first * xMult;
        double y = 0.0f + offset.second * yMult;
        double re_len = screenWH.first * xMult;
        double im_len = screenWH.second * yMult;
        double RE_START = -1.5f * scale + x;
        double IM_START = -1.0f * scale + y;
        return {{RE_START, RE_START + re_len}, {IM_START, IM_START + im_len}};
    }

    uint32_t calculateModelPoint(
            std::pair<int32_t, int32_t> point,
            std::pair<int32_t, int32_t> offset,
            std::pair<uint32_t, uint32_t> screenWH,
            double scale
    ) {
        auto [spanReal, spanImaginary] = getSpansByOffsetAndScreen(offset, screenWH, scale);
        const auto& [x, y] = point;
        std::complex<double> c = std::complex(
            spanReal.first + (static_cast<double>(x) / screenWH.first) * (spanReal.second - spanReal.first),
            spanImaginary.first + (static_cast<double>(y) / screenWH.second) * (spanImaginary.second - spanImaginary.first));
        uint32_t est = getModelEstimation(c);
        return est;
    }

    std::vector<uint32_t>
    calculateModel(
            std::vector<std::pair<int32_t, int32_t>>& coordPairs,
            int32_t offsetX,
            int32_t offsetY,
            uint32_t screenWidth,
            uint32_t screenHeight,
            double scale
    ) {
        std::vector<uint32_t> res;
        res.resize(coordPairs.size());

        std::vector<uint32_t> indices;
        indices.resize(coordPairs.size());

        std::iota(indices.begin(), indices.end(), 0);

        std::pair<int32_t, int32_t> offset{offsetX, offsetY};
        std::pair<uint32_t, uint32_t> screenWH{screenWidth, screenHeight};
        std::for_each(std::execution::par_unseq, indices.begin(), indices.end(),
                      [&](uint32_t index) {
                          auto& point = coordPairs[index];
                          auto est = calculateModelPoint(
                                  point,
                                  offset,
                                  screenWH,
                                  scale
                          );
                          res[index] = est;
                      });

        return res;
    }
}

namespace {

    PyObject* getMaxEstimation(PyObject* , PyObject* ) {
        return Py_BuildValue("I", mandelbrot::maxIterations);
    }

    PyObject* calculateManyMandelbrots(PyObject *, PyObject *args) {
        // done_work = calculate_many_mandelbrots(offset[0], offset[1], screenWH[0], screenWH[1], scale)
        // it is assumed that all pixels will be calculated
        int32_t offsetX, offsetY;
        uint32_t screenWidth, screenHeight;
        double scale;
        if (!PyArg_ParseTuple(args, "iiIId", &offsetX, &offsetY, &screenWidth, &screenHeight, &scale)) {
            std::cerr << "Error parsing input tuple" << std::endl;
            return nullptr;
        }

        using Coordinate = std::pair<int32_t, int32_t>;
        std::vector<Coordinate> jobCoords;
        jobCoords.reserve(screenHeight * screenWidth);
        for (uint32_t x = 0; x < screenWidth; x++) {
            for (uint32_t y = 0; y < screenHeight; y++) {
                jobCoords.push_back({x, y});
            }
        }

        auto result = mandelbrot::calculateModel(
                jobCoords,
                offsetX, offsetY,
                screenWidth, screenHeight,
                scale
        );
        PyObject* returnList = PyList_New(result.size());
        for (uint32_t i = 0; i < result.size(); i++) {
            // PyObject* coordsTuple = Py_BuildValue("ii", result[i].first.first, result[i].first.second);
            PyObject* coordsToIterations = Py_BuildValue("I", result[i]);
            PyList_SET_ITEM(returnList, i, coordsToIterations);
        }
        return returnList;
    }

    PyMethodDef MandelbrotMethods[] = {
            {"get_max_estimation",         getMaxEstimation, METH_VARARGS, "Returns max number of iterations."},
            {"calculate_many_mandelbrots", calculateManyMandelbrots, METH_VARARGS, "For each pair of coords, calculates number of iterations."},
            {nullptr,                      nullptr, 0,                             nullptr}
    };

    PyModuleDef MandelbrotModule = {
            PyModuleDef_HEAD_INIT,
            "mandelbrot",
            "A set of methods for calculating the Mandelbrot fractal.",
            -1,
            MandelbrotMethods
    };
}

PyMODINIT_FUNC PyInit_mandelbrot() {
    return PyModule_Create(&MandelbrotModule);
}
