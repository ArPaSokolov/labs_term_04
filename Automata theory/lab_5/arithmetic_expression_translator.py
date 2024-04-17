OPERATORS = {'+': (1, lambda x, y: x + y),
             '%': (2, lambda x, y: x % y),
             '/': (3, lambda x, y: x / y),
             '*': (3, lambda x, y: x * y)}


def eval_(formula):
    def parse(formula_string):
        number = ''
        for s in formula_string:
            if s in '1234567890.':
                number += s
            elif number:
                yield float(number)
                number = ''
            if s in OPERATORS or s in "()":
                yield s
        if number:
            yield float(number)

    def shunting_yard(parsed_formula):
        stack = []
        for token in parsed_formula:
            if token in OPERATORS:
                # Обработка операторов
                while stack and stack[-1] != "(" and OPERATORS[token][0] <= OPERATORS[stack[-1]][0]:
                    yield stack.pop()
                stack.append(token)
            elif token == ")":
                # Обработка закрывающей скобки
                while stack:
                    x = stack.pop()
                    if x == "(":
                        break
                    yield x
            elif token == "(":
                # Обработка открывающей скобки
                stack.append(token)
            else:
                # Обработка чисел и других символов
                yield token
        while stack:
            yield stack.pop()

    def calc(polish):
        stack = []
        for token in polish:
            if token in OPERATORS:
                # Вычисление операций
                y, x = stack.pop(), stack.pop()
                stack.append(OPERATORS[token][1](x, y))
            else:
                # Добавление чисел в стек
                stack.append(token)
        return stack[0]

    r = list(shunting_yard(parse(formula)))
    print("Выражение в обратной польской записи: ")
    print(' '.join(map(str, r)))
    print()
    print("Вычисленный результат: ")
    return calc(shunting_yard(parse(formula)))


print("Введите арифметическое выражение: ")
arithmetic_expression = input()

try:
    eval(arithmetic_expression)
    print(eval_(arithmetic_expression))
except SyntaxError:
    print("Ошибка!")