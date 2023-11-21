import io
import sqlite3
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidgetItem


class Espresso(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.bd = None
        self.cursor = None
        self.load_table()

    def load_table(self):
        self.bd = sqlite3.connect('coffee.sqlite')
        self.cursor = self.bd.cursor()
        mass = self.cursor.execute("SELECT * FROM coffees").fetchall()
        title = ['ID', 'название сорта', 'степень обжарки', 'молотый/в зернах', 'описание вкуса', 'цена',
                 'объем упаковки']
        self.tableWidget.setColumnCount(len(title))
        self.tableWidget.setHorizontalHeaderLabels(title)
        self.tableWidget.setRowCount(0)
        for i, row in enumerate(mass):
            self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(elem)))
        self.tableWidget.resizeColumnsToContents()
        self.bd.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Espresso()
    w.show()
    sys.exit(app.exec())