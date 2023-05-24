import random

class Matrix:
    def __init__(self, rows, columns) -> None:
        matrix = []
        for i in range(rows):
            matrix.append([])
            for j in range(columns):
                matrix[i].append(0)
        self.matrix = matrix
        self.rows = rows
        self.columns = columns
    
    def printMatrix(self):
        for i in range(self.rows):
            print("[" + ", ".join(map(str, self.matrix[i])) + "]")

    def edit(self):
        print("Enter new matrix:")
        for j in range(self.rows):
            self.matrix[j] = list(map(int, input().split()))

    def dot_product(self, other):
        if self.columns != other.rows:
            return None
        result = Matrix(self.rows, other.columns)
        for i in range(self.rows):
            for j in range(other.columns):
                result.matrix[i][j] = sum([self.matrix[i][k] * other.matrix[k][j] for k in range(self.columns)])
        return result
    
    def randomize(self, min, max, type):
        for i in range(self.rows):
            for j in range(self.columns):
                if type == "int":
                    self.matrix[i][j] = random.randint(min, max)
                elif type == "double":
                    self.matrix[i][j] = random.uniform(min, max)
                else:
                    return None
    


