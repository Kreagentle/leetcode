def rotate(matrix):
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for row in matrix:
        row.reverse()

    return matrix

if __name__ == '__main__':
    print(rotate([[1,2,3],[4,5,6],[7,8,9]]))