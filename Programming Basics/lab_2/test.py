import sys
import requests
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QListWidget, QListWidgetItem, QTextEdit


class BelarusBankApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("BelarusBank Branches")
        self.setGeometry(100, 100, 800, 700)

        self.city_label = QLabel("Enter city name:", self)
        self.city_label.move(50, 50)

        self.city_input = QLineEdit(self)
        self.city_input.move(150, 50)

        self.ok_button = QPushButton("OK", self)
        self.ok_button.move(250, 50)
        self.ok_button.clicked.connect(self.get_branches_info)

        self.result_label_main = QListWidget(self)
        self.result_label_main.setGeometry(10, 100, 200, 200)
        self.result_label_main.itemClicked.connect(self.update_label_text)

        self.label_adress = QLabel(self)
        self.label_adress.move(210, 100)
        self.label_adress.setFixedSize(200, 20)

        self.label_time = QLabel(self)
        self.label_time.move(210, 140)
        self.label_time.setFixedSize(250, 140)

        self.label_buy = QTextEdit(self)
        self.label_buy.move(450, 100)
        self.label_buy.resize(300, 550)

    def get_branches_info(self):
        city = self.city_input.text()
        url = f"https://belarusbank.by/api/kursExchange?city={city}"
        response = requests.get(url)
        if response.status_code == 200:
            self.answer = response.json()
            n = len(self.answer)
            self.result_label_main.clear()
            for i in range(n):
                if isinstance(self.answer[i], dict):
                    branch_info = QListWidgetItem(f"{self.answer[i]['filials_text']}\n")
                    self.result_label_main.addItem(branch_info)
                else:
                    self.result_label.setText("Error not dict")
        else:
            self.display_result("Error occurred while fetching data.")


    def update_label_text(self, clickedItem):
        row = self.result_label_main.indexFromItem(clickedItem).row()
        dictor = self.answer[row]
        self.label_adress.setText(f"Адрес: {dictor['street_type']} {dictor['street']}, {dictor['home_number']}")
        str_list = dictor['info_worktime'].split("|")
        str_list = str_list[:6]
        str = ''
        for i in range(len(str_list)-1):
            day, start_time_hour, start_time_minute, end_time_hour, end_time_minute, break_start_hour, break_start_minute, break_end_hour, break_end_minute = str_list[i].split()
            formatted_str = f"{day}: {start_time_hour}:{start_time_minute} - {end_time_hour}:{end_time_minute} (пер. {break_start_hour}:{break_start_minute} - {break_end_hour}:{break_end_minute})\n"
            str += formatted_str
        self.label_time.setText(f"Время работы:\n{str}")
        output_str = ""
        for currency, values in self.answer[0].items():
            if currency.endswith("_in"):
                currency_name = currency[:-3]
                buy_rate = values
                sell_rate = self.answer[0].get(f"{currency_name}_out", "N/A")
                output_str += f"{currency_name}\nПокупка: {buy_rate}\nПродажа: {sell_rate}\n\n"
        self.label_buy.setText(output_str)


app = QApplication(sys.argv)
window = BelarusBankApp()
window.show()
sys.exit(app.exec_())