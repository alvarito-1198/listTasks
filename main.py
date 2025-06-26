from PyQt6 import QtWidgets

from viewsLayer.qt.Main_Interface import Ui_MainWindow
from viewsLayer.Menu_view import Menu
from helpers.Loggin_configuration import loggin_run
import sys

def iniciar_menu_consola():
    loggin_run(1,"inicio del sistema")
    menu = Menu()
    menu.show_menu()




if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w_DemoForm = QtWidgets.QWidget()
    ui = Ui_MainWindow()
    ui.setupUi(w_DemoForm)
    w_DemoForm.show()
    sys.exit(app.exec())

