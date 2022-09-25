from ggT import bezout, ggT


class IntegersModulo:  # Z_pZ with p > 1
    def __init__(self, modulo_p: int):
        if modulo_p < 2:
            raise ValueError("Modulo has to be at least 2.")
        self.mod_p = modulo_p

    def number(self, integer: int):
        return Modulus(integer, self.mod_p)

    def get(self, integer: int):
        return self.number(integer)

    def convert(self, number):
        if isinstance(number, int):
            return Modulus(number, self.mod_p)
        if isinstance(number, Modulus):
            return number
        raise TypeError(number)


class Modulus:  # n (mod p)
    def __init__(self, integer_n: int, modulo_p: int):
        self.__name__ = "Z/" + str(modulo_p) + "Z"
        # In Python, Modulo-Rechnung % liefert stets positive Werte --> -2 % 5 = 3
        self.n = integer_n % modulo_p
        self.mod = modulo_p

    def __int__(self):
        return self.n

    def __add__(self, other):
        if isinstance(other, Modulus):
            return Modulus(self.n + other.n, self.mod)
        if isinstance(other, int):
            return Modulus(self.n + other, self.mod)
        raise TypeError(other, type(other))

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        return self + -other

    def __rsub__(self, other):
        return other + -self

    def __neg__(self):
        return Modulus(-self.n, self.mod)

    def __mul__(self, other):
        if isinstance(other, Modulus):
            return Modulus(self.n * other.n, self.mod)
        if isinstance(other, int):
            return Modulus(self.n * other, self.mod)
        raise TypeError(other, type(other))

    def __rmul__(self, other):
        return self * other

    def __pow__(self, power):
        return Modulus(pow(self.n, power, self.mod), self.mod)

    def __truediv__(self, other):
        if isinstance(other, Modulus):
            return self * other.inverse()
        if isinstance(other, int):
            return self * Modulus(other, self.mod).inverse()
        raise TypeError(other, type(other))

    def __rtruediv__(self, other):
        if isinstance(other, int):
            return Modulus(other, self.mod) * self.inverse()
        raise TypeError(other, type(other))

    def __floordiv__(self, other):
        return self.__truediv__(other)

    def __rfloordiv__(self, other):
        return self.__rtruediv__(other)

    def __eq__(self, other):
        if isinstance(other, int):
            return self.n == other
        if isinstance(other, Modulus):
            return self.n == other.n
        raise TypeError(other, type(other))

    def __abs__(self):
        return abs(self.n)

    def __str__(self):
        return str(self.n)

    def __repr__(self):
        return str(self.n)  # + " (mod " + str(self.mod) + ")"

    def __gt__(self, other):
        return self.n > other

    def __ge__(self, other):
        return self.n >= other

    def __lt__(self, other):
        return self.n < other

    def __le__(self, other):
        return self.n <= other

    def __divmod__(self, divisor):
        q, r = divmod(self.n, divisor)
        return Modulus(q, self.mod), Modulus(r, self.mod)

    def __hash__(self):
        return hash((self.n, self.mod))

    def is_invertible(self) -> bool:
        g = ggT(self.n, self.mod)
        if g == 1:
            return True
        return False

    def inverse(self):
        g, s, t = bezout(self.n, self.mod)  # ggt = g = s * n + t * p
        if g == 1:
            return Modulus(s, self.mod)
        else:
            raise ValueError("The number " + repr(self.n) + " has no inverse in Z/" + str(self.mod) + "Z.")


if __name__ == "__main__":
    Z51 = IntegersModulo(51)
    n = Z51.number(2)
    print(n.inverse())
    print(n**1221)
