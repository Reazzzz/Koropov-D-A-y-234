def dig(matrix, k):
    diagonal = matrix[k-1][k-1]
    for i in range(len(matrix[k-1])):
        matrix[k-1][i] /= diagonal
    return matrix

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
k = 2
res = dig(matrix, k)
print(res)
