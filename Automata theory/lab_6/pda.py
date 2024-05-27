class PDA:
    def __init__(self, states, alphabet, stack_alphabet, transitions, initial_state, initial_stack_symbol, final_states):
        self.states = states
        self.alphabet = alphabet
        self.stack_alphabet = stack_alphabet
        self.transitions = transitions
        self.initial_state = initial_state
        self.initial_stack_symbol = initial_stack_symbol
        self.final_states = final_states

    def process_input(self, input_string):
        current_state = self.initial_state
        stack = [self.initial_stack_symbol]

        for symbol in input_string:
            if symbol not in self.alphabet:
                print(stack, current_state)
                print(f"Строка не принадлежит языку (символ {symbol} не принадлежит алфавиту)")
                return

            if current_state not in self.transitions or symbol not in self.transitions[current_state]:
                print(stack, current_state)
                print(f"Строка не принадлежит языку (нет перехода из текущего состояния {current_state})")
                return

            transition = self.transitions[current_state][symbol]

            print(symbol)
            print(stack, current_state)

            if transition['pop'] != stack[-1]:
                if transition['pop'] != "":
                    print(stack, current_state)
                    print(f"Строка не принадлежит языку (символ {transition['pop']} в магазинной памяти не соответствует ожидаемому {stack[-1]})")
                    return
            if transition['pop'] != "":
                stack.pop()
            if transition['push'] != [""]:
                stack.extend(transition['push'])
            current_state = transition['state']

        if current_state not in self.final_states:
            while stack[-1] != "Z" and current_state in self.transitions:
                if "" in self.transitions[current_state]:
                    transition = self.transitions[current_state][""]
                    print(stack, current_state)
                    if transition['pop'] != stack[-1]:
                        if transition['pop'] != "":
                            print(stack, current_state)
                            print(f"Строка не принадлежит языку (символ {transition['pop']} в магазинной памяти не соответствует ожидаемому {stack[-1]})")
                            return
                    if transition['pop'] != "":
                        stack.pop()
                    if transition['push'] != [""]:
                        stack.extend(transition['push'])
                    current_state = transition['state']
                else:
                    break

        if current_state in self.final_states:
            print(stack, current_state)
            print("Строка принадлежит языку.")
        else:
            print(stack, current_state)
            print("Строка не принадлежит языку.")


# Создание автомата с магазинной памятью
states = {"1", "2"}  # Множество состояний
alphabet = {"a", "b", "c"}  # Алфавит входных символов
stack_alphabet = {"Z", "A", "T"}  # Алфавит символов магазинной памяти
transitions = {
    "1": {
        "a": {'pop': "", 'push': ["A"], 'state': "1"},
        "b": {'pop': "A", 'push': [""], 'state': "1"},
        "c": {'pop': "", 'push': ["T"], 'state': "2"}
    },
    "2": {
        "": {'pop': "T", 'push': [""], 'state': "1"},
    }
}  # Переходы
initial_state = "1"  # Начальное состояние
initial_stack_symbol = "Z"  # Начальный символ в магазинной памяти
final_states = {"1"}  # Множество конечных состояний

pda = PDA(states, alphabet, stack_alphabet, transitions, initial_state, initial_stack_symbol, final_states)

# Обработка входной строки
input_string = input("Введите строку: ")
pda.process_input(input_string)