class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = [[0 for _ in range(cols)] for _ in range(rows)]

    def __str__(self):
        matrix_str = ""
        for row in self.data:
            matrix_str += " ".join(str(x) for x in row) + "\n"
        return matrix_str

    def set_data(self, data):
        if len(data) == self.rows and len(data[0]) == self.cols:
            self.data = data
        else:
            print("Invalid data dimensions")

    def add(self, other_matrix):
        if self.rows == other_matrix.rows and self.cols == other_matrix.cols:
            result = Matrix(self.rows, self.cols)
            for i in range(self.rows):
                for j in range(self.cols):
                    result.data[i][j] = self.data[i][j] + other_matrix.data[i][j]
            return result
        else:
            print("Matrix dimensions do not match for addition.")
            return None

    def multiply(self, other_matrix):
        if self.cols == other_matrix.rows:
            result = Matrix(self.rows, other_matrix.cols)
            for i in range(self.rows):
                for j in range(other_matrix.cols):
                    dot_product = 0
                    for k in range(self.cols):
                        dot_product += self.data[i][k] * other_matrix.data[k][j]
                    result.data[i][j] = dot_product
            return result
        else:
            print("Matrix dimensions are not suitable for multiplication.")
            return None

matrix1 = Matrix(3, 3)
matrix1.set_data([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

matrix2 = Matrix(3, 3)
matrix2.set_data([[10, 11, 12], [13, 14, 15], [16, 17, 18]])

print("Matrix 1:")
print(matrix1)

print("Matrix 2:")
print(matrix2)

result_addition = matrix1.add(matrix2)
if result_addition:
    print("Addition result:")
    print(result_addition)

result_multiplication = matrix1.multiply(matrix2)
if result_multiplication:
    print("Multiplication result:")
    print(result_multiplication)
