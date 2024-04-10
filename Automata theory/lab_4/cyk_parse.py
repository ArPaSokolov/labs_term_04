def cyk_parse(grammar, string):
    n = len(string)
    table = [[set() for _ in range(n+1)] for _ in range(n+1)]

    # Заполняем таблицу для подстрок длины 1
    for i in range(1, n+1):
        for rule in grammar:
            if string[i-1] in grammar[rule]:
                table[i][i].add(rule)

    # Заполняем таблицу для подстрок большей длины
    for length in range(2, n + 1):
        for i in range(1, n - length + 2):
            j = i + length - 1
            for k in range(i, j):
                for rule in grammar:
                    for r1 in table[i][k]:
                        for r2 in table[k + 1][j]:
                            if r1 + r2 in grammar[rule]:
                                table[i][j].add(rule)

    return table

def print_table(table):
    n = len(table) - 1
    max_cell_width = max(len(str(rule)) for row in table for rule in row)

    for row in range(1, n + 1):
        row_str = ''
        for col in range(row, n + 1):
            cell_str = ' '.join(sorted(table[row][col])) if table[row][col] else '-'
            cell_str = cell_str.ljust(max_cell_width)
            row_str += cell_str + ' | '

        print(row_str[:-3])  # Исключаем последний разделитель '|'


# Пример грамматики
grammar = {
    'S': {'FN'},
    'N': {'GC'},
    'G': {'BD'},
    'D': {'GC', 'BC'},
    'F': {'TA'},
    'T': {'+'},
    'A': {'a'},
    'B': {'b'},
    'C': {'c'}
}

# Пример строки
string = '+a' + 'b' * 4 + 'c' * 4

# Построение таблицы разбора
table = cyk_parse(grammar, string)

# Вывод таблицы разбора с выравниванием
print_table(table)
