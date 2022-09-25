from typing import List

from matrix import Matrix2x2 as Matrix
from quiddity_cycle import is_quiddity_cycle

SPACING = 2


class Empty:
    def __init__(self, i: int = None, j: int = None):
        self.i = i
        self.j = j

    def __repr__(self):
        if self.i is None or self.j is None:
            return " "
        return "c_" + str(self.i) + "," + str(self.j)

    def __str__(self):
        return " "


class FriezePattern:
    def __init__(self, quiddity_cycle: tuple, field=None):
        self.field = field

        if not is_quiddity_cycle(quiddity_cycle):
            print("WARNING: Cycle", quiddity_cycle, "is not a (-1)-quiddity cycle!")
        self.quiddity_cycle: tuple = quiddity_cycle
        self.quiddity_length = len(quiddity_cycle)

        self.height: int = self.quiddity_length - 3
        self.height_skew: int = self.quiddity_length
        self.width_skew: int = 2 * self.quiddity_length
        self.height_hori: int = self.quiddity_length + 1
        self.width_hori: int = 2 * self.quiddity_length

        self.pattern_skew: List[list] = [[None for _ in range(self.width_skew)] for _ in range(self.height_skew)]
        self.pattern_hori: List[list] = [[None for _ in range(self.width_hori)] for _ in range(self.height_hori)]

        self.setup()

    def setup(self):
        if self.field:
            self.convert_quiddity()
        self.fill_tableaux_skew()
        self.fill_tableaux_hori()

    # convert quiddity cycle to field
    def convert_quiddity(self):
        self.quiddity_cycle = tuple(self.field.convert(number) for number in self.quiddity_cycle)

    def calculate_entry(self, i: int, j: int):
        if i == j + 1 or j == self.height + i + 4:
            return 1
        if i == j + 2:
            return 0
        m_ij = Matrix(1, 0, 0, 1)
        for k in range(i, j + 1):
            eta = Matrix(self.quiddity_cycle[k % self.quiddity_length], -1, 1, 0)
            m_ij = m_ij @ eta
        return m_ij.a_1

    def fill_tableaux_skew(self):
        for i in range(self.height_skew):
            for j in range(-2, self.width_skew):
                if i - 2 <= j <= self.quiddity_length + i - 2:
                    self.pattern_skew[i][j + 2] = self.calculate_entry(i, j)
                elif 0 <= j + 2 < self.width_skew:
                    self.pattern_skew[i][j + 2] = Empty()

    def fill_tableaux_hori(self):
        for i in range(self.height_hori):
            for j in range(self.height_skew):
                self.pattern_hori[i][(2 * j + i - 2) % self.width_hori] = self.pattern_skew[j][(j + i) % self.width_skew]
                self.pattern_hori[i][(2 * j + i - 1) % self.width_hori] = Empty()

    # True if all entries are positive
    def is_positive(self) -> bool:
        for row in self.pattern_skew:
            for entry in row:
                if entry <= 0:
                    return False
        return True

    # True if all entries are integers
    def is_integral(self) -> bool:
        for row in self.pattern_skew:
            for entry in row:
                if isinstance(entry, float):
                    if not entry.is_integer():
                        return False
                elif not isinstance(entry, int):
                    return False
        return True

    def determinant_3_x_3(self, i: int, j: int):
        c = self.pattern_skew
        return \
            c[i][j] * c[i + 1][j + 1] * c[i + 2][j + 2] \
            + c[i][j + 1] * c[i + 1][j + 2] * c[i + 2][j] \
            + c[i][j + 2] * c[i + 1][j] * c[i + 2][j + 1] \
            - c[i + 2][j] * c[i + 1][j + 1] * c[i][j + 2] \
            - c[i + 2][j + 1] * c[i + 1][j + 2] * c[i][j] \
            - c[i + 2][j + 2] * c[i + 1][j] * c[i][j + 1]

    # True if every complete adjacent 3 x 3-submatrix has determinant 0
    def is_tame(self) -> bool:
        for i in range(self.height_skew - 2):
            for j in range(i + 2, i + self.height + 2):
                if self.determinant_3_x_3(i, j) != 0:
                    return False
        return True

    # get max string length of each entry
    def get_max_string_width(self) -> int:
        return max([max(len(str(entry)) for entry in row) for row in self.pattern_skew])

    # get tableaux as string
    def get_tableaux_skew(self) -> str:
        max_width = self.get_max_string_width()
        tableuax = ""
        for row in self.pattern_skew:
            for entry_ij in row:
                tableuax += " " * (max_width - len(str(entry_ij))) + str(entry_ij) + " " * SPACING
            tableuax += "\n"
        return tableuax

    # get tableaux as string
    def get_tableaux_horizontal(self, max_columns: int = None) -> str:
        if max_columns:
            max_columns = min(max_columns, self.width_hori)
        else:
            max_columns = self.width_hori
        max_width = max(self.get_max_string_width(), 2)
        tableuax = ""
        for row in self.pattern_hori:
            if max_columns:
                row = row[:max_columns]
            for entry_ij in row:
                tableuax += " " * (max_width - len(str(entry_ij))) + str(entry_ij) + " " * SPACING
            tableuax += "\n"
        return tableuax

    def get_latex_skew(self):
        max_width = max(self.get_max_string_width(), 2)
        phantom = "\\phantom{" + "p" * max_width + "} "

        latex_code = "\\begin{array}{"
        latex_code += "c" * self.width_skew + "}\n"
        latex_code += "\\ddots & " + phantom + ("& " + phantom) * self.height + "& \\ddots & "
        latex_code += ("& " + phantom) * (self.width_skew - self.height - 4) + " \\\\ \n"
        for row in self.pattern_skew:
            latex_code += " & ".join(map(repr, row))
            latex_code += " \\\\ \n"
        latex_code += " & " * (self.width_skew - self.height - 4)
        latex_code += "& \\ddots " + "& " * self.height + "& & \\ddots " + " \\\\ \n"
        latex_code += "\\end{array}"
        return latex_code

    def get_latex_horizontal(self, max_columns: int = None):
        if max_columns:
            max_columns = min(max_columns, self.width_hori)
        else:
            max_columns = self.width_hori
        max_width = max(self.get_max_string_width(), 2)
        phantom = "\\phantom{" + "p" * max_width + "} "

        latex_code = "\\begin{array}{"
        latex_code += "c" * max_columns + "}\n"
        for row in self.pattern_hori:
            if max_columns:
                row = row[:max_columns]
            latex_code += " & ".join(map(repr, row))
            latex_code += " \\\\ \n"
        latex_code += "\\end{array}"
        return latex_code

    def __str__(self):
        return self.get_tableaux_skew()

    def __repr__(self):
        return str(self.pattern_skew)


if __name__ == "__main__":
    qc = (0, ) * 6
    F = FriezePattern(qc)
    print("tame =", F.is_tame())
    print(F.get_tableaux_horizontal())
    print((F.get_latex_horizontal(4)))

    from quadratic_field import ComplexQuadratic
    qc = (ComplexQuadratic(0, 1, -3), ComplexQuadratic(0, -1, -3)) * 3
    F = FriezePattern(qc)
    print(F.get_tableaux_horizontal())
    print((F.get_latex_horizontal(4)))


