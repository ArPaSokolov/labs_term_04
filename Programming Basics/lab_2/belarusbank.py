from PyQt5.QtWidgets import QApplication, QWidget, QListWidgetItem
from PyQt5 import uic
import requests


class Belarusbank(QWidget):
    def __init__(self):
        super().__init__()
        self.children = []

        uic.loadUi("branches.ui", self)  # загрузка файла
        self.setWindowTitle("Branches")  # окно
        self.pushButton.clicked.connect(self.get_filials)  # нажали кнопку поиска
        self.filialsList.itemClicked.connect(self.get_filials_info)  # выбрали отделение в таблице

    def get_filials(self): # https://belarusbank.by/ru/33139/forDevelopers
        # получаем город из строки поиска
        city = self.cityInput.toPlainText()
        print("Поиск по городу:", city)

        #  отправляем запрос и получаем ответ
        requests_string = f"https://belarusbank.by/api/kursExchange?city={city}"
        print("Ожидание ответа...")
        response = requests.get(requests_string)

        # ответ
        if response:
            print("Ответ получен:", response.content)
            self.answer = response.json()
            self.filialsList.clear()  # очищаем список филиалов

            # заполняем список филиалов
            for i in range(len(self.answer)):
                filials = QListWidgetItem(f"{self.answer[i]['filials_text']}\n")
                self.filialsList.addItem(filials) # добавляем филиалы в табличку
        else:
            print("Ошибка")
            print("Код ответа:", response.status_code)
            print("Причина:", response.reason)

    def get_filials_info(self, clickedItem):
        row = self.filialsList.indexFromItem(clickedItem).row()
        filials_info = self.answer[row]

        # адрес
        street_type = filials_info.get('street_type', '-')
        street = filials_info.get('street', '-')
        home_number = filials_info.get('home_number', '-')
        self.adress_label.setText(f"Адрес:\n{street_type} {street}, {home_number}")

        # часы работы
        info_worktime = filials_info.get('info_worktime', '-').split("|")
        hours = ""

        for i in range(len(info_worktime) - 1):
            time = info_worktime[i].split()
            day = time[0]  # получаем день недели
            time_intervals = time[1:]  # получаем массив, где каждый элемент - пара чисел
            formatted_str = f"{day} "

            if len(time_intervals) >= 4:
                start_time_hour = time_intervals[0]
                start_time_minute = time_intervals[1]
                end_time_hour = time_intervals[2]
                end_time_minute = time_intervals[3]
                formatted_str += f"{start_time_hour}:{start_time_minute} - {end_time_hour}:{end_time_minute} "
                if len(time_intervals) == 8:  # если есть перерывы
                    break_start_time_hour = time_intervals[4]
                    break_start_time_minute = time_intervals[5]
                    break_end_time_hour = time_intervals[6]
                    break_end_time_minute = time_intervals[7]
                    formatted_str += f"(пер. {break_start_time_hour}:{break_start_time_minute} - {break_end_time_hour}:{break_end_time_minute})"
            else:
                formatted_str += " выходной"

            formatted_str = formatted_str.strip() + "\n"
            hours += formatted_str

        self.time_label.setText(f"Время работы:\n{hours}")

        # курс
        exchange_rate = ""

        for currency, values in self.answer[0].items():
            if currency.endswith("_in"):
                currency_name = currency[:-3]
                buy_rate = values
                sell_rate = self.answer[0].get(f"{currency_name}_out", "-")
                exchange_rate += f"{currency_name}\nПокупка: {buy_rate}\nПродажа: {sell_rate}\n\n"

        self.exchangeList.setText("Курсы валют:\n" + exchange_rate)


app = QApplication([])
ex = Belarusbank()
ex.show()
app.exec()
