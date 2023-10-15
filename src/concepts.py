import math
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    """Function that applies a scalar multiplication to x in a quadratic function."""
    return 3 * x**2 - 4 * x + 5

def derivative(x, h):
    """Function that calculates the derivative programatically with some delta h."""
    print(f(x))

    # Positive delta h should give a positive increase
    print(f(x + h))

    # Calculate the change in slope of the function
    rise = f(x + h) - f(x)
    print(f"Rise of the function: {rise}")

    # Normalize the rise by dividing by the delta h
    run = h
    print(f"Slope of the function: {rise / run}")
    print("")

def complex_derivative():
    """Function that calculates the derivative programatically with multiple inputs."""
    h = 0.0001

    # Inputs
    a = 2.0
    b = -3.0
    c = 10.0

    # Calculate derivative of d for all a, b, and c
    d1 = a * b + c

    print(f"Complex derivative of a = {a}, b = {b}, c = {c}:")
    print('d1 (a * b + c): ', d1)

    # Calculate derivative of d with respect to a
    a += h
    d2 = a * b + c

    print(f"Complex derivative of a = {a}, b = {b}, c = {c} and h = {h}:")
    print('d2 ((a + h) * b + c): ', d2)
    print('Slope: ', (d2 - d1) / h)

    # Calculate derivative of d with respect to b
    a -= h
    b += h
    d3 = a * b + c

    print(f"Complex derivative of a = {a}, b = {b}, c = {c} and h = {h}:")
    print('d3 (a * (b + h) + c): ', d3)
    print('Slope: ', (d3 - d1) / h)

    # Calculate derivative of d with respect to c
    b -= h
    c += h
    d4 = a * b + c

    print(f"Complex derivative of a = {a}, b = {b}, c = {c} and h = {h}:")
    print('d4 (a * b + (c + h)): ', d4)
    print('Slope: ', (d4 - d1) / h)

def main():
    # Scalar muliplication f(x)
    print(f(3.0))

    # Vector from -5 to 5 with a step of 0.25
    xs = np.arange(-5, 5, 0.25)

    # Scalar multiplication of vector xs with f(x)
    ys = f(xs)
    print(ys)

    # plot of vectors xs and ys
    # plt.plot(xs, ys)
    # plt.show()

    # working out the derivative of f(x) programatically
    derivative(3.0, 0.0001)
    derivative(-3.0, 0.0001)

    # Calculating the derivative with respect to multiple inputs
    complex_derivative()



if __name__ == '__main__':
    main()