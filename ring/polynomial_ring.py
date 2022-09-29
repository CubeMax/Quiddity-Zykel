from typing import Tuple


class Polynomial:
    def __init__(self, *coefficients, variable_name: str = "x"):
        p_list = list(coefficients)
        while len(p_list) > 0 and p_list[-1] == 0:
            p_list.pop()
        if len(p_list) == 0:
            p_list = [0]
        self.p: tuple = tuple(p_list)
        self.variable_name = variable_name

    def degree(self) -> int:
        if len(self.p) == 1 and self.p[0] == 0:
            return -1
        return len(self.p) - 1

    def eval(self, x):
        return sum(self.p[i] * x**i for i in range(self.degree() + 1))

    def __add__(self, other):
        if isinstance(other, Polynomial):
            if self.variable_name != other.variable_name:
                raise TypeError("Can not add, because ", self.variable_name, "!=", other.variable_name)
            p_list = [0] * (max(self.degree(), other.degree()) + 1)
            for i in range(self.degree() + 1):
                p_list[i] += self.p[i]
            for i in range(other.degree() + 1):
                p_list[i] += other.p[i]
            return Polynomial(*p_list, variable_name=self.variable_name)
        return Polynomial(self.p[0] + other, *self.p[1:], variable_name=self.variable_name)

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        return self + -other

    def __rsub__(self, other):
        return other + -self

    def __neg__(self):
        return Polynomial(*[-c for c in self.p], variable_name=self.variable_name)

    def __mul__(self, other):
        if isinstance(other, Polynomial):
            if self.variable_name != other.variable_name:
                raise TypeError("Can not mul, because ", self.variable_name, "!=", other.variable_name)
            p_list = [0] * (self.degree() + other.degree() + 1)
            for i in range(self.degree() + 1):
                for j in range(other.degree() + 1):
                    p_list[i + j] += self.p[i] * other.p[j]
            return Polynomial(*p_list, variable_name=self.variable_name)
        return Polynomial(*[c * other for c in self.p], variable_name=self.variable_name)

    def __rmul__(self, other):
        return self * other

    def __pow__(self, power):
        if not isinstance(power, int) or power < 0:
            raise TypeError(power)
        if power == 0:
            return Polynomial(1, variable_name=self.variable_name)
        return self * pow(self, power - 1)

    def __eq__(self, other):
        if isinstance(other, Polynomial):
            if self.variable_name != other.variable_name:
                return False
            if self.degree() != other.degree():
                return False
            for i in range(self.degree() + 1):
                if self.p[i] != other.p[i]:
                    return False
            return True
        if self.degree() > 0:
            return False
        return self.p[0] == other

    def __str__(self):
        d = self.degree()
        polynomial_string = ""
        for i in range(d, -1, -1):
            c = self.p[i]
            if c != 0:
                if polynomial_string != "":
                    if c > 0:
                        polynomial_string += " + "
                    else:
                        polynomial_string += " - "
                        c = -c
                if i == 0 or c != 1:
                    polynomial_string += str(c) + " "
                if i == 1:
                    polynomial_string += self.variable_name
                elif i > 1:
                    polynomial_string += self.variable_name + "^" + str(i)
        if polynomial_string == "":
            return "0"
        return polynomial_string

    def get_latex(self):
        d = self.degree()
        polynomial_string = ""
        for i in range(d, -1, -1):
            c = self.p[i]
            if c != 0:
                if polynomial_string != "":
                    if c > 0:
                        polynomial_string += " + "
                    else:
                        polynomial_string += " - "
                        c = -c
                if i == 0 or c != 1:
                    polynomial_string += repr(c) + " "
                if i == 1:
                    polynomial_string += self.variable_name
                elif i > 1:
                    polynomial_string += self.variable_name + "^{" + str(i) + "}"
        if polynomial_string == "":
            return "0"
        return polynomial_string

    def __repr__(self):
        self.get_latex()

    def __hash__(self):
        return hash(*self.p)


def Monom(degree: int, variable: str = "x") -> Polynomial:
    if degree == 0:
        return Polynomial(1, variable_name=variable)
    return Polynomial(*[0] * degree, 1, variable_name=variable)


def division(a: Polynomial, b: Polynomial) -> Tuple[Polynomial, Polynomial]:
    from rational_numbers import Better_fraction as Fraction
    if a.variable_name != b.variable_name:
        raise TypeError(a.variable_name, "!=", b.variable_name)
    q = Polynomial(0, variable_name=a.variable_name)
    r = a
    d = b.degree()
    c = b.p[-1]
    while r.degree() >= d:
        s = Monom(r.degree() - d) * Fraction(r.p[-1], c)
        q = q + s
        r = r - s * b
    return q, r


def ggT(a: Polynomial, b: Polynomial) -> Polynomial:
    if a.variable_name != b.variable_name:
        raise TypeError(a.variable_name, "!=", b.variable_name)
    if a == 0:
        return b
    if b == 0:
        return a

    q, r = division(a, b)
    ggt = ggT(b, r)
    if ggt.p[-1] < 0:
        ggt = -ggt
    return ggt


if __name__ == "__main__":
    P = Polynomial(1, 2, 3, 4, 5, 6, variable_name="z")
    print("p(z) =", P)
