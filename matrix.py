

class Matrix2x2:
    def __init__(self, a_1, a_2, a_3, a_4):
        self.a_1 = a_1
        self.a_2 = a_2
        self.a_3 = a_3
        self.a_4 = a_4

    def get_trace(self):
        return self.a_1 + self.a_4

    def get_determinate(self):
        return self.a_1 * self.a_4 - self.a_2 * self.a_3

    def __add__(self, other):
        if isinstance(other, Matrix2x2):
            return Matrix2x2(self.a_1 + other.a_1,
                             self.a_2 + other.a_2,
                             self.a_3 + other.a_3,
                             self.a_4 + other.a_4
                             )
        else:
            raise TypeError

    def __matmul__(self, other):
        if isinstance(other, Matrix2x2):
            return Matrix2x2(self.a_1 * other.a_1 + self.a_2 * other.a_3,
                             self.a_1 * other.a_2 + self.a_2 * other.a_4,
                             self.a_3 * other.a_1 + self.a_4 * other.a_3,
                             self.a_3 * other.a_2 + self.a_4 * other.a_4
                             )
        else:
            raise TypeError

    def __eq__(self, other) -> bool:
        if isinstance(other, Matrix2x2):
            if self.a_1 == other.a_1 and self.a_2 == other.a_2 and self.a_3 == other.a_3 and self.a_4 == other.a_4:
                return True
            else:
                return False
        else:
            return False

    def __str__(self):
        return "(" + str(self.a_1) + ", " + str(self.a_2) + "; " + str(self.a_3) + ", " + str(self.a_4) + ")"

    def get_latex(self):
        return "\\mat{\n" + repr(self.a_1) + " & " + repr(self.a_2) + " \\\\ \n" \
               + repr(self.a_3) + " & " + repr(self.a_4) + "\n}"

    def __repr__(self):
        return self.get_latex()


class Matrix3x3:
    def __init__(self, a_1, a_2, a_3, a_4, a_5, a_6, a_7, a_8, a_9):
        self.a_1 = a_1
        self.a_2 = a_2
        self.a_3 = a_3
        self.a_4 = a_4
        self.a_5 = a_5
        self.a_6 = a_6
        self.a_7 = a_7
        self.a_8 = a_8
        self.a_9 = a_9

    def get_trace(self):
        return self.a_1 + self.a_5 + self.a_9

    def get_determinate(self):
        return self.a_1 * self.a_5 * self.a_9 + self.a_2 * self.a_6 * self.a_7 + self.a_3 * self.a_4 * self.a_8 \
               - self.a_3 * self.a_5 * self.a_7 - self.a_1 * self.a_6 * self.a_8 - self.a_2 * self.a_4 * self.a_9


if __name__ == "__main__":
    M = Matrix2x2(2, 3, 4, 5)
    print(M.get_latex())
