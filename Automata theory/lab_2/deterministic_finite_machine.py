class DFA:
    def __init__(self, states, alphabet, transitions, start_state, accept_states):
        self.states = states
        self.alphabet = alphabet
        self.transitions = transitions
        self.start_state = start_state
        self.accept_states = accept_states

    def process_input(self, input_string):
        current_state = self.start_state

        for symbol in input_string:
            if symbol not in self.alphabet:
                print("Ошибка: Символ", symbol, "не входит в алфавит.")
                return

            if (current_state, symbol) not in self.transitions:
                print("Ошибка: Нет перехода из состояния", current_state, "по символу", symbol)
                return

            current_state = self.transitions[(current_state, symbol)]

        if current_state in self.accept_states:
            print("Входная строка принята.")
        else:
            print("Входная строка не принята.")


# Создание экземпляра детерминированного автомата
states = {'q0', 'q1', 'q2'}  # Множество состояний
alphabet = {'0', '1'}  # Множество символов алфавита
transitions = {('q0', '0'): 'q1', ('q0', '1'): 'q0', ('q1', '0'): 'q2', ('q1', '1'): 'q0', ('q2', '0'): 'q2', ('q2', '1'): 'q2'}  # Переходы
start_state = 'q0'  # Начальное состояние
accept_states = {'q2'}  # Множество принимающих состояний

dfa = DFA(states, alphabet, transitions, start_state, accept_states)

# Пример использования
dfa.process_input("0110")  # Входная строка принята
dfa.process_input("0011")  # Входная строка не принята
dfa.process_input("00001111")