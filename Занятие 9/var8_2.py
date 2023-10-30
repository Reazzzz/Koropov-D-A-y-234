def trans(matrix):
    new_matrix = []
    for i in range(len(matrix)):
        r = []
    for j in range(len(matrix[i])):
        r.append(matrix[j][i])
    new_matrix.append(r)
    return new_matrix

def print_matrix(matrix):
    for r in matrix:
        for element in r:
            print(element, end=" ")
            print()
matrix=[[1,2,3],[4,5,6],[7,8,9]]
trans= trans(matrix)
print_matrix(trans)
