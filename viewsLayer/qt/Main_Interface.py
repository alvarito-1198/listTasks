# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Main_UI.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QStatusBar, QTableWidget, QTableWidgetItem,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(705, 537)
        MainWindow.setMinimumSize(QSize(400, 400))
        palette = QPalette()
        brush = QBrush(QColor(5, 4, 4, 255))
        brush.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush)
        brush1 = QBrush(QColor(0, 0, 0, 153))
        brush1.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush1)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush1)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush1)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush1)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush1)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush1)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush1)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush1)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush1)
        MainWindow.setPalette(palette)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"background-color: rgba(0, 0, 0, .6);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.btnAdd = QPushButton(self.centralwidget)
        self.btnAdd.setObjectName(u"btnAdd")
        self.btnAdd.setGeometry(QRect(440, 20, 121, 31))
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(18)
        self.btnAdd.setFont(font)
        self.btnAdd.setAutoFillBackground(False)
        self.btnAdd.setStyleSheet(u"\n"
":enabled { \n"
"color: white;\n"
"background: #9b9b9b\n"
"}\n"
"\n"
":disabled {\n"
"background: #7c7c7c\n"
"}")
        self.tableList = QTableWidget(self.centralwidget)
        if (self.tableList.columnCount() < 3):
            self.tableList.setColumnCount(3)
        brush2 = QBrush(QColor(255, 255, 255, 255))
        brush2.setStyle(Qt.BrushStyle.SolidPattern)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font);
        __qtablewidgetitem.setBackground(QColor(0, 0, 0));
        __qtablewidgetitem.setForeground(brush2);
        self.tableList.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font);
        __qtablewidgetitem1.setBackground(QColor(0, 0, 0));
        __qtablewidgetitem1.setForeground(brush2);
        self.tableList.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        brush3 = QBrush(QColor(255, 255, 255, 255))
        brush3.setStyle(Qt.BrushStyle.Dense1Pattern)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font);
        __qtablewidgetitem2.setBackground(QColor(0, 0, 0));
        __qtablewidgetitem2.setForeground(brush3);
        self.tableList.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.tableList.setObjectName(u"tableList")
        self.tableList.setEnabled(True)
        self.tableList.setGeometry(QRect(120, 100, 441, 291))
        self.tableList.setFont(font)
        self.tableList.setMouseTracking(True)
        self.tableList.setTabletTracking(True)
        self.tableList.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.tableList.setAutoFillBackground(True)
        self.tableList.setStyleSheet(u"color: black;\n"
"background: white;\n"
"selection-background-color: rgba(79, 80, 90, 0.9)")
        self.tableList.setTabKeyNavigation(False)
        self.tableList.setProperty(u"showDropIndicator", False)
        self.tableList.setDragDropOverwriteMode(False)
        self.tableList.setAlternatingRowColors(False)
        self.tableList.setSelectionMode(QAbstractItemView.SelectionMode.ExtendedSelection)
        self.tableList.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableList.setShowGrid(False)
        self.tableList.setGridStyle(Qt.PenStyle.SolidLine)
        self.tableList.setSortingEnabled(True)
        self.tableList.setWordWrap(False)
        self.tableList.setColumnCount(3)
        self.tableList.horizontalHeader().setCascadingSectionResizes(True)
        self.tableList.horizontalHeader().setMinimumSectionSize(30)
        self.tableList.horizontalHeader().setHighlightSections(True)
        self.tableList.horizontalHeader().setStretchLastSection(True)
        self.tableList.verticalHeader().setMinimumSectionSize(30)
        self.Label = QLabel(self.centralwidget)
        self.Label.setObjectName(u"Label")
        self.Label.setGeometry(QRect(120, 30, 111, 21))
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(18)
        font1.setBold(True)
        self.Label.setFont(font1)
        self.Label.setStyleSheet(u"color: white")
        self.Label.setTextFormat(Qt.TextFormat.AutoText)
        self.description = QLineEdit(self.centralwidget)
        self.description.setObjectName(u"description")
        self.description.setGeometry(QRect(240, 20, 191, 31))
        self.description.setFont(font)
        self.description.setStyleSheet(u"color: white")
        self.cmbState = QComboBox(self.centralwidget)
        self.cmbState.addItem("")
        self.cmbState.addItem("")
        self.cmbState.addItem("")
        self.cmbState.setObjectName(u"cmbState")
        self.cmbState.setGeometry(QRect(240, 60, 181, 31))
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(14)
        self.cmbState.setFont(font2)
        self.cmbState.setAutoFillBackground(False)
        self.cmbState.setStyleSheet(u"color: white;\n"
"border-color: white solid 2px")
        self.btnUpdate = QPushButton(self.centralwidget)
        self.btnUpdate.setObjectName(u"btnUpdate")
        self.btnUpdate.setGeometry(QRect(440, 60, 121, 31))
        self.btnUpdate.setFont(font)
        self.btnUpdate.setStyleSheet(u"\n"
":enabled { \n"
"color: white;\n"
"background: #9b9b9b\n"
"}\n"
"\n"
":disabled {\n"
"background: #7c7c7c\n"
"}")
        self.btnDelete = QPushButton(self.centralwidget)
        self.btnDelete.setObjectName(u"btnDelete")
        self.btnDelete.setGeometry(QRect(120, 400, 441, 31))
        self.btnDelete.setFont(font)
        self.btnDelete.setStyleSheet(u"\n"
":enabled { \n"
"color: white;\n"
"background: #9b9b9b\n"
"}\n"
"\n"
":disabled {\n"
"background: #7c7c7c\n"
"}")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"List Tasks 2025", None))
        self.btnAdd.setText(QCoreApplication.translate("MainWindow", u"Agregar", None))
        ___qtablewidgetitem = self.tableList.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"id", None));
        ___qtablewidgetitem1 = self.tableList.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"descricion", None));
        ___qtablewidgetitem2 = self.tableList.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"state", None));
        self.Label.setText(QCoreApplication.translate("MainWindow", u"Descripcion", None))
        self.cmbState.setItemText(0, QCoreApplication.translate("MainWindow", u"PENDIENTE", None))
        self.cmbState.setItemText(1, QCoreApplication.translate("MainWindow", u"EN_PROCESO", None))
        self.cmbState.setItemText(2, QCoreApplication.translate("MainWindow", u"TERMINADO", None))

        self.btnUpdate.setText(QCoreApplication.translate("MainWindow", u"Actualizar", None))
        self.btnDelete.setText(QCoreApplication.translate("MainWindow", u"Eliminar", None))
    # retranslateUi

