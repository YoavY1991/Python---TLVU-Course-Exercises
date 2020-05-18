def mul_mat_by_scalar(mat, alpha):
    mat_new = []
    for lst in mat:
        mat_new.append([])

    for i, m in enumerate(mat):
        for n in m:
            mat_new[i].append(n * alpha)

    return mat_new


print(mul_mat_by_scalar([[1, 2], [3, 4], [5, 6]], -1.5))
print(mul_mat_by_scalar([[1, 2], [3, 4.5], [5, 42]], 2))