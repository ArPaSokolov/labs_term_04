class Watchdog:
    def __init__(self):
        self.current_state = "Покой"

    def process_input(self, action):
        if self.current_state == "Покой":
            if action == "Приблизиться":
                print("Вы приблизились к сторожевому псу в состоянии покоя")
                self.current_state = "Злится"
                print("Пес в состоянии:", self.current_state)

        elif self.current_state == "Злится":
            if action == "Приблизиться":
                print("Вы приблизились к сторожевому псу в состоянии злости")
                self.current_state = "Лай"
                print("Пес в состоянии:", self.current_state)
            elif action == "Отойти":
                print("Вы отошли от сторожевого пса в состоянии злости")
                self.current_state = "Покой"
                print("Пес в состоянии:", self.current_state)

        elif self.current_state == "Лай":
            if action == "Отойти":
                print("Вы отошли от сторожевого пса в состоянии лай")
                self.current_state = "Злится"
                print("Пес в состоянии:", self.current_state)


# Создание экземпляра конечного автомата
fsm = Watchdog()
action = "Старт"

# Пример использования
while action != "Конец":
    action = input("Ваше действие - Приблизиться или Отойти? ")
    fsm.process_input(action)