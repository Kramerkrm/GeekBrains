z = [[7, 4, 6, 7], [4, 5, 6, 5], [9, 0, 7, 3]]
x = [[2, 3, 2, 3], [4, 1, 1, 4], [8, 1, 8, 1]]


class Matrix:
    def __init__(self, list_1):
        self.list_1 = list_1

    def __str__(self):
        return '\n'.join(map(str, self.list_1))

    def __add__(self, another):
        matriz = []
        for i in range(len(self.list_1)):
            matriz.append([])
            for j in range(len(self.list_1[0])):
                    matriz[i].append(self.list_1[i][j] + another.list_1[i][j])
        return '\n'.join(map(str, matriz))


my_matrix = Matrix(z)
my_matrix_1 = Matrix(x)
print(f"*** Matrix 1 ***\n{my_matrix}")
print(f"*** Matrix 2 ***\n{my_matrix_1}")
print(f"*** Matrix 1 + Matrix 2 ***\n{my_matrix + my_matrix_1}")