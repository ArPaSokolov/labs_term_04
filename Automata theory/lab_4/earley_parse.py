def earley_parse(grammar, input_string):
    chart = [[] for _ in range(len(input_string) + 1)]
    start_rule = ('S', ('+', 'a', 'N'), 0, 0)
    chart[0].append(start_rule)

    for i in range(len(chart)):
        for item in chart[i]:
            symbol_after_dot = get_symbol_after_dot(item)

            if symbol_after_dot is not None and symbol_after_dot in grammar:
                # Predict
                for production in grammar[symbol_after_dot]:
                    new_item = (symbol_after_dot, production, 0, i)
                    if new_item not in chart[i]:
                        chart[i].append(new_item)

            elif symbol_after_dot is not None:
                # Scan
                if i < len(input_string) and symbol_after_dot == input_string[i]:
                    new_item = (item[0], item[1], item[2] + 1, item[3])
                    if new_item not in chart[i + 1]:
                        chart[i + 1].append(new_item)

            else:
                # Complete
                for prev_item in chart[item[3]]:
                    if prev_item[2] < len(prev_item[1]) and prev_item[1][prev_item[2]] == item[0]:
                        new_item = (prev_item[0], prev_item[1], prev_item[2] + 1, prev_item[3])
                        if new_item not in chart[i]:
                            chart[i].append(new_item)

    return chart


def get_symbol_after_dot(item):
    if item[2] < len(item[1]):
        return item[1][item[2]]
    else:
        return None


# Пример использования:
grammar = {
    'S': {('+', 'a', 'N')},
    'N': {('b', 'D', 'c')},
    'D': {('b', 'D', 'c'), ('b', 'c')}
}

input_string = '+a' + 'b' * 4 + 'c'
chart = earley_parse(grammar, input_string)

# Вывод таблицы разбора по столбцам
for i, column in enumerate(chart):
    if column:
        if i > 0:
            print(f"======= {input_string[i - 1]} =======")  # Вывод символа из входной строки
        print()
        for j, item in enumerate(column):
            production = ' '.join(item[1])
            dot_position = item[2]
            rule = f"{item[0]} -> {' '.join(item[1][:dot_position])} • {' '.join(item[1][dot_position:])}"
            print(f"{rule}, {item[3]}")  # Вывод правила и номера шага
        print()
