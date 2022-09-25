
from sympy import divisors

from matrix import Matrix2x2 as Matrix


def is_quiddity_cycle(cycle: tuple, lamb=-1) -> bool:
    lambda_matrix = Matrix(lamb, 0, 0, lamb)
    cycle_matrix = Matrix(1, 0, 0, 1)
    for c in cycle:
        cycle_matrix @= Matrix(c, -1, 1, 0)
    return cycle_matrix == lambda_matrix


class QuiddityCycle:
    def __init__(self, *cycle, lamb=-1):
        self.cycle: tuple = cycle
        self.lamb = lamb

        if not self.is_quiddity_cycle():
            print("WARNING: Cycle", cycle, "is not a (" + str(lamb) + ")-quiddity cycle!")

    def is_quiddity_cycle(self) -> bool:
        return is_quiddity_cycle(self.cycle, self.lamb)

    def is_periodic(self) -> bool:
        cycle_len = len(self.cycle)
        for d in divisors(cycle_len):
            if d < cycle_len:
                cycle = self.cycle[0: d]
                if cycle * (cycle_len // d) == self.cycle:
                    for k in range(1, cycle_len // d):
                        if is_quiddity_cycle(cycle * k, self.lamb):
                            return True
        return False

    def __str__(self):
        return str(self.cycle)

    def get_latex(self):
        return repr(self.cycle)

    def __repr__(self):
        return self.get_latex()


if __name__ == "__main__":
    tc = (0, ) * 7
    qc = QuiddityCycle(*tc)
    print(qc)

    print()

    tc = (1, 2) * 2
    qc = QuiddityCycle(*tc)
    print(qc)
    print("periodic =", qc.is_periodic())

    print()

    tc = (1, 3) * 9
    qc = QuiddityCycle(*tc)
    print(qc)
    print("periodic =", qc.is_periodic())

    print()

    tc = (-1, -1, -1)
    qc = QuiddityCycle(*tc, lamb=1)
    print(qc)
    print("periodic =", qc.is_periodic())
