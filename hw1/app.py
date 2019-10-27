from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QAction
import os
import sys
from functools import partial

from problems.problem1 import Problem1

class MainUi(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainUi, self).__init__()
        ui_path = os.getcwd() + os.sep + "ui" + os.sep + "hw1.ui"
        uic.loadUi(ui_path, self)
        self.bind_buttons()

        menubar = self.menuBar()
        close_all = QAction('Close all CV windows', self)
        close_all.triggered.connect(Problem1.close_all)
        menubar.addAction(close_all)

        self.show()

    def bind_buttons(self):
        bind_dict = {
            'b1_1': Problem1.p1_1,
            'b1_2': Problem1.p1_2,
            'b1_3': Problem1.p1_3,
            'b1_4': Problem1.p1_4,
        }
        for object_name, bind_function in bind_dict.items():
            self.findChild(QtWidgets.QPushButton, object_name).clicked.connect(partial(bind_function, self))

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainUi()
    sys.exit(app.exec_())