import math


class StackMax:

    def __init__(self):
        self._stack = []

    def pop(self):
        self._stack.pop()

    def push(self, value):
        self._stack.append(value)

    def max(self):
        return max(self._stack)
