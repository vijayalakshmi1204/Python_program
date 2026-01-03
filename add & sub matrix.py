A = [[1, 2],
     [3, 4]]

B = [[5, 6],
     [7, 8]]

add = []
sub = []

for i in range(len(A)):
    add_row = []
    sub_row = []
    for j in range(len(A[0])):
        add_row.append(A[i][j] + B[i][j])
        sub_row.append(A[i][j] - B[i][j])
    add.append(add_row)
    sub.append(sub_row)

print("Addition:")
for row in add:
    print(row)

print("Subtraction:")
for row in sub:
    print(row)
