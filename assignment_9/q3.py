class Matrix:
        # Remember that instanes variables should be private (i.e., prepended with two underscores: __)
    def __init__(self, matrix):
        assert isinstance(matrix, list), "Input should be a list"
        assert all(isinstance(row, list) for row in matrix), "Each row should be a list"
        assert all(all(isinstance(val, (int, float)) for val in row) for row in matrix), "Values should be either integers or floats"
        assert len(matrix) >= 1, "There should be at least one non-empty row"
        assert all(len(row) == len(matrix[0]) for row in matrix), "All rows should have the same length"
        assert any(len(row) > 0 for row in matrix), "There should be at least one non-empty row"
        self.__matrix = matrix

    def __add__(self, other):
        assert isinstance(other, Matrix)
        assert self._get_shape() == other._get_shape(), "Matrices should have the same shape for addition"

        result = []
        for i in range(len(self.__matrix)):
            row = [a + b for a, b in zip(self.__matrix[i], other.__matrix[i])]
            result.append(row)
        return Matrix(result)

    def __mul__(self, other):
        assert isinstance(other, Matrix), "Can only multiply two Matrix instances"
        assert self._get_shape()[1] == other._get_shape()[0], "Number of columns in the first matrix should match the number of rows in the second matrix"

        result = []
        for i in range(len(self.__matrix)):
            row = []
            for j in range(len(other.__matrix[0])):
                val = sum(self.__matrix[i][k] * other.__matrix[k][j] for k in range(len(other.__matrix)))
                row.append(val)
            result.append(row)
        return Matrix(result)

    def __eq__(self, other):
        assert isinstance(other, Matrix)
        return self.__matrix == other.__matrix

    def __hash__(self):
        print(hash(tuple(tuple(row) for row in self.__matrix)))
        return hash(tuple(tuple(row) for row in self.__matrix))

    def _get_shape(self):
        return len(self.__matrix), len(self.__matrix[0])

if __name__=="__main__":
    a = Matrix(
        [[1, 2],
        [3, 4]])
    b = Matrix(
        [[1, 2], 
        [3, 4]])
    c = Matrix(
        [[2, 3], 
        [4, 5]])

    matrix_dict = {a: "A", b: "B", c: "C"}
    

