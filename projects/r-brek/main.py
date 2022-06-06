import pygame
from mandelbrot import calculate_many_mandelbrots
from mandelbrot import get_max_estimation
from sys import stderr


class Estimation:
    pass


class Unreachable(Estimation):
    pass


class Reachable(Estimation):
    def __init__(self, iteration, max_iter):
        self.iteration = iteration
        self._max_iter = max_iter

    # 0 to 255
    def getHottness(self):
        return int((self.iteration / self._max_iter) * 255)


def getModelEstimation(c):
    MAX_ITER = 15
    z = 0
    n = 0
    while abs(z) <= 2 and n < MAX_ITER:
        z = z*z + c
        n += 1
    return Unreachable() if n == MAX_ITER else Reachable(n, MAX_ITER)

def iterationHottnessToColor(iteration, maxIteration):
    est = Unreachable() if (iteration == maxIteration) else Reachable(iteration, maxIteration)
    return estimationToColor(est)

def estimationToColor(estimation):
    def normalize(x, higher_bound):
        if x < 0:
            return 0
        return int((x / higher_bound) * 255)
    if isinstance(estimation, Unreachable):
        return pygame.Color(255, 255, 255)
    else:
        hottness = estimation.getHottness()
        red = hottness # if hottness <= 120 else 120
        green = normalize(hottness - 120, 500)
        blue = normalize(hottness - 180, 75)
        # green = normalize(hottness - 1 * (255 / 3), 2 * (255 / 3))
        # blue = normalize(hottness, 255)
        return pygame.Color(red, green, blue)

def calculateModelPoint(point, offset, screenDims, scale):
    x, y = point
    spanReal, spanImaginary = getSpansByOffsetAndScreen(offset, screenDims, scale)
    c = complex(spanReal[0] + (x / screenDims[0]) * (spanReal[1] - spanReal[0]),
                spanImaginary[0] + (y / screenDims[1]) * (spanImaginary[1] - spanImaginary[0]))
    est = getModelEstimation(c)
    color = estimationToColor(est)
    return color

def calculateWholeModelAt(offset, screenDims, scale):
    spanReal, spanImaginary = getSpansByOffsetAndScreen(offset, screenDims, scale)
    res = dict()
        
    for x in range(screenDims[0]):
        for y in range(screenDims[1]):
            c = complex(spanReal[0] + (x / screenDims[0]) * (spanReal[1] - spanReal[0]),
                        spanImaginary[0] + (y / screenDims[1]) * (spanImaginary[1] - spanImaginary[0]))
            est = getModelEstimation(c)
            color = estimationToColor(est)
            res[(x + offset[0], y + offset[1])] = color
    return res

def getSpansByOffsetAndScreen(offset, screenWH, scale):
    scale = 1 / scale
    screenCenter = (screenWH[0] // 2,
                    screenWH[1] // 2)
    xPixelsToReal, yPixelsToReal = (1 / screenWH[0] * 3), (1 / screenWH[1] * 2)
    xPixelsToScaledReal, yPixelsToScaledReal = xPixelsToReal * scale, yPixelsToReal * scale
    screenCenterAbs = ((screenCenter[0] + offset[0]) * xPixelsToScaledReal,
                       (screenCenter[1] + offset[1]) * yPixelsToScaledReal)
    # print(screenCenterAbs)
    # x, y = (-2 + screenCenterAbs[0]) * xPixelsToScaledReal , (-1.0 + screenCenterAbs[1]) * yPixelsToScaledReal
    re_len, im_len = screenWH[0] * xPixelsToScaledReal, screenWH[1] * yPixelsToScaledReal
    RE_START = -1.5 * scale + screenCenterAbs[0]
    IM_START = -1 * scale + screenCenterAbs[1]
    return ((RE_START, RE_START + re_len), (IM_START, IM_START + im_len))

def patch_model(pixel_array, offset, screenWH, scale):
    print("Generating workload", file=stderr)
    work_load = []
    for x in range(screenWH[0]):
        for y in range(screenWH[1]):
            # xAbs = x + offset[0]
            # yAbs = y + offset[1]
            work_load.append((x, y))
            # if (xAbs, yAbs) not in pixel_array:
            #     work_load.append((x, y))
    estimation_max_level = get_max_estimation()
    print("Patching model...", file=stderr)
    done_work = calculate_many_mandelbrots(offset[0], offset[1], screenWH[0], screenWH[1], scale)
    print("Retrieved new values", file=stderr)
    for (idx, est) in enumerate(done_work):
    # for (idx, (x, y)) in enumerate(work_load):
        x, y = work_load[idx]
        # xAbs = x + offset[0]
        # yAbs = y + offset[1]
        pixel_array[x, y] = iterationHottnessToColor(est, estimation_max_level)
        # pixel_array[x, y] = calculateModelPoint((x, y), offset, screenWH, scale)
    print("Model is patched\n", file=stderr)

def draw_model_lazy(screen_pixel_array, offset, model):
    raise RuntimeError("fix absolute coords first")
    print("drawing lazy", file=stderr)
    for x in range(screen_pixel_array.shape[0]):
        for y in range(screen_pixel_array.shape[1]):
            xAbs = x + offset[0]
            yAbs = y + offset[1]
            if (xAbs, yAbs) not in model:
                screen_pixel_array[x, y] = pygame.Color(0, 0, 0)
            else:
                screen_pixel_array[x, y] = model[(xAbs, yAbs)]
    print("finished lazy draw", file=stderr)

def main():
    state_is_dirty = True
    pygame.init()

    REDRAW_EVENT = pygame.USEREVENT + 1
    REDRAW_EVENT_TIME = 1200 # millis

    def moveToCoordsStart():
        nonlocal current_offset
        nonlocal current_scale
        START_OFFSET = (0, 0)
        START_SCALE = 1
        current_offset = START_OFFSET
        current_scale = START_SCALE

    screen_dims_start = (800, 600)
    moveToCoordsStart()
    screen = pygame.display.set_mode(screen_dims_start, pygame.RESIZABLE)
    screen_pixel_array = pygame.PixelArray(screen)

    running = True
    isDragging = False
    while running:
        for event in pygame.event.get():
            LEFT_MOUSE_BUTTON = 1
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.VIDEORESIZE:
                screen_pixel_array.close()
                screen_pixel_array = pygame.PixelArray(screen)
                pygame.display.flip()
                state_is_dirty = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == LEFT_MOUSE_BUTTON:
                    isDragging = True
                    pygame.time.set_timer(REDRAW_EVENT, 0, loops=1)
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == LEFT_MOUSE_BUTTON:
                    isDragging = False
                    pygame.time.set_timer(REDRAW_EVENT, REDRAW_EVENT_TIME, loops=1)
            elif event.type == pygame.MOUSEMOTION:
                if isDragging:
                    delta_x, delta_y = int(event.rel[0] * current_scale), int(event.rel[1] * current_scale)
                    current_offset = (current_offset[0] - delta_x, current_offset[1] - delta_y)
                    screen.scroll(event.rel[0], event.rel[1])
                    pygame.display.flip()
            elif event.type == pygame.MOUSEWHEEL:
                scale_const = 0.1
                # scale_mult = -scale_const * current_scale
                # current_scale += scale_mult * event.y
                current_scale *= 1 + scale_const * event.y
                screen_pixel_array.close()
                new_size = (screen.get_width() * (1 + scale_const * event.y),
                            screen.get_height() * (1 + scale_const * event.y))
                screen_center_coords = (screen.get_width() // 2, screen.get_height() // 2)
                scaled_version = pygame.transform.scale(screen, new_size).copy()
                left_high_corner_of_scaled_image = (screen_center_coords[0] - scaled_version.get_width() // 2,
                                                    screen_center_coords[1] - scaled_version.get_height() // 2)
                screen.fill(pygame.Color(0, 0, 0))
                screen.blit(scaled_version, left_high_corner_of_scaled_image)
                screen_pixel_array = pygame.PixelArray(screen)
                pygame.display.flip()
                pygame.time.set_timer(REDRAW_EVENT, REDRAW_EVENT_TIME, loops=1)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    state_is_dirty = True
                    moveToCoordsStart()
                if event.key == pygame.K_f:
                    pygame.time.set_timer(REDRAW_EVENT, 0, loops=1) # cancel event
                    state_is_dirty = True
            elif event.type == REDRAW_EVENT:
                state_is_dirty = True

        if state_is_dirty: # redraw (recalculate the whole thing)
            screen.fill((255, 255, 255))
            patch_model(screen_pixel_array, current_offset, (screen.get_width(), screen.get_height()), current_scale)
            state_is_dirty = False
            # do_lazy = True
            pygame.display.flip()
        
        # if do_lazy:
        #     draw_model_lazy(screen_pixel_array, current_offset)
        #     do_lazy = False
        #     pygame.display.flip()
            


    pygame.quit()

def printHelp():
    print("Press R to move to the starting point")

if __name__ == '__main__':
    printHelp()
    main()
