import sys
import requests
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton


class BelarusBankApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("BelarusBank Branches")
        self.setGeometry(100, 100, 400, 300)

        self.city_label = QLabel("Enter city name:", self)
        self.city_label.move(50, 50)

        self.city_input = QLineEdit(self)
        self.city_input.move(150, 50)

        self.ok_button = QPushButton("OK", self)
        self.ok_button.move(150, 100)
        self.ok_button.clicked.connect(self.get_branches_info)

        self.result_label = QLabel(self)
        self.result_label.move(50, 150)

    def get_branches_info(self):
        city = self.city_input.text()
        url = f"https://belarusbank.by/api/kursExchange?city={city}"

        response = requests.get(url)
        if response.status_code == 200:
            branches_info = response.json()
            self.display_result(branches_info)
        else:
            self.display_result("Error occurred while fetching data.")

    def display_result(self, result):
        if isinstance(result, dict):
            branches = result.get("branches")
            if branches:
                info = "Branches:\n"
                for branch in branches:
                    branch_info = f"Branch {branch['number']}\n"
                    branch_info += f"Address: {branch['address']}\n"
                    branch_info += f"Working hours: {branch['workingHours']}\n"
                    branch_info += f"USD: Buy - {branch['USD_in']} / Sell - {branch['USD_out']}\n"
                    branch_info += f"EUR: Buy - {branch['EUR_in']} / Sell - {branch['EUR_out']}\n"
                    info += branch_info + "\n"
                self.result_label.setText(info)
            else:
                self.result_label.setText("No branches found.")
        else:
            self.result_label.setText(result)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BelarusBankApp()
    window.show()
    sys.exit(app.exec_())
