//
// Created by Konstantin Moskalenko on 29.05.2022.
//

#ifndef MANDELBROT_PALETTE_H
#define MANDELBROT_PALETTE_H

#include <cstdint>

struct Color;
struct GradientPoint;

using pixel_t = uint32_t;
using Gradient = GradientPoint[];

struct Color {
    const uint8_t r, g, b;

    pixel_t toRGBA() const {
        return 0xff << 24 | b << 16 | g << 8 | r;
    }
};

struct GradientPoint {
    const double position;
    const Color color;
};

constexpr Gradient spectrum = {
        {0.16, {255, 0,   0}},
        {0.33, {255, 255, 0}},
        {0.5,  {0,   255, 0}},
        {0.66, {0,   255, 255}},
        {0.83, {0,   0,   255}},
        {1.0,  {255, 0,   255}},
};

constexpr Gradient earthAndSky = {
        {0.0,    {0,   7,   100}},
        {0.16,   {32,  107, 203}},
        {0.42,   {237, 255, 255}},
        {0.6425, {255, 170, 0}},
        {0.8575, {0,   2,   0}},
        {1.0,    {0,   7,   100}},
};

constexpr Gradient grayscale = {
        {0.0, {0,   0,   0}},
        {0.5, {255, 255, 255}},
        {1.0, {0,   0,   0}},
};

#endif //MANDELBROT_PALETTE_H
