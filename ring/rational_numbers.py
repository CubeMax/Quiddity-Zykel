from ring.ggT import ggT


class RationalNumbers:

    @staticmethod
    def number(numerator: int, denominator: int):
        return Fraction(numerator, denominator)

    @staticmethod
    def get(numerator: int, denominator: int):
        return Fraction(numerator, denominator)

    @staticmethod
    def convert(number):
        if isinstance(number, int):
            return Fraction(number, 1)
        if isinstance(number, Fraction):
            return number
        raise TypeError(number)


class Fraction:  # fraction = p/q
    def __init__(self, numerator: int, denominator: int, reduce: bool = True):
        if denominator == 0:
            raise ZeroDivisionError

        self.p = numerator
        self.q = denominator

        if reduce:
            d = ggT(numerator, denominator)
            self.p = numerator // d
            self.q = denominator // d

        if self.q < 0:
            self.p = - self.p
            self.q = - self.q

    def __int__(self):
        return int(self.p // self.q)

    def __add__(self, other):
        if isinstance(other, Fraction):
            return Fraction(self.p * other.q + self.q * other.p, self.q * other.q)
        if isinstance(other, int):
            return Fraction(self.p + self.q * other, self.q)
        raise TypeError(other, type(other))

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        return self + -other

    def __rsub__(self, other):
        return other + -self

    def __neg__(self):
        return Fraction(-self.p, self.q)

    def __mul__(self, other):
        if isinstance(other, Fraction):
            return Fraction(self.p * other.p, self.q * other.q)
        if isinstance(other, int):
            return Fraction(self.p * other, self.q)
        raise TypeError(other, type(other))

    def __rmul__(self, other):
        return self * other

    def __pow__(self, power):
        return Fraction(pow(self.p, power), pow(self.q, power), reduce=False)

    def __truediv__(self, other):
        if isinstance(other, Fraction):
            return Fraction(self.p * other.q, self.q * other.p)
        if isinstance(other, int):
            return Fraction(self.p, self.q * other)
        raise TypeError(other, type(other))

    def __rtruediv__(self, other):
        if isinstance(other, int):
            return Fraction(other * self.q, self.p)
        raise TypeError(other, type(other))

    def __floordiv__(self, other):
        return self.__truediv__(other)

    def __rfloordiv__(self, other):
        return self.__rtruediv__(other)

    def __eq__(self, other):
        if isinstance(other, int):
            return other * self.q == self.p
        if isinstance(other, Fraction):
            return self.p * other.q == self.q * other.p
        raise TypeError(other, type(other))

    def __gt__(self, other):
        if isinstance(other, int):
            return self.p > other * self.q
        if isinstance(other, Fraction):
            return self.p * other.q > self.q * other.p
        raise TypeError(other, type(other))

    def __ge__(self, other):
        if isinstance(other, int):
            return self.p >= other * self.q
        if isinstance(other, Fraction):
            return self.p * other.q >= self.q * other.p
        raise TypeError(other, type(other))

    def __lt__(self, other):
        if isinstance(other, int):
            return self.p < other * self.q
        if isinstance(other, Fraction):
            return self.p * other.q < self.q * other.p
        raise TypeError(other, type(other))

    def __le__(self, other):
        if isinstance(other, int):
            return self.p <= other * self.q
        if isinstance(other, Fraction):
            return self.p * other.q <= self.q * other.p
        raise TypeError(other, type(other))

    def __abs__(self):
        return abs(self.p / self.q)

    def __float__(self):
        return self.p / self.q

    def __str__(self):
        if self.q == 1:
            return str(self.p)
        return str(self.p) + "/" + str(self.q)

    def get_latex(self):
        if self.q == 1:
            return str(self.p)
        return "\\frac{" + str(self.p) + "}{" + str(self.q) + "}"

    def __repr__(self):
        return self.get_latex()

    def __hash__(self):
        return hash((self.p, self.q))

    def is_invertible(self) -> bool:
        if self.p == 0:
            return False
        return True

    def inverse(self):
        if self.p == 0:
            raise ZeroDivisionError
        return Fraction(self.q, self.p)

    def is_integral(self) -> bool:
        if self.q == 1:
            return True
        return False


# convert from continued fraction to one fraction
def Better_fraction(a, b):
    if isinstance(a, Fraction):
        return Better_fraction(a.p, a.q * b)
    if isinstance(b, Fraction):
        return Better_fraction(b.q * a, b.p)
    return Fraction(a, b)


if __name__ == "__main__":
    r = Fraction(3, 17)
    s = Fraction(5, -3)
    print(r.inverse())
    print(r + s, r*s, r/s)
    print(r < s)
    print(abs(r), int(s))
    print(7 - Fraction(3, 4))

    z = Better_fraction(r, s)
    print(z.get_latex())
