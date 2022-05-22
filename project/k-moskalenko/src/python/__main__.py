from mandelbrot import calculate_point

if __name__ == '__main__':
    point = -0.75, 0.05
    result = calculate_point(*point)
    print(f'The value at {point} is equal to {result}.')
