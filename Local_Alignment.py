def localalign(v, w, matrix):    
    s = [[0 for x in range(len(v) + 1)] for y in range(len(w) + 1)]
    b = [[0 for x in range(len(v) + 1)] for y in range(len(w) + 1)]
    for i in range(1, len(w) + 1):
        for j in range(1, len(v) + 1):
            s[i][j] = max([s[i - 1][j] - 5, s[i][j - 1] - 5, s[i - 1][j - 1] + matrix[v[j - 1]][w[i - 1]], 0])
            if s[i][j] == s[i - 1][j] - 5:
                b[i][j] = 1
            elif s[i][j] == s[i][j - 1] - 5:
                b[i][j] = 2
            elif s[i][j] == s[i - 1][j - 1] + matrix[v[j - 1]][w[i - 1]]:
                b[i][j] = 3
            elif s[i][j] == 0:
                b[i][j] = 0

    cols = [[x[y] for x in s] for y in range(len(s[0]))]
    colmaxes = [max(x) for x in cols]
    rowmaxes = [max(x) for x in s]
    colmax = colmaxes.index(max(colmaxes))
    rowmax = rowmaxes.index(max(rowmaxes))

    return b, s[rowmax][colmax], colmax, rowmax

def backtrack(b, w, v, col, row):
    output1 = ''
    output2 = ''
    column = col
    row = row
    while b[row][column] != 0:
        if b[row][column] == 1:
            row = row - 1
            output1 = output1 + '-'
            output2 = output2 + v[row]
        elif b[row][column] == 2:
            column = column - 1
            output1 = output1 + w[column]
            output2 = output2 + '-'
        elif b[row][column] == 3:
            column = column - 1
            row = row - 1
            output1 = output1 + w[column]
            output2 = output2 + v[row]
    return output1[::-1], output2[::-1]

matrix = {}
with open('matrix.mtx') as file:
    header = file.readline().split()
    header = [x.strip() for x in header]
    lines = file.readlines()
    lines = [x.strip().split() for x in lines]
    for line in lines:
        matrix[line[0]] = dict(zip(header, list(map(int, line[1:]))))
        
with open('input.txt') as file:
    w = file.readline().strip()
    v = file.readline().strip()

b, score, col, row = localalign(w, v, matrix)
bt1, bt2 = backtrack(b, w, v, col, row)
print(score)
print(bt1)
print(bt2)
output = open('output.txt', 'w')
output.write('{}\n{}\n{}'.format(score, bt1, bt2))
output.close()