class FiniteStateMachine:
    def __init__(self):
        self.states = set()  # Множество состояний
        self.alphabet = set()  # Множество входных символов
        self.transitions = {}  # Словарь для хранения переходов
        self.initial_state = None  # Начальное состояние
        self.accept_states = set()  # Множество принимающих состояний

    def add_transition(self, state, input_symbol, next_state):
        self.states.add(state)
        self.states.add(next_state)
        self.alphabet.add(input_symbol)
        key = (state, input_symbol)
        if key not in self.transitions:
            self.transitions[key] = set()
        self.transitions[key].add(next_state)

    def set_initial_state(self, state):
        self.initial_state = state

    def set_accept_state(self, state):
        self.accept_states.add(state)

    def process_input(self, input_string):
        current_states = {self.initial_state}  # Начинаем с начального состояния
        current_string = ""  # Строка в текущем состоянии
        print(f"{current_states}")
        for symbol in input_string:
            current_string += symbol
            next_states = set()  # Множество для хранения следующих состояний
            for state in current_states:
                key = (state, symbol)
                if key in self.transitions:
                    next_states.update(self.transitions[key])
            current_states = next_states
            print(f"{current_states} = {current_string}")  # Выводим текущее состояние
        return current_states.intersection(self.accept_states)


#-----------------------Задание 1------------------------#
# Детерминированный
nfa1 = FiniteStateMachine()

# Добавление состояний и переходов
nfa1.add_transition("S", "a", "A")
nfa1.add_transition("S", "b", "F")
nfa1.add_transition("A", "a", "B")
nfa1.add_transition("A", "b", "C")
nfa1.add_transition("B", "b", "B")
nfa1.add_transition("B", "c", "A")
nfa1.add_transition("C", "b", "A")
nfa1.add_transition("C", "a", "F")
nfa1.add_transition("A", "b", "C")


# Установка начального состояния и принимающих состояний
nfa1.set_initial_state("S")
nfa1.set_accept_state("F")

# Обработка входных сигналов
input_string = "abba"
print(f"Input #1: {input_string}")
accepted_states1 = nfa1.process_input(input_string)


if accepted_states1 == set():
    print(f"Автомат не принят")
else:
    print(f"Автомат принят")

#--------------------------------Задание 2----------------------------------#
# # Недетерминированный
nfa2 = FiniteStateMachine()

# Добавление состояний и переходов
nfa2.add_transition("1", "b", "1")
nfa2.add_transition("3", "a", "1")
nfa2.add_transition("2", "b", "3")
nfa2.add_transition("2", "b", "2")
nfa2.add_transition("2", "b", "0")
nfa2.add_transition("1", "b", "3")


# Установка начального состояния и принимающих состояний
nfa2.set_initial_state("1")
nfa2.set_accept_state("1")
nfa2.set_accept_state("0")

# Обработка входных сигналов
input_string = "ba"
print(f"\nInput #2: {input_string}")
accepted_states2 = nfa2.process_input(input_string)

if accepted_states2 == set():
    print(f"Автомат не принят")
else:
    print(f"Автомат принят")

#-----------------------------------Задание 2-------------------------------------------#
# Детерминированный
nfa3 = FiniteStateMachine()

# Добавление состояний и переходов
nfa3.add_transition("1", "b", "13")
nfa3.add_transition("13", "b", "13")
nfa3.add_transition("13", "a", "1")
nfa3.add_transition("0123", "b", "0123")
nfa3.add_transition("023", "a", "1")
nfa3.add_transition("023", "b", "023")

# Установка начального состояния и принимающих состояний
nfa3.set_initial_state("1")
nfa3.set_accept_state("1")
nfa3.set_accept_state("13")
nfa3.set_accept_state("023")
nfa3.set_accept_state("0123")

# Обработка входных сигналов
input_string = ""
print(f"\nInput #3: {input_string}")
accepted_states3 = nfa3.process_input(input_string)

if accepted_states3 == set():
    print(f"Автомат не принят")
else:
    print(f"Автомат принят")

#---------------------------------Задание 4---------------------------------#
nfa5 = FiniteStateMachine()

# Добавление состояний и переходов
nfa5.add_transition("p", "a", "q")
nfa5.add_transition("q", "a", "r")
nfa5.add_transition("r", "b", "r")
nfa5.add_transition("r", "a", "s")
nfa5.add_transition("p", "b", "s")
nfa5.add_transition("q", "a", "s")
nfa5.add_transition("s", "a", "q")


# Установка начального состояния и принимающих состояний
nfa5.set_initial_state("p")
nfa5.set_accept_state("r")
nfa5.set_accept_state("s")

# Обработка входных сигналов
input_string = "aaa"
print(f"\nInput #4: {input_string}")
accepted_states5 = nfa5.process_input(input_string)

if accepted_states5 == set():
    print(f"Автомат не принят")
else:
    print(f"Автомат принят")
#---------------------------------Задание 4---------------------------------#
nfa4 = FiniteStateMachine()

# Добавление состояний и переходов
nfa4.add_transition("q", "a", "r")
nfa4.add_transition("r", "a", "q")
nfa4.add_transition("q", "b", "r")
nfa4.add_transition("r", "b", "r")

# Установка начального состояния и принимающих состояний
nfa4.set_initial_state("q")
nfa4.set_accept_state("r")

# Обработка входных сигналов
input_string = "b"
print(f"\nInput #5: {input_string}")
accepted_states4 = nfa4.process_input(input_string)

if accepted_states4 == set():
    print(f"Автомат не принят")
else:
    print(f"Автомат принят")
