import math
import numpy as np

class Value:

    def __init__(self, data, _children=(), _op = ''):
        """Initialize the value class."""
        self.data = data
        # Children nodes of the resulting value object
        self._prev = set(_children)
        # Operation that was performed to get the resulting value object
        self._op = _op

    def __repr__(self):
        """Return the string representation of the value."""
        return f"Value(data={self.data})"
    
    def __add__(self, other):
        """Add two value class objects together."""
        out = Value(self.data + other.data, (self, other), '+') # storing the previous nodes
        return out
    
    def __mul__(self, other):
        """Multiply two value class objects together."""
        out = Value(self.data * other.data, (self, other), '*') # storing the previous nodes
        return out


def main():
    # Testing Value class

    a = Value(2.0)
    b = Value(-3.0)
    c = Value(10.0)

    print(a)
    print(b)
    print(a + b)
    print(a * b)
    d = a * b + c
    print(d)
    print(d._prev)
    print(d._op)


if __name__ == "__main__":
    main()