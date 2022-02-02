import sqlite3
import sys

from PyQt5 import QtWidgets
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.wr()

    def wr(self):
        self.con = sqlite3.connect('coffee.db')
        cursor = self.con.cursor()
        res = cursor.execute(f"""SELECT * FROM info_about_coffee
                             ORDER BY ID""").fetchall()

        self.tableWidget.setRowCount(len(res))
        self.tableWidget.setColumnCount(len(res[0]))

        for i, k in enumerate(res):
            for j, g in enumerate(k):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(g)))

        self.tableWidget.setHorizontalHeaderLabels(['ID', 'Название сорта', 'Степень обжарки', 'Молотый/В зёрнах',
                                                    'Описание вкуса', 'Цена', 'Объём упаковки'])
        self.tableWidget.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)

        for i in range(1, 7):
            self.tableWidget.horizontalHeader().setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeToContents)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())