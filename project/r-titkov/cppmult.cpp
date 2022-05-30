#include <iostream>
#include <iomanip>
#include <string.h>
#include "cptl.h"
#include <cmath>
#include "cppmult.hpp"

int MAX_STEPS = 25;
double MAX_COORDS = 3;

int WINDOW_WIDTH = 700;
int WINDOW_HEIGHT = 700;

double centerX = -0.5; 
double centerY = 0;

char* colors;

double BASE_WIDTH = 2.5;
double BASE_HEIGHT = 2.5;

double CALC_WIDTH = 2.5;
double CALC_HEIGHT = 2.5;

EXPORT_SYMBOL void setWindowSize(int width, int height) {
	WINDOW_WIDTH = width;
	WINDOW_HEIGHT = height;

	CALC_WIDTH = BASE_WIDTH * (double) WINDOW_WIDTH / 700;
	CALC_HEIGHT = BASE_HEIGHT * (double) WINDOW_HEIGHT / 700;
}

void scaleFrame(double scale) {
	if ((scale > 1 && (CALC_WIDTH <= 1e-11 || CALC_HEIGHT <= 1e-11)) ||
		 (scale < 1 && (CALC_WIDTH >= 6 || CALC_HEIGHT >= 6)))
		return;

	BASE_WIDTH *= 1 / scale;
	BASE_HEIGHT *= 1 / scale;
	CALC_WIDTH = BASE_WIDTH * (double) WINDOW_WIDTH / 700;
	CALC_HEIGHT = BASE_HEIGHT * (double) WINDOW_HEIGHT / 700;
}

void setCenter(double x, double y) {
	centerX = x;
	centerY = y;
}

void setCenterRelative(int x, int y) {
	double newCenterX = centerX - CALC_WIDTH / 2 + CALC_WIDTH / WINDOW_WIDTH * x;
	double newCenterY = centerY - CALC_HEIGHT / 2 + CALC_HEIGHT / WINDOW_HEIGHT * y;
	if (newCenterX <= -MAX_COORDS || newCenterX > MAX_COORDS || 
		 newCenterY < -MAX_COORDS || newCenterY > MAX_COORDS)
		return;
	centerX = newCenterX;
	centerY = newCenterY;
}

void zoomInFrame(int xmin, int ymin, int xmax, int ymax) {
	int xmidle = (int) (xmin + xmax) / 2;
	int ymidle = (int) (ymin + ymax) / 2;
	setCenterRelative(xmidle, ymidle);

	double scale = WINDOW_WIDTH / (xmax - xmin);
	BASE_WIDTH *= 1 / scale;
	BASE_HEIGHT *= 1 / scale;
	CALC_WIDTH = BASE_WIDTH * (double) WINDOW_WIDTH / 700;
	CALC_HEIGHT = BASE_HEIGHT * (double) WINDOW_HEIGHT / 700;
}

EXPORT_SYMBOL void setMaxSteps(int maxSteps) {
	MAX_STEPS = maxSteps;
	const int BASE_COLORS_COUNT = 7;
	double points[BASE_COLORS_COUNT] = {0, 0.03, 0.20, 0.4, 0.7, 0.99, 1};
	int y[BASE_COLORS_COUNT][3] = {
		{0, 7, 100}, 
		{32, 107, 155}, 
		{147, 187, 185}, 
		{197, 190, 104}, 
		{223, 150, 65}, 
		{100, 10, 10},
		{30, 0, 0}
	};

	double slopes[BASE_COLORS_COUNT - 1][3] = {};
	for (int i = 0; i < BASE_COLORS_COUNT - 1; i++) {
		double xslope = points[i + 1] - points[i];
		double rslope = (y[i + 1][0] - y[i][0]) / xslope;
		double gslope = (y[i + 1][1] - y[i][1]) / xslope;
		double bslope = (y[i + 1][2] - y[i][2]) / xslope;

		slopes[i][0] = rslope;
		slopes[i][1] = gslope;
		slopes[i][2] = bslope;
	}

	double m[BASE_COLORS_COUNT][3] = {};
	for (int i = 0; i < BASE_COLORS_COUNT ; i++) {
		double mkr, mkg, mkb;
		if (i == 0) {
			mkr = slopes[i][0];
			mkg = slopes[i][1];
			mkb = slopes[i][2];
		} else if (i == BASE_COLORS_COUNT - 1) {
			mkr = slopes[i - 1][0];
			mkg = slopes[i - 1][1];
			mkb = slopes[i - 1][2];
		} else {
			if (slopes[i - 1][0] * slopes[i][0] < 0)
				mkr = 0;
			else
				mkr = (slopes[i - 1][0] + slopes[i][0]) / 2;

			if (slopes[i - 1][1] * slopes[i][1] < 0)
				mkg = 0;
			else
				mkg = (slopes[i - 1][1] + slopes[i][1]) / 2;

			if (slopes[i - 1][2] * slopes[i][2] < 0)
				mkb = 0;
			else
				mkb = (slopes[i - 1][2] + slopes[i][2]) / 2;
		}

		m[i][0] = mkr;
		m[i][1] = mkg;
		m[i][2] = mkb;
	}

	for (int k = 0; k < BASE_COLORS_COUNT - 1 ; k++) {
		double ak0 = m[k][0] / slopes[k][0];
		double bk0 = m[k+1][0] / slopes[k][0];

		double ak1 = m[k][1] / slopes[k][1];
		double bk1 = m[k+1][1] / slopes[k][1];

		double ak2 = m[k][2] / slopes[k][2];
		double bk2 = m[k+1][2] / slopes[k][2];

		if (ak0 * ak0 + bk0 * bk0 > 9) {
			double tk0 = 3 / std::sqrt(ak0 * ak0 + bk0 * bk0);
			m[k][0] = tk0 * ak0 * slopes[k][0];
			m[k+1][0] = tk0 * bk0 * slopes[k][0];
		}
		if (ak1 * ak1 + bk1 * bk1 > 9) {
			double tk1 = 3 / std::sqrt(ak1 * ak1 + bk1 * bk1);
			m[k][1] = tk1 * ak1 * slopes[k][1];
			m[k+1][1] = tk1 * bk1 * slopes[k][1];
		}
		if (ak2 * ak2 + bk2 * bk2 > 9) {
			double tk2 = 3 / std::sqrt(ak2 * ak2 + bk2 * bk2);
			m[k][2] = tk2 * ak2 * slopes[k][2];
			m[k+1][2] = tk2 * bk2 * slopes[k][2];
		}
	}

	auto h00 = [] (double t) { return (2*t*t*t - 3*t*t + 1); };
	auto h10 = [] (double t) { return (t*t*t - 2*t*t + t); };
	auto h01 = [] (double t) { return (-2*t*t*t + 3*t*t); };
	auto h11 = [] (double t) { return (t*t*t - t*t); };

	colors = (char *) malloc(MAX_STEPS * 3);

	for (int colorId = 0; colorId < MAX_STEPS; colorId++) {
		double colorX = (double) colorId / MAX_STEPS;
		for (int k = 0; k < BASE_COLORS_COUNT - 1; k++) {
			if (points[k] <= colorX && colorX <= points[k + 1]) {
				double delta = points[k + 1] - points[k];
				double t = (colorX - points[k]) / delta;
				

				unsigned char r = int(y[k][0]   * h00(t) + delta * m[k][0]   * h10(t)
							 + y[k+1][0] * h01(t) + delta * m[k+1][0] * h11(t));
				
				unsigned char g = int(y[k][1]   * h00(t) + delta * m[k][1]   * h10(t)
							 + y[k+1][1] * h01(t) + delta * m[k+1][1] * h11(t));

				unsigned char b = int(y[k][2]   * h00(t) + delta * m[k][2]   * h10(t)
							 + y[k+1][2] * h01(t) + delta * m[k+1][2] * h11(t));

				colors[colorId * 3] = r;
				colors[colorId * 3 + 1] = g;
				colors[colorId * 3 + 2] = b;
				break;
			}
		}
	}
}

void getState(double *centerXState, double *centerYState, double *dxState, double *dyState) {
	*centerXState = centerX;
	*centerYState = centerY;
	*dxState = CALC_WIDTH / WINDOW_WIDTH;
	*dyState = CALC_HEIGHT / WINDOW_HEIGHT;
}
	

int calculateStep(double pointReal, double pointImag) {
	double real = pointReal;
	double imag = pointImag;

	double realXreal, imagXimag, realXimag;
	double newResReal, newResImag;

	int step = 1;
	while (step < MAX_STEPS) {
		realXreal = real * real;
		imagXimag = imag * imag;

		if (realXreal + imagXimag >= 4)
			return step;

		realXimag = real * imag;

		newResReal = (realXreal - imagXimag);
		newResImag = (realXimag + realXimag);

		real = pointReal + newResReal;
		imag = pointImag + newResImag;
		step += 1;
	}
	return step;
}

void calculate(unsigned char* array) {
	double xmin = centerX - CALC_WIDTH / 2;
	double ymin = centerY - CALC_HEIGHT / 2;

	double dx = CALC_WIDTH / WINDOW_WIDTH;
	double dy = CALC_HEIGHT / WINDOW_HEIGHT;

	const int nthreads = std::thread::hardware_concurrency();

	ctpl::thread_pool p(nthreads);
	std::vector<std::future<void>> results;

	int ROW_OFFSET = 25;
	for (int fromRow = 0; fromRow < WINDOW_HEIGHT; fromRow += ROW_OFFSET) {
		int toRow = fromRow + ROW_OFFSET;
		if (toRow > WINDOW_HEIGHT)
			toRow = WINDOW_HEIGHT;

		results.push_back(p.push([&array, dx, dy, xmin, ymin,
										  fromRow, toRow] (int) {
			double real, imag;
			int step;
			for (int y = fromRow; y < toRow; y++) {
				for (int x = 0; x < WINDOW_WIDTH; x++) {
					real = xmin + dx * x;
					imag = ymin + dy * y;
					step = calculateStep(real, imag);

					if (step == MAX_STEPS) {
						array[3 * (y * WINDOW_WIDTH + x)] = 0;
						array[3 * (y * WINDOW_WIDTH + x) + 1] = 0;
						array[3 * (y * WINDOW_WIDTH + x) + 2] = 0;
					} else {
						array[3 * (y * WINDOW_WIDTH + x)] = colors[step * 3];
						array[3 * (y * WINDOW_WIDTH + x) + 1] = colors[step * 3 + 1];
						array[3 * (y * WINDOW_WIDTH + x) + 2] = colors[step * 3 + 2];
					}
				}
			}		
		}));
	}

	for (unsigned long i = 0; i < results.size(); i += 1) {
		results[i].get();
	}
}
