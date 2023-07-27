def print_pattern(rows):
    for i in range(rows, 0, -1):
        line = ''.join(str(j) for j in range(1, i + 1))
        line += ' ' * (2 * (rows - i))
        line += ''.join(str(j) for j in range(i, 0, -1))
        print(line)

    for i in range(2, rows + 1):
        line = ''.join(str(j) for j in range(1, i + 1))
        line += ' ' * (2 * (rows - i))
        line += ''.join(str(j) for j in range(i, 0, -1))
        print(line)

rows = 5  # Change this to the desired number of rows
print_pattern(rows)
