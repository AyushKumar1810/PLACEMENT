def celebrity(M, n):
    i = 0
    for j in range(1, n):
        if M[i][j] == 1:
            i = j
    for j in range(n):
        if i == j:
            continue
        if M[i][j] == 1 or M[j][i] == 0:
            return -1
    return i
M = [[0, 1, 0],
    [0, 0, 0],
    [1, 1, 0]]
n = 3
output = celebrity(M, n)
print("Celebrity index:", output)
