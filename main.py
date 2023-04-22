from pprint import pprint

first_code = input()
second_code = input()
row = [-1] * (len(first_code) + 1)
matrix = []
for i in range(len(second_code) + 1):
    matrix.append(row.copy())

for y in range(len(second_code) + 1):
    for x in range(len(first_code) + 1):
        if y == 0:
            h = x
            v = 1000000
            d = 1000000
        elif x == 0:
            h = 1000000
            v = y
            d = 1000000
        else:
            h = matrix[y][x - 1] + 1
            v = matrix[y - 1][x] + 1
            d = matrix[y - 1][x - 1]
            if second_code[y - 1] != first_code[x - 1]:
                d += 1
        mins = min(h, v, d)
        matrix[y][x] = mins

x, y = len(first_code), len(second_code)
code1 = ''
code2 = ''
while x != 0 and y != 0:
    h = matrix[y][x - 1]
    v = matrix[y - 1][x]
    d = matrix[y - 1][x - 1]
    mins = min(h, v, d)
    if h == mins:
        code2 += '_'
        code1 += first_code[x - 1]
        x -= 1
    elif v == mins:
        code1 += '_'
        code2 += second_code[y - 1]
        y -= 1
    else:
        if mins != matrix[y][x]:
            code2 += second_code[y - 1].lower()
            code1 += first_code[x - 1].lower()
        else:
            code2 += second_code[y - 1]
            code1 += first_code[x - 1]
        x -= 1
        y -= 1
code1 = code1[::-1]
code2 = code2[::-1]

pprint(matrix)
print(matrix[len(second_code)][len(first_code)])
print(code1)
print(code2)