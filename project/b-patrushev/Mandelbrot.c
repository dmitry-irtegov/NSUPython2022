#include <stdio.h>
#include <stdlib.h>
#include <complex.h>
#include <math.h>
#include <omp.h>

int** res;
double xmin, ymin, ymax, xmax;
double PixelWidth, PixelHeight;
const int IterationMax=200;
const double EscapeRadius=2;


double complex give_c(int iX, int iY){
    double Cx, Cy;
    Cy = ymin + iY*PixelHeight;
    if (fabs(Cy) < PixelHeight / 2)
        Cy = 0.0;
    Cx = xmin + iX * PixelWidth;

    return Cx + Cy * I;

}

int iterate(double complex C , int iMax)
{
    int i;
    double complex Z = 0.0;
    for( i = 0; i < iMax; i++)
    {
        Z = Z * Z + C;
        if(cabs(Z) > EscapeRadius){
            break;
        }
    }
    return i;
}



int** mandelbrot(double x, double y, double m, int w, int h){
    complex double c;

    xmin = x - m;
    xmax = x + m;
    ymin = y - m;
    ymax = y + m;

    PixelWidth = (xmax - xmin) / w;
    PixelHeight = (ymax - ymin) / h;
    res = malloc(sizeof(int*) * h);
    for(int iY = 0; iY < h; iY++){
        res[iY] = malloc(sizeof(int*) * w);
    }
    #pragma omp parallel
    for(int iY = 0;iY < h; iY++){
        for(int iX = 0;iX < w; iX++){

            c = give_c(iX, iY);
            res[iY][iX] = iterate(c, IterationMax);
        }
    }

    return res;

}

int main(){
    mandelbrot(-0.75, 0, 1.5, 720, 720 );
    return 0;
}


