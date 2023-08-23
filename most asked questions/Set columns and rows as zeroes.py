def set_zeros(matrix):
    rows = set()
    cols = set()

    # Find positions of zero elements
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                rows.add(i)
                cols.add(j)
                # print(rows)
                # print(cols)

    # Set entire rows and columns to zero
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i in rows or j in cols:
                matrix[i][j] = 0

    return matrix

matrix = [
        [5,4,3,9],
        [2,0,7,6],
        [1,3,4,0],
        [9,8,3,4],
        [5,6,0,4]
        ]

result = set_zeros(matrix)
for row in result:
    print(row)