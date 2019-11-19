M = [
    [9, 6, -20, 4, -5],
    [-5, 14, 6, 10, -3],
    [7, 4, -1, -3, -5],
    [-6, 2, -8, 11, 1],
    [4, -10, 7, -5, 2]
    ]


def pos(matrix):
    count = 0

    for i in range(len(matrix)):
        for j in range(len(matrix)):
            value = matrix[i][j]
            if i < j and value > 0:
                count += 1
    return count


print(pos(M))
