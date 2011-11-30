# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created: Tue Jan  4 21:11:49 2011
#      by: PyQt4 UI code generator 4.7.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(571, 289)
        self.groupBox = QtGui.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 321, 271))
        self.groupBox.setObjectName("groupBox")
        self.addSlideButton = QtGui.QPushButton(self.groupBox)
        self.addSlideButton.setGeometry(QtCore.QRect(0, 230, 111, 41))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/open.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addSlideButton.setIcon(icon)
        self.addSlideButton.setIconSize(QtCore.QSize(32, 32))
        self.addSlideButton.setObjectName("addSlideButton")
        self.listWidget = QtGui.QListWidget(self.groupBox)
        self.listWidget.setGeometry(QtCore.QRect(0, 20, 321, 192))
        self.listWidget.setAcceptDrops(True)
        self.listWidget.setDragEnabled(True)
        self.listWidget.setDragDropMode(QtGui.QAbstractItemView.InternalMove)
        self.listWidget.setAlternatingRowColors(True)
        self.listWidget.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.listWidget.setIconSize(QtCore.QSize(72, 72))
        self.listWidget.setObjectName("listWidget")
        self.deleteSlideButton = QtGui.QPushButton(self.groupBox)
        self.deleteSlideButton.setGeometry(QtCore.QRect(130, 230, 131, 41))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/exit.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.deleteSlideButton.setIcon(icon1)
        self.deleteSlideButton.setIconSize(QtCore.QSize(32, 32))
        self.deleteSlideButton.setObjectName("deleteSlideButton")
        self.groupBox_2 = QtGui.QGroupBox(Form)
        self.groupBox_2.setGeometry(QtCore.QRect(350, 10, 211, 211))
        self.groupBox_2.setFlat(False)
        self.groupBox_2.setObjectName("groupBox_2")
        self.slideSpinBox = QtGui.QSpinBox(self.groupBox_2)
        self.slideSpinBox.setGeometry(QtCore.QRect(140, 20, 61, 27))
        self.slideSpinBox.setMinimum(1)
        self.slideSpinBox.setMaximum(1000)
        self.slideSpinBox.setProperty("value", 300)
        self.slideSpinBox.setObjectName("slideSpinBox")
        self.label = QtGui.QLabel(self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(0, 30, 101, 20))
        self.label.setObjectName("label")
        self.label_2 = QtGui.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(0, 70, 131, 17))
        self.label_2.setObjectName("label_2")
        self.transitionSpinBox = QtGui.QDoubleSpinBox(self.groupBox_2)
        self.transitionSpinBox.setGeometry(QtCore.QRect(140, 60, 62, 27))
        self.transitionSpinBox.setMaximum(10.0)
        self.transitionSpinBox.setSingleStep(0.1)
        self.transitionSpinBox.setProperty("value", 1.5)
        self.transitionSpinBox.setObjectName("transitionSpinBox")
        self.saveButton = QtGui.QPushButton(Form)
        self.saveButton.setGeometry(QtCore.QRect(340, 240, 221, 41))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/save.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.saveButton.setIcon(icon2)
        self.saveButton.setIconSize(QtCore.QSize(32, 32))
        self.saveButton.setObjectName("saveButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "pySlideMaker v0.6", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("Form", "Slides", None, QtGui.QApplication.UnicodeUTF8))
        self.addSlideButton.setText(QtGui.QApplication.translate("Form", "Add Slide", None, QtGui.QApplication.UnicodeUTF8))
        self.deleteSlideButton.setText(QtGui.QApplication.translate("Form", "Delete Slide", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("Form", "Options", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "Slide duration", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Form", "Transition duration", None, QtGui.QApplication.UnicodeUTF8))
        self.saveButton.setText(QtGui.QApplication.translate("Form", "Save animated wallpaper", None, QtGui.QApplication.UnicodeUTF8))

