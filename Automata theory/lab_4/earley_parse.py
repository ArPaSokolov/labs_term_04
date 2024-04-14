class EarleyItem:
    def __init__(self, rule, dot, start, end):
        self.rule = rule
        self.dot = dot
        self.start = start
        self.end = end


def earley_parse(grammar, string):
    n = len(string)
    chart = [[] for _ in range(n + 1)]

    # Инициализируем начальное состояние
    start_rule = list(grammar.keys())[0]
    start_item = EarleyItem(start_rule, 0, 0, 0)
    chart[0].append(start_item)

    for i in range(n + 1):
        added = True
        while added:
            added = False
            for item in chart[i]:
                if item.dot < len(item.rule):
                    next_symbol = item.rule[item.dot]
                    if next_symbol in grammar:
                        # Прогнозирование
                        predict(grammar, next_symbol, i, chart)
                    else:
                        # Сканирование
                        scan(item, next_symbol, i, chart, string)
                else:
                    # Завершение элемента
                    complete(item, i, chart)
                    added = True

    return chart


def predict(grammar, symbol, position, chart):
    for rule in grammar[symbol]:
        item = EarleyItem(rule, 0, position, position)
        if item not in chart[position]:
            chart[position].append(item)


def scan(item, symbol, position, chart, string):
    if position < len(string) and symbol == string[position]:
        new_item = EarleyItem(item.rule, item.dot + 1, item.start, position + 1)
        if new_item not in chart[position + 1]:
            chart[position + 1].append(new_item)


def complete(item, position, chart):
    for prev_item in chart[item.start]:
        if prev_item.dot < len(prev_item.rule) and prev_item.rule[prev_item.dot] == item.rule[0]:
            new_item = EarleyItem(prev_item.rule, prev_item.dot + 1, prev_item.start, position)
            if new_item not in chart[position]:
                chart[position].append(new_item)


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
string = ['+abbbbcccc']

# Разбор методом Эрли
chart = earley_parse(grammar, string)

# Вывод разбора
for i, items in enumerate(chart):
    print(f'Chart[{i}]:')
    for item in items:
        print(f'{item.rule: <10} ({item.dot}) [{item.start}:{item.end}]')
    print()