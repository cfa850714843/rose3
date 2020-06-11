# coding: utf-8
import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from .DockerMe import Ui_DockerMe


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    ui = Ui_DockerMe()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())




