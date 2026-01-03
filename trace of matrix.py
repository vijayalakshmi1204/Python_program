matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

trace = 0
for i in range(len(matrix)):
    trace += matrix[i][i]

print("Trace of the matrix:", trace)
