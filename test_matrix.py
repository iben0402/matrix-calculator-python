from matrix import Matrix
import numpy as np
import pytest

def test_matrix_dotproduct():
    matrix1 = Matrix(2, 3)
    matrix1.matrix = [[1, 2, 3], [4, 5, 6]]
    matrix2 = Matrix(3, 2)
    matrix2.matrix = [[7, 8], [9, 10], [11, 12]]
    result = matrix1.dot_product(matrix2)
    assert result.matrix == [[58, 64], [139, 154]]

def test_matrix_dotproduct2():
    matrix1 = Matrix(2, 3)
    matrix1.matrix = [[1, 2, 3], [4, 5, 6]]
    matrix2 = Matrix(3, 2)
    matrix2.matrix = [[7, 8], [9, 10], [11, 12]]
    result = matrix2.dot_product(matrix1)
    assert result.matrix == [[39, 54, 69], [49, 68, 87], [59, 82, 105]]

def test_matrix_dotproduct3():
    matrix1 = Matrix(2, 2)
    matrix1.matrix = [[1, 2], [3, 4]]
    matrix2 = Matrix(3, 3)
    matrix2.matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    result = matrix1.dot_product(matrix2)
    assert result == None

def test_matrix_dotproduct4_big():
    matrix1 = Matrix(20, 30)
    matrix1.matrix = [[i + j for i in range(30)] for j in range(20)]
    matrix2 = Matrix(30, 20)
    matrix2.matrix = [[i + j for i in range(20)] for j in range(30)]
    result = matrix1.dot_product(matrix2)
    assert result.matrix == np.dot(matrix1.matrix, matrix2.matrix).tolist()
