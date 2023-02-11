import sys

from PyQt5.QtWidgets import QApplication

from controllers.mainwindow_ctrl import Cocomo2Mainwindow


def main():
    app = QApplication(sys.argv)
    window = Cocomo2Mainwindow()
    window.show()
    app.exec()


if __name__ == '__main__':
    main()
