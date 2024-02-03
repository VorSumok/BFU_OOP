import numpy as np

class Integral:
    def __init__(self, function, start, end):
        self.function = function
        self.start = start
        self.end = end

    def Calc(self):
        pass
class Sym(Integral):
    def Calc(self):
        return (self.end - self.start) * (self.function(self.end) + self.function(self.start)
                                          + 4 * self.function((self.end + self.start) / 2)) / 6

class Trap(Integral):
    def Calc(self):
        total = 0
        array = np.linspace(self.start, self.end, 1000)
        for i in array:
            total += 2 * self.function(i)
        result = (array[1] - array[0]) * (total - self.function(array[0])
                                          - self.function(array[-1])) / 2
        return result

def func(x):
    return x ** 3


if __name__ == '__main__':

    print(f"Метод Сипсона: {Sym(func, 0, 2).Calc()}")
    print(f"Метод Трапеций: {Trap(func, 0, 2).Calc()}")