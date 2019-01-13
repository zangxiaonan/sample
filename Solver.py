import math
import django

class Solver(object):
    def demo(self, a, b, c):
        if ((a + b - c * c) > 0):
            print(math.sqrt(c - 4 + 2))
        else:
            print("a")

            raise Exception("数值为负数！")


Solver().demo(2, 3, 1)
Solver().demo(3, 4, 1)

class Apple(object):
    pass
    print("sample3")


