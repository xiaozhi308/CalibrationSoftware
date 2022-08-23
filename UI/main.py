#!/usr/bin/python３
"""主函数"""
from CalibrationSoftware.UI.maintext import Ui_mainWindow
from PyQt5 import QtWidgets
import sys


class UiMain(QtWidgets.QMainWindow, Ui_mainWindow):
    def __init__(self):
        super(UiMain, self).__init__()
        self.setupUi(self)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = UiMain()
    mainWindow.show()
    sys.exit(app.exec_())




