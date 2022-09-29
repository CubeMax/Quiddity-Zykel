
from math import sqrt
from typing import Union


PRECISION = 2
LATEX_I = "\\i"


class ComplexNumbers:

    @staticmethod
    def number(real_part: Union[int, float], imaginary_part: Union[int, float]):
        return Complex(real_part, imaginary_part)

    @staticmethod
    def get(real_part: Union[int, float], imaginary_part: Union[int, float]):
        return Complex(real_part, imaginary_part)

    @staticmethod
    def convert(number):
        if isinstance(number, int) or isinstance(number, float):
            return Complex(number, 0)
        if isinstance(number, Complex):
            return number
        raise TypeError(number)


class Complex:  # z = re + i * im
    def __init__(self, real_part: Union[float, int], imaginary_part: Union[float, float]):
        self.re = real_part
        self.im = imaginary_part

    def __add__(self, other):
        if isinstance(other, Complex):
            return Complex(self.re + other.re, self.im + other.im)
        if isinstance(other, int) or isinstance(other, float):
            return Complex(self.re + other, self.im)
        raise TypeError(other, type(other))

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        return self + -other

    def __rsub__(self, other):
        return other + -self

    def __neg__(self):
        return Complex(-self.re, -self.im)

    def __mul__(self, other):
        if isinstance(other, Complex):
            return Complex(self.re * other.re - self.im * other.im, self.re * other.im + self.im * other.re)
        if isinstance(other, int) or isinstance(other, float):
            return Complex(self.re * other, self.im * other)
        raise TypeError(other, type(other))

    def __rmul__(self, other):
        return self * other

    def __pow__(self, power):
        if not isinstance(power, int):
            raise TypeError(power)
        if power == 0:
            return Complex(1, 0)
        if power > 0:
            return self * self.__pow__(power - 1)
        # power < 0:
        return 1 / self.__pow__(- power)

    def __truediv__(self, other):
        if isinstance(other, Complex):
            return self * other.conjugate() / (other.re ** 2 + other.im ** 2)
        if isinstance(other, int) or isinstance(other, float):
            return Complex(self.re / other, self.im / other)
        raise TypeError(other, type(other))

    def __rtruediv__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return other * self.conjugate() / (self.re ** 2 + self.im ** 2)
        raise TypeError(other, type(other))

    def __floordiv__(self, other):
        return self.__truediv__(other)

    def __rfloordiv__(self, other):
        return self.__rtruediv__(other)

    def __eq__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return self.re == other and self.im == 0
        if isinstance(other, Complex):
            return self.re == other.re and self.im == other.im
        raise TypeError(other, type(other))

    def __abs__(self):
        return sqrt(self.re ** 2 + self.im ** 2)

    def __str__(self):
        re = round(self.re, PRECISION)
        im = round(self.im, PRECISION)
        if isinstance(re, float) and re.is_integer():
            re = int(re)
        if isinstance(im, float) and im.is_integer():
            im = int(im)

        if re == 0:
            return str(im) + "i"
        if im == 0:
            return str(re)
        if im == 1:
            return str(re) + " + " + "i"
        if im == -1:
            return str(re) + " - " + "i"
        if im > 0:
            return str(re) + " + " + str(im) + "i"
        if im < 0:
            return str(re) + " - " + str(-im) + "i"

    def get_latex(self):
        re = round(self.re, PRECISION)
        im = round(self.im, PRECISION)
        if isinstance(re, float) and re.is_integer():
            re = int(re)
        if isinstance(im, float) and im.is_integer():
            im = int(im)

        if re == 0:
            return str(im) + LATEX_I
        if im == 0:
            return str(re)
        if im == 1:
            return str(re) + " + " + LATEX_I
        if im == -1:
            return str(re) + " - " + LATEX_I
        if im > 0:
            return str(re) + " + " + str(im) + LATEX_I
        if im < 0:
            return str(re) + " - " + str(-im) + LATEX_I

    def __repr__(self):
        return self.get_latex()

    def __hash__(self):
        return hash((self.re, self.im))

    def conjugate(self):
        return Complex(self.re, - self.im)

    def is_invertible(self) -> bool:
        if self.re == 0 and self.im == 0:
            return False
        return True

    def inverse(self):
        if self.re == 0 and self.im == 0:
            raise ZeroDivisionError
        return 1 / self


if __name__ == "__main__":
    z1 = Complex(3, 2)
    z2 = Complex(0, -3)

    print(z1 + z2)
    print(z1 * z2)
    print(z1 / z2)
    print(z1 ** 5)
    print(z1.get_latex())
