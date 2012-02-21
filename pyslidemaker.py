#!/usr/bin/python -tt

__author__ = "Diego Navarro"
__email__ = "dnmellen@gmail.com"
__version__ = 0.6


import sys
import os
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import *
from PIL import Image
from gui import Ui_Form
from xmlgenerator import XmlGenerator

class MyForm(QtGui.QMainWindow):

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # Signals/Slots
        QtCore.QObject.connect(self.ui.addSlideButton, QtCore.SIGNAL("clicked()"), self.addSlide)
        QtCore.QObject.connect(self.ui.deleteSlideButton, QtCore.SIGNAL("clicked()"), self.deleteSlide)
        QtCore.QObject.connect(self.ui.saveButton, QtCore.SIGNAL("clicked()"), self.save)


    def _addFileToList(self,filename):
        if (not filename.isEmpty()):
            item = QListWidgetItem(os.path.basename(unicode(filename)))
            picture = QtGui.QImage()
            picture.load(filename)
            picture.scaled(72,72)
            icon = QIcon(QPixmap.fromImage(picture))
            item.setStatusTip(filename)
            item.setIcon(icon) 
            self.ui.listWidget.addItem(item)


    def addSlide(self):
        files = QtGui.QFileDialog.getOpenFileNames(self, 'Add slide',os.path.expanduser("~"),"Image Files (*.png *.jpg *.bmp)")
        for filename in files:
            self._addFileToList(filename)

    def deleteSlide(self):
        self.ui.listWidget.takeItem(self.ui.listWidget.currentRow())

    def save(self):
        filename = QtGui.QFileDialog.getSaveFileName(self, 'Save background','background.xml', 'XML file (*.xml)')

        if not filename:
            return -1

        # Generate animated background
        listOfSlides = []
        for i in range(self.ui.listWidget.count()):
            listOfSlides.append(unicode(self.ui.listWidget.item(i).statusTip()))

        xml_handler = XmlGenerator(listOfSlides,self.ui.slideSpinBox.value(),self.ui.transitionSpinBox.value())
        xml_handler.save_to(unicode(filename))

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())   
