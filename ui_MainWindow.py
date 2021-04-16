# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFrame


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(30, 30, 281, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.openFilePushButton = QtWidgets.QPushButton(self.centralwidget)
        self.openFilePushButton.setGeometry(QtCore.QRect(330, 30, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.openFilePushButton.setFont(font)
        self.openFilePushButton.setObjectName("openFilePushButton")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(30, 80, 150, 400))
        self.textEdit.setObjectName("textEdit2")
        self.textEdit2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit2.setGeometry(QtCore.QRect(200, 80, 150, 400))
        self.textEdit2.setObjectName("textEdit2")
        self.countsLcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.countsLcdNumber.setGeometry(QtCore.QRect(630, 10, 160, 41))
        self.countsLcdNumber.setStyleSheet('background-color:#cbf7ff')
        self.countsLcdNumber.setLineWidth(2)
        self.countsLcdNumber.setFrameShape(QFrame.Box)
        self.countsLcdNumber.setFrameShadow(QFrame.Plain)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.countsLcdNumber.setFont(font)
        self.countsLcdNumber.setObjectName("countsLcdNumber")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(540, 30, 75, 12))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.awbLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.awbLineEdit.setGeometry(QtCore.QRect(480, 90, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.awbLineEdit.setFont(font)
        self.awbLineEdit.setObjectName("awbLineEdit")
        self.TimeIntervalLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.TimeIntervalLineEdit.setGeometry(QtCore.QRect(560, 150, 113, 31))
        self.TimeIntervalLineEdit.setText('300')
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.TimeIntervalLineEdit.setFont(font)
        self.TimeIntervalLineEdit.setObjectName("TimeIntervalLineEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(400, 100, 41, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(400, 160, 101, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.awbHandleNameLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.awbHandleNameLineEdit.setGeometry(QtCore.QRect(560, 210, 113, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.awbHandleNameLineEdit.setFont(font)
        self.awbHandleNameLineEdit.setObjectName("awbHandleNameLineEdit")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(400, 220, 151, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.awbHandleLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.awbHandleLineEdit.setGeometry(QtCore.QRect(560, 270, 113, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.awbHandleLineEdit.setFont(font)
        self.awbHandleLineEdit.setText("")
        self.awbHandleLineEdit.setObjectName("awbHandleLineEdit")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(400, 280, 101, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.getHandlePushButton = QtWidgets.QPushButton(self.centralwidget)
        self.getHandlePushButton.setGeometry(QtCore.QRect(680, 280, 91, 23))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.getHandlePushButton.setFont(font)
        self.getHandlePushButton.setObjectName("getHandlePushButton")
        self.startPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.startPushButton.setGeometry(QtCore.QRect(400, 320, 75, 23))
        self.startPushButton.setCheckable(True)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.startPushButton.setFont(font)
        self.startPushButton.setObjectName("startPushButton")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(680, 160, 31, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.openFilePushButton.setText(_translate("MainWindow", "openFile"))
        self.label.setText(_translate("MainWindow", "COUNTS"))
        self.label_2.setText(_translate("MainWindow", "AWB"))
        self.label_3.setText(_translate("MainWindow", "Time Interval"))
        self.label_4.setText(_translate("MainWindow", "AWB Handle Name"))
        self.label_5.setText(_translate("MainWindow", "AWB Handle"))
        self.getHandlePushButton.setText(_translate("MainWindow", "getHandle"))
        self.startPushButton.setText(_translate("MainWindow", "START"))
        self.label_6.setText(_translate("MainWindow", "ms"))
