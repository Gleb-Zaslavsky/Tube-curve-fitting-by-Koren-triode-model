# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 13:35:05 2023

@author: Chiffa
"""

import sys
from PyQt5.QtCore import Qt, QRect
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QRubberBand
from PyQt5.QtWidgets import QHBoxLayout, QSizeGrip
from PyQt5 import QtCore, QtGui, QtWidgets
from PIL import Image, ImageOps, ImageFilter
from PIL.ImageQt import ImageQt
from PIL.ImageQt import ImageQt
from  ImageStorage import ImageStorage
class CropImage(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(526, 478)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralWidget)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setText("")
        # fname = ImageStorage.fname
        # print(fname)
        # fname = 'image.png'
        # 
        # image  = Image.open(fname )   
        # image  = image.convert("RGBA")
        # qim = ImageQt(image)
        # self.pixmap =QtGui. QPixmap(QtGui.QImage(qim))
       
        self.pixmap = ImageStorage.crop_result
        self.label.setPixmap(self.pixmap)

        # self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 526, 25))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Crop image window"))
        self.pushButton.setText(_translate("MainWindow", "Crop"))


class Test_Resize(QMainWindow, CropImage):
    def __init__(self):
        super(Test_Resize, self).__init__()
        self.setupUi(self)
        self.show()

    # def run(self):
        self.pushButton.clicked.connect(self.cropImage)
        self.band = Resizable_rubber_band(self.label)
        self.band.move(50, 50)
        self.band.resize(200, 266)
        self.band.setMinimumSize(30, 30)

    def cropImage(self):
        rect = self.band.getCoverage()
        r = QRect(self.label.mapFromGlobal(rect.topLeft()), rect.size())
        px = self.label.pixmap()
        tr = QtGui.QTransform()
        tr.scale(px.size().width()*1.0/self.label.size().width(), px.size().height()*1.0/self.label.size().height())
        r = tr.mapRect(r)
        self.result = self.label.setPixmap(px.copy(r))
        self.band.hide()
        ImageStorage.crop_result = px.copy(r)
        print(ImageStorage.crop_result )
        return self.result

class Resizable_rubber_band(QWidget):
    def __init__(self, parent=None):
        super(Resizable_rubber_band, self).__init__(parent)
        # tell QSizeGrip to resize this widget instead of top-level window
        self.setWindowFlags(Qt.SubWindow)
        self.layout = QHBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.grip1 = QSizeGrip(self)
        self.grip2 = QSizeGrip(self)
        self.layout.addWidget(self.grip1, 0, Qt.AlignLeft | Qt.AlignTop)
        self.layout.addWidget(self.grip2, 0, Qt.AlignRight | Qt.AlignBottom)
        self.rubberband = QRubberBand(QRubberBand.Rectangle, self)
        self.rubberband.move(0, 0)
        self.rubberband.show()
        self.show()

    def resizeEvent(self, event):
        # force 4h x 3w aspect ratio using QSize
        # if width < height: height = 1.333 * width
        # if width > height: width = height / 1.333
        # width = self.width()
        # height = self.height()
        # if(width < height):
        #     height = int(width * 1.333)
        # else:
        #     width = int(height / 1.333)
        # self.rubberband.resize(QSize(width, height))
        self.rubberband.resize(self.size())

    def getCoverage(self):
        localCoords = self.contentsRect()
        print("localCoords: ", localCoords)
        TL = self.mapToGlobal(localCoords.topLeft())
        BR = localCoords.bottomRight()
        # TL+BR to get width & height
        widgetCoords = QRect(TL, TL+BR)
        print("widgetCoords: ", widgetCoords)
        return widgetCoords



if __name__ == "__main__":
    app = QApplication(sys.argv)
    program = Test_Resize()
    # program.run()
    sys.exit(app.exec_())