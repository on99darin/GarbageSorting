# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_distancetest.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog_lx(object):
    def setupUi(self, Dialog_lx):
        Dialog_lx.setObjectName("Dialog_lx")
        Dialog_lx.resize(1836, 1064)
        self.label = QtWidgets.QLabel(Dialog_lx)
        self.label.setGeometry(QtCore.QRect(820, 1020, 148, 45))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setLineWidth(6)
        self.label.setObjectName("label")
        self.distanceEdit = QtWidgets.QLineEdit(Dialog_lx)
        self.distanceEdit.setGeometry(QtCore.QRect(-10, 650, 921, 361))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.distanceEdit.setFont(font)
        self.distanceEdit.setObjectName("distanceEdit")
        self.getdata = QtWidgets.QPushButton(Dialog_lx)
        self.getdata.setGeometry(QtCore.QRect(610, 550, 241, 51))
        self.getdata.setObjectName("getdata")
        self.stop = QtWidgets.QPushButton(Dialog_lx)
        self.stop.setGeometry(QtCore.QRect(60, 550, 211, 51))
        self.stop.setObjectName("stop")
        self.wgt_player = QVideoWidget(Dialog_lx)
        self.wgt_player.setGeometry(QtCore.QRect(60, 40, 791, 451))
        self.wgt_player.setObjectName("wgt_player")
        self.listWidget = QtWidgets.QListWidget(Dialog_lx)
        self.listWidget.setGeometry(QtCore.QRect(910, 0, 921, 1011))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.listWidget.setFont(font)
        self.listWidget.setObjectName("listWidget")

        self.retranslateUi(Dialog_lx)
        QtCore.QMetaObject.connectSlotsByName(Dialog_lx)

    def retranslateUi(self, Dialog_lx):
        _translate = QtCore.QCoreApplication.translate
        Dialog_lx.setWindowTitle(_translate("Dialog_lx", "Dialog"))
        self.label.setText(_translate("Dialog_lx", "分类结果"))
        self.getdata.setText(_translate("Dialog_lx", "开始"))
        self.stop.setText(_translate("Dialog_lx", "停止"))

from PyQt5.QtMultimediaWidgets import QVideoWidget
