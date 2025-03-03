class Matrix2x2:
    def __init__(self, a, b, c, d):
        self.matrix = [[a, b], [c, d]]

    def __str__(self):
        return f'Matrix2x2({self.matrix[0][0]}, {self.matrix[0][1]}, {self.matrix[1][0]}, {self.matrix[1][1]})'
    
    def determinat(self):
        return self.matrix[0][0] * self.matrix[1][1] - self.matrix[0][1] * self.matrix[1][0]
    
    def __add__(self, other):
        return Matrix2x2(
            self.matrix[0][0] + other.matrix[0][0], self.matrix[0][1] + other.matrix[0][1],
            self.matrix[1][0] + other.matrix[1][0], self.matrix[1][1] + other.matrix[1][1]
        )

matrix1 = Matrix2x2(1, 2, 3, 4)
matrix2 = Matrix2x2(5, 6, 7, 8)

matrix3 = matrix1 + matrix2
print(matrix3)