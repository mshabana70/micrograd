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
    a = 2.0
    b = -3.0
    c = 10.0
    d = a * b + c

    print("Complex derivative of a = {a}, b = {b}, c = {c}:")
    print(d)

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