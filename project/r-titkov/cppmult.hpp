#include <vector>

#ifdef _MSC_VER
    #define EXPORT_SYMBOL __declspec(dllexport)
#else
    #define EXPORT_SYMBOL
#endif

#ifdef __cplusplus
extern "C" {
#endif

EXPORT_SYMBOL void calculate(unsigned char* array);
EXPORT_SYMBOL void setWindowSize(int width, int height);
EXPORT_SYMBOL void setCenter(double x, double y);
EXPORT_SYMBOL void setCenterRelative(int x, int y);
EXPORT_SYMBOL void setMaxSteps(int maxSteps);
EXPORT_SYMBOL void zoomInFrame(int xmin, int ymin, int xmax, int ymax);
EXPORT_SYMBOL void scaleFrame(double scale);

#ifdef __cplusplus
}
#endif