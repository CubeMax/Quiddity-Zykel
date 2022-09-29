
from math import sqrt, isqrt
from typing import Union

from ring.rational_numbers import Fraction


ERROR_DIFFERENT_FIELD = "Elements are from different quadratic fields!"


def is_square_number(n: int) -> bool:
    return n == isqrt(abs(n)) ** 2


class QuadraticField:
    def __init__(self, sqrt_d: int):
        if is_square_number(sqrt_d):
            raise ValueError("d has to be square-free.")
        self.d = sqrt_d

    def number(self, rational_part: Union[Fraction, int], sqrt_part: Union[Fraction, float]):
        return ComplexQuadratic(rational_part, sqrt_part, self.d)

    def get(self, rational_part: Union[Fraction, int], sqrt_part: Union[Fraction, float]):
        return self.number(rational_part, sqrt_part)

    def convert(self, number):
        if isinstance(number, int) or isinstance(number, Fraction):
            return ComplexQuadratic(number, 0, self.d)
        if isinstance(number, ComplexQuadratic):
            return number
        raise TypeError(number, type(number))


class ComplexQuadratic:  # z = x + y * sqrt(d)
    def __init__(self, rational_part: Union[Fraction, int], sqrt_part: Union[Fraction, float], sqrt_d: int):
        self.x = rational_part
        self.y = sqrt_part
        self.d = sqrt_d

    def same_field_as(self, other) -> bool:
        if isinstance(other, ComplexQuadratic) and self.d == other.d:
            return True
        return False

    def __add__(self, other):
        if isinstance(other, int) or isinstance(other, Fraction):
            return ComplexQuadratic(self.x + other, self.y, self.d)
        if self.same_field_as(other):
            return ComplexQuadratic(self.x + other.x, self.y + other.y, self.d)
        raise TypeError(ERROR_DIFFERENT_FIELD)

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        return self + -other

    def __rsub__(self, other):
        return other + -self

    def __neg__(self):
        return ComplexQuadratic(-self.x, -self.y, self.d)

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, Fraction):
            return ComplexQuadratic(self.x * other, self.y * other, self.d)
        if self.same_field_as(other):
            return ComplexQuadratic(self.x * other.x + self.y * other.y * self.d,
                                    self.x * other.y + self.y * other.x, self.d)
        raise TypeError(ERROR_DIFFERENT_FIELD)

    def __rmul__(self, other):
        return self * other

    def __pow__(self, power):
        if not isinstance(power, int):
            raise TypeError(power)
        if power == 0:
            return ComplexQuadratic(1, 0, self.d)
        if power > 0:
            return self * self.__pow__(power - 1)
        # power < 0:
        return 1 / self.__pow__(- power)

    def __truediv__(self, other):
        if isinstance(other, int):
            return ComplexQuadratic(self.x * Fraction(1, other), self.y * Fraction(1, other), self.d)
        if isinstance(other, Fraction):
            return ComplexQuadratic(self.x / other, self.y / other, self.d)
        if self.same_field_as(other):
            return self * other.conjugate() / other.norm()
        raise TypeError(ERROR_DIFFERENT_FIELD)

    def __rtruediv__(self, other):
        if isinstance(other, int) or isinstance(other, Fraction):
            return other * self.conjugate() / self.norm()
        raise TypeError(other, type(other))

    def __floordiv__(self, other):
        return self.__truediv__(other)

    def __rfloordiv__(self, other):
        return self.__rtruediv__(other)

    def __eq__(self, other):
        if isinstance(other, int) or isinstance(other, Fraction):
            return self.x == other and self.y == 0
        if self.same_field_as(other):
            return self.x == other.x and self.y == other.y

    def __abs__(self):
        if self.d == 0:
            return abs(self.x)
        if self.d > 0:
            return abs(self.x) + abs(self.y) * sqrt(self.d)
        return sqrt(abs(self.x)**2 - self.d * abs(self.y)**2)

    def __str__(self):
        x = self.x
        y = self.y
        if isinstance(x, Fraction) and x.is_integral():
            x = int(x)
        if isinstance(y, Fraction) and y.is_integral():
            y = int(y)

        sqrt_string = "\u221a"
        if self.d == -1:
            sqrt_d_as_string = "i"
        elif self.d < -1:
            sqrt_d_as_string = "i " + sqrt_string + str(-self.d)
        else:
            sqrt_d_as_string = sqrt_string + str(self.d)

        if y == 0:
            return str(x)
        if x == 0 and y == 1:
            return sqrt_d_as_string
        if x == 0 and y == -1:
            return "-" + sqrt_d_as_string
        if x == 0:
            return str(y) + sqrt_d_as_string
        if y == 1:
            return str(x) + " + " + sqrt_d_as_string
        if y == -1:
            return str(x) + " - " + sqrt_d_as_string
        if y > 0:
            return str(x) + " + " + str(y) + sqrt_d_as_string
        if y < 0:
            return str(x) + " - " + str(-y) + sqrt_d_as_string

    def get_latex(self):
        x = self.x
        y = self.y
        if isinstance(x, Fraction) and x.is_integral():
            x = int(x)
        if isinstance(y, Fraction) and y.is_integral():
            y = int(y)

        sqrt_string = "\\sqrt{"
        if self.d == -1:
            sqrt_d_as_string = "i"
        elif self.d < -1:
            sqrt_d_as_string = "i " + sqrt_string + str(-self.d) + "}"
        else:
            sqrt_d_as_string = sqrt_string + str(self.d) + "}"

        if y == 0:
            return repr(x)
        if x == 0 and y == 1:
            return sqrt_d_as_string
        if x == 0 and y == -1:
            return "- " + sqrt_d_as_string
        if x == 0:
            return repr(y) + " " + sqrt_d_as_string
        if y == 1:
            return repr(x) + " + " + sqrt_d_as_string
        if y == -1:
            return repr(x) + " - " + sqrt_d_as_string
        if y > 0:
            return repr(x) + " + " + repr(y) + " " + sqrt_d_as_string
        if y < 0:
            return repr(x) + " - " + repr(-y) + " " + sqrt_d_as_string

    def __repr__(self):
        return self.__str__()

    def __hash__(self):
        return hash((self.x, self.y, self.d))

    def conjugate(self):
        return ComplexQuadratic(self.x, - self.y, self.d)

    def norm(self) -> int:
        return self.x ** 2 - self.d * self.y ** 2

    def is_invertible(self) -> bool:
        if self.x == 0 and self.y == 0:
            return False
        return True

    def inverse(self):
        if self.x == 0 and self.y == 0:
            raise ZeroDivisionError
        return 1 / self


class Gauss(ComplexQuadratic):
    def __init__(self, rational_part: Union[Fraction, int], sqrt_part: Union[Fraction, float]):
        super().__init__(rational_part, sqrt_part, -1)


if __name__ == "__main__":
    z1 = ComplexQuadratic(1, 2, 7)
    z2 = ComplexQuadratic(2, -1, 7)

    print(z1)
    print(z2)

    print(z1.get_latex())
    print(z2.get_latex())

    print(z1 + z2)
    print(z1 * z2)
    print(z1 / z2)
    print(z1 ** 5)
    print((z1 ** 5).norm())
