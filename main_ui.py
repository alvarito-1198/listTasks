from PySide6 import QtWidgets as qtw

from controllerslayer.TaskController import TaskController
from helpers.Enum_state import Enum_state
from viewsLayer.qt.Main_Interface import Ui_MainWindow

from PySide6.QtWidgets import (QTableWidgetItem)

class MainUi(qtw.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.selected_data = None
        self.controller = TaskController()
        self.setupUi(self)

        self.list_tasks()

        self.btnAdd.setEnabled(False)
        self.btnUpdate.setEnabled(False)
        self.btnDelete.setEnabled(False)

        self.tableList.clicked.connect(self.delete_button_state)
        self.tableList.clicked.connect(self.update_button_state)

        self.description.textChanged.connect(self.add_button_state)

        self.btnAdd.clicked.connect(self.add_task)
        self.btnDelete.clicked.connect(self.delete_task)
        self.btnUpdate.clicked.connect(self.update_task)


        self.show()

    def add_button_state(self, text):
        if text:
            self.btnAdd.setEnabled(True)
        else:
            self.btnAdd.setEnabled(False)

    def delete_button_state(self):
        if self.on_row_selected():
            self.btnDelete.setEnabled(True)
        else:
            self.btnDelete.setEnabled(False)

    def update_button_state(self, text):
        if text:
            self.btnUpdate.setEnabled(True)
        else:
            self.btnUpdate.setEnabled(False)

    def list_tasks(self):
        tasks = self.controller.list_tasks()

        self.tableList.setRowCount(len(tasks))
        table_row = 0
        for i in tasks:
            self.tableList.setItem(table_row, 0, QTableWidgetItem(str(i.id)))
            self.tableList.setItem(table_row, 1, QTableWidgetItem(i.description))
            self.tableList.setItem(table_row, 2, QTableWidgetItem(Enum_state(i.state).name))

            table_row += 1

    def add_task(self):
        add = self.controller.add_task(self.description.text())
        if add:
            self.list_tasks()

    def update_task(self):
        selected_item = self.selected_data
        selected_item['description'] = self.description.text()

        selected_item['state'] = Enum_state[self.cmbState.currentText()].value

        if selected_item:
            update = self.controller.update_task(selected_item)
            if update:
                self.description.setText("")
                self.cmbState.setCurrentText(Enum_state.PENDIENTE.name)
                self.tableList.selectionModel().clearSelection()
                self.btnUpdate.setEnabled(False)
                self.btnDelete.setEnabled(False)
                self.list_tasks()

    def delete_task(self):
        selected_item = self.on_row_selected()
        if selected_item:
            delete = self.controller.delete_task_logical(selected_item['id'])
            if delete:
                self.tableList.selectionModel().clearSelection()
                self.description.setText("")
                self.cmbState.setCurrentText(Enum_state.PENDIENTE.name)
                self.btnDelete.setEnabled(False)
                self.btnUpdate.setEnabled(False)
                self.list_tasks()

    def on_row_selected(self):
        selected_index = self.tableList.selectionModel().selectedIndexes()

        if selected_index:
            row = {'id': selected_index[0].data(), 'description': selected_index[1].data(),
                   'state': selected_index[2].data()}
            self.description.setText(row['description'])
            self.cmbState.setCurrentText(row['state'])
            self.selected_data = row
            return row
        else:
            return None


# if __name__ == '__main__':
#     app = qtw.QApplication([])
#
#     form = MainUi()
#
#     form.show()
#
#     sys.exit(app.exec_())


# if __name__ == '__main__':
#     app = QApplication([])
#     window = QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(window)
#     window.show()
#     app.exec()

if __name__ == '__main__':
    app = qtw.QApplication([])
    window = MainUi()
    app.exec()