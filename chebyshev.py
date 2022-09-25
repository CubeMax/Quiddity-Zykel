
from polynomial_ring import Polynomial


def chebyshev(n: int, delta: int = 1, variable_name: str = "x") -> Polynomial:
    if n <= 0:
        return Polynomial(0, variable_name=variable_name)
    if n == 1:
        return Polynomial(1, variable_name=variable_name)
    t_0 = Polynomial(0, variable_name=variable_name)
    t_1 = Polynomial(1, variable_name=variable_name)
    while n >= 2:
        t_2 = Polynomial(0, 1, variable_name=variable_name) * t_1 - delta * t_0
        t_0 = t_1
        t_1 = t_2
        n -= 1
    return t_1


if __name__ == "__main__":
    N = 14
    for i in range(N):
        print("t_" + str(i) + "^0", "=", chebyshev(i, delta=0))
    print()
    for i in range(N):
        print("t_" + str(i), "=", chebyshev(i))
    print()
    for i in range(N):
        print("t_" + str(i) + "^-1", "=", chebyshev(i, delta=-1))

