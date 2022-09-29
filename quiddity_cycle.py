
from sympy import divisors

from matrix import Matrix2x2 as Matrix


def identity() -> Matrix:
    return Matrix(1, 0, 0, 1)


# cycle = (c_1, ..., c_m)
def eta(*cycle, begin: int = 1, end: int = None) -> Matrix:
    m = len(cycle)
    product = identity()

    begin = max(1, begin)
    if end:
        end = min(m, end)
    else:
        end = m

    for c in cycle[begin - 1:end]:
        product @= Matrix(c, -1, 1, 0)
    return product


def is_quiddity_cycle(cycle: tuple, lamb=-1) -> bool:
    return eta(*cycle) == lamb * identity()


class QuiddityCycle:
    def __init__(self, *cycle):
        self.cycle: tuple = cycle
        self.length: int = len(cycle)
        self.lamb = None
        self.is_quiddity_cycle(warning=True)

    def is_quiddity_cycle(self, warning: bool = False) -> bool:
        if self.lamb:
            return True
        if is_quiddity_cycle(self.cycle, -1):
            self.lamb = -1
            return True
        if is_quiddity_cycle(self.cycle, 1):
            self.lamb = 1
            return True
        if warning:
            print("WARNING: Cycle", self.cycle, "is not a lambda-quiddity cycle!")
        return False

    def is_periodic(self) -> bool:
        cycle_len = self.length
        if cycle_len < 2:
            return False
        for d in divisors(cycle_len):
            if d < cycle_len:
                cycle = self.cycle[0: d]
                if cycle * (cycle_len // d) == self.cycle:
                    for k in range(1, cycle_len // d):
                        if is_quiddity_cycle(cycle * k, self.lamb):
                            return True
        return False

    def is_reducible(self) -> bool:
        m = len(self)
        if m < 3:
            return False
        if m > 3 and (-1 in self or 1 in self):
            return True
        for i in range(m):
            for j in range(i + 2, i + m - 1):
                if self.get_entry_in_frieze_pattern(i, j) in {-1, 1}:
                    return True
        return False

    def get_entry_in_frieze_pattern(self, i: int, j: int):
        if i > j - 2:
            raise ValueError("Entry out of frieze pattern!")
        if i == j:
            return 0
        if i + 1 == j:
            return 1
        frieze_matrix = identity()
        for k in range(i, j - 1):
            frieze_matrix @= eta(self.cycle[(k - 1) % len(self)])
        return frieze_matrix.a_1

    def __str__(self):
        return str(self.cycle)

    def get_latex(self):
        return repr(self.cycle)

    def __repr__(self):
        return self.get_latex()

    def __len__(self):
        return len(self.cycle)

    def __iter__(self):
        for c in self.cycle:
            yield c


if __name__ == "__main__":
    zykel = (1, 2) * 2
    qc = QuiddityCycle(*zykel)
    print(qc)
    print("periodic =", qc.is_periodic())
    print("reducible =", qc.is_reducible())

    print()

    zykel = (1, 3) * 9
    qc = QuiddityCycle(*zykel)
    print(qc)
    print("periodic =", qc.is_periodic())
    print("reducible =", qc.is_reducible())

    print()

    zykel = (-1, -1, -1)
    qc = QuiddityCycle(*zykel)
    print(qc)
    print("periodic =", qc.is_periodic())
    print("reducible =", qc.is_reducible())

    print()

    from ring.quadratic_field import Gauss
    K = 7
    twos = tuple(2 for _ in range(2 * K))
    neg_twos = tuple(-2 for _ in range(2 * K))
    zykel = (Gauss(0, 2), Gauss(1, -1), *twos, Gauss(1, 1), Gauss(0, -2), Gauss(-1, 1), *neg_twos, Gauss(-1, -1))
    qc = QuiddityCycle(*zykel)
    print(qc)
    print("periodic =", qc.is_periodic())
    print("reducible =", qc.is_reducible())
    # print(qc.get_entry_in_frieze_pattern(1, 2 * K + 5))
