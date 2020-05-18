def max_mat_square(mat):
    # Returns the largest sum of 2x2 square in a given matrix (m)
    rows = (len(mat[0]))
    colums = len(mat)
    squares = []
    multiples = []
    f = 0
    for i, c in enumerate(mat[:-1]):
        for y, n in enumerate(c[:-1]):
            squares.append([])
            squares[f].append(n)
            squares[f].append(c[y + 1])
            squares[f].append(mat[i + 1][y])
            squares[f].append(mat[i + 1][y + 1])
            f += 1

    for s in squares:
        m = 0
        for x in s:
            m += x
        multiples.append(m)

    return max(multiples)


print(max_mat_square([[1, 2.5, 3], [4, -4, 6], [0.5, -1, 5]]))
print(max_mat_square([[1, 2], [3, 4], [5, 6]]))