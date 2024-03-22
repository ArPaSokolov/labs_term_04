from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel


class Form(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("db_table_view.ui", self)
        self.pushButton.clicked.connect(self.press)

    def press(self):
        db = QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName("films_db.sqlite")
        db.open()

        model = QSqlTableModel(self, db)
        model.setTable("films")
        model.select()

        self.tableView.setModel(model)


app = QApplication([])
window = Form()
window.show()
app.exec()
