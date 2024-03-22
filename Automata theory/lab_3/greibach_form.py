import random

# Грамматика в виде словаря, где ключи - нетерминальные символы, значения - списки строк-правил
grammar = {
    'A1': ['-A3'],
    'A3': ['1A6A5', '2A6A5', '0A6A5', '1A3A5', '2A3A5'],
    'A8': ['1', '2'],
    'A6': ['/'],
    'A5': ['1', '2', '0']
}


def generate_string(start_symbol):
    string = ''

    if start_symbol not in grammar:
        return start_symbol

    production = random.choice(grammar[start_symbol])
    i = 0
    while i < len(production):
        symbol = production[i]
        if i + 1 < len(production):
            next_symbol = production[i + 1]
            if symbol + next_symbol in grammar:
                string += generate_string(symbol + next_symbol)
                i += 2
                continue
        if symbol in grammar:
            string += generate_string(symbol)
        else:
            string += symbol
        i += 1

    return string


for _ in range(10):
    random_string = generate_string('A1')
    print(random_string)
