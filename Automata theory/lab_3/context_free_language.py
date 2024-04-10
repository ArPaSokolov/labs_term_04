import random

# Грамматика в виде словаря, где ключи - нетерминальные символы, значения - списки строк-правил
grammar = {
    'S': ['-N'],
    'N': ['B/A', 'ANB'],
    'A': ['1', '2'],
    'B': ['1', '2', '0']
}

def generate_string(start_symbol):
    string = ''
    if start_symbol not in grammar:
        return start_symbol
    else:
        production = random.choice(grammar[start_symbol])
        for symbol in production:
            string += generate_string(symbol)
    return string


for _ in range(5):
    random_string = generate_string('S')
    print(random_string)
