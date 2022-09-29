
from ring.quadratic_field import ComplexQuadratic
from ring.rational_numbers import Fraction
from quiddity_cycle import QuiddityCycle
from frieze_pattern import FriezePattern
from chebyshev import chebyshev

show_chapter_3 = False
show_chapter_4 = False
show_chapter_5 = False
show_chapter_6 = False
show_chapter_9 = False
show_chapter_10 = False

if __name__ == "__main__":
    if show_chapter_3:
        print("3 Einleitung")
        print("============")
        cycle = (5, 1, 2, 4, 1, 2, 3, 2, 1)
        # qc = QuiddityCycle(*cycle, lamb=-1)
        frieze = FriezePattern(cycle)
        print("Höhe:", frieze.height)
        print(frieze.get_tableaux_horizontal())
        # print(frieze.get_latex_horizontal())

        print("============")
        cycle = (3, 1) * 3
        # qc = QuiddityCycle(*cycle, lamb=-1)
        frieze = FriezePattern(cycle)
        print("Höhe:", frieze.height)
        print(frieze.get_tableaux_horizontal())
        # print(frieze.get_latex_horizontal())

        print("============")
        cycle = (3, 1) * 9
        qc = QuiddityCycle(*cycle)
        frieze = FriezePattern(cycle)
        print("Höhe:", frieze.height)
        print(frieze.get_tableaux_horizontal(12))
        # print(frieze.get_latex_horizontal(12))
        print(cycle, "is_periodic:", qc.is_periodic())
        print()

    if show_chapter_4:
        print("4 Friesmuster")
        print("=============")
        cycle = (1, 3, 3, 1, 2, 3, 2)
        # qc = QuiddityCycle(*cycle, lamb=-1)
        frieze = FriezePattern(cycle)
        print("Höhe:", frieze.height)
        print("is_tame:", frieze.is_tame())
        print(frieze.get_tableaux_horizontal())
        # print(frieze.get_latex_horizontal())

        print("=============")
        cycle = (2, 1, 2, 1) * 3
        # qc = QuiddityCycle(*cycle, lamb=-1)
        frieze = FriezePattern(cycle)
        print("Höhe:", frieze.height)
        print("is_tame:", frieze.is_tame())
        print(frieze.get_tableaux_horizontal(8))
        # print(frieze.get_latex_horizontal(8))

        print("=============")
        cycle = (ComplexQuadratic(2, 1, 3), 1) * 6
        qc = QuiddityCycle(*cycle)
        print(cycle)
        frieze = FriezePattern(cycle)
        print("Höhe:", frieze.height)
        print("is_tame:", frieze.is_tame())
        print("is_periodic:", qc.is_periodic())
        print(frieze.get_tableaux_horizontal(8))
        # print(frieze.get_latex_horizontal(8))
        print()

    if show_chapter_5:
        print("5 lambda-Quiddity-Zykel")
        print("=======================")
        cycle = (0, 0)
        qc = QuiddityCycle(*cycle)
        print(cycle, "is qc:", qc.is_quiddity_cycle())

        cycle = (1, 1, 1)
        qc = QuiddityCycle(*cycle)
        print(cycle, "is qc:", qc.is_quiddity_cycle())

        cycle = (-1, -1, -1)
        qc = QuiddityCycle(*cycle)
        print(cycle, "is qc:", qc.is_quiddity_cycle())

        cycle = (ComplexQuadratic(0, 1, 3), ) * 6
        qc = QuiddityCycle(*cycle)
        print(cycle, "is qc:", qc.is_quiddity_cycle())

        cycle = (ComplexQuadratic(0, 1, 2), 0, ComplexQuadratic(0, -1, 2), 0)
        qc = QuiddityCycle(*cycle)
        print(cycle, "is qc:", qc.is_quiddity_cycle())

        cycle = (ComplexQuadratic(0, 1, 5),
                 ComplexQuadratic(0, Fraction(3, 5), 5),
                 ComplexQuadratic(0, Fraction(2, 3), 5),
                 ComplexQuadratic(0, Fraction(9, 5), 5)
                 ) * 2
        qc = QuiddityCycle(*cycle)
        print(cycle, "is qc:", qc.is_quiddity_cycle())

        print()

        cycle = (-1, -1, -1)
        qc = QuiddityCycle(*cycle)
        print(cycle, "is aperiodic:", not qc.is_periodic())

        cycle = (1, 2) * 2
        qc = QuiddityCycle(*cycle)
        print(cycle, "is aperiodic:", not qc.is_periodic())

        cycle = (1, 3) * 3
        qc = QuiddityCycle(*cycle)
        print(cycle, "is aperiodic:", not qc.is_periodic())

        cycle = (ComplexQuadratic(0, 1, 2), ) * 4
        qc = QuiddityCycle(*cycle)
        print(cycle, "is aperiodic:", not qc.is_periodic())

        cycle = (ComplexQuadratic(0, 1, 3), ) * 6
        qc = QuiddityCycle(*cycle)
        print(cycle, "is aperiodic:", not qc.is_periodic())

        cycle = (ComplexQuadratic(0, 1, 3), ) * 12
        qc = QuiddityCycle(*cycle)
        print(cycle, "is aperiodic:", not qc.is_periodic())
        print()

    if show_chapter_6:
        print("6 Variante Tschebyschow-Polynome zweiter Art")
        print("============================================")
        N = 7
        for i in range(N + 1):
            print("t_" + str(i) + "^0(x)", "=", chebyshev(i, delta=0))
        print()
        for i in range(N + 1):
            print("t_" + str(i) + "(x)", "=", chebyshev(i))
        print()
        for i in range(N + 1):
            print("t_" + str(i) + "^-1(x)", "=", chebyshev(i, delta=-1))
        print()

    if show_chapter_9:
        print("9 Berechnung von lambda-Quiddity-Zykeln")
        print("=======================================")
        cycle = (ComplexQuadratic(0, 1, -3), ComplexQuadratic(0, -1, -3)) * 3
        qc = QuiddityCycle(*cycle)
        print(cycle, "is aperiodic:", not qc.is_periodic())

        cycle = (ComplexQuadratic(0, -1, -3), ComplexQuadratic(0, 1, -3)) * 3
        qc = QuiddityCycle(*cycle)
        print(cycle, "is aperiodic:", not qc.is_periodic())

    if show_chapter_10:
        print("10 Aperiodische lambda-Quiddity-Zykeln über algebraischen Erweiterungen")
        print("=======================================================================")
        for i in range(14):
            print("theta_" + str(i) + "(t)", "=", chebyshev(i, variable_name="t"))
        print()
