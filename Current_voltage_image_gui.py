# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tube_gui.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!
import numpy as  np
import pandas as pd
import json
import os.path

from PyQt5 import QtCore, QtGui, QtWidgets


from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox, QToolBar,  QRubberBand, QHBoxLayout, QWidget
from  PyQt5.QtCore import QRect
from PIL import Image, ImageOps, ImageFilter
from PIL.ImageQt import ImageQt
from PIL.ImageQt import ImageQt
from PyQt5.QtCore import (Qt, pyqtSignal)
from PyQt5.QtCore import Qt, QDir, QRect, QTimer
from PyQt5.QtGui import QImage, QPixmap, QTransform, QPainter
from PyQt5.QtWidgets import (QApplication, QMainWindow, QGraphicsScene, QGraphicsView, QGraphicsPixmapItem,
        QMenu, QDialog, QFileDialog, QAction, QMessageBox, QFrame, QRubberBand, qApp)
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog
from PyQt5.QtGui import QPalette, QPixmap, QImage, QKeySequence
from PyQt5.QtWidgets import QWidget, QCheckBox, QApplication
from PyQt5 import QtCore, QtGui, QtWidgets
from crop_image import  Test_Resize
from PyQt5.QtCore import QSize, QCoreApplication, QSettings
from Koren_fitting import function_fit
from  ImageStorage import ImageStorage

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.window = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1067, 870)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.update = QtWidgets.QPushButton(self.centralwidget)
        self.update  .setGeometry(QtCore.QRect(830, 30, 75, 23))
        self.update .setObjectName("select area")
        self.update .clicked.connect(self.update_button)
        
        self.label_update = QtWidgets.QLabel(self.centralwidget)
        self.label_update.setGeometry(QtCore.QRect(830, 10, 187, 13))
        self.label_update.setObjectName("label")
        
        self.tube_name_field = QtWidgets.QLineEdit(self.centralwidget)
        self.tube_name_field.setGeometry(QtCore.QRect(490, 5, 113, 20))
        self.tube_name_field.setObjectName("I_max_field")
        
        
        self.label_tube_name = QtWidgets.QLabel(self.centralwidget)
        self.label_tube_name.setGeometry(QtCore.QRect(430, 10, 60, 20))
        self.label_tube_name.setObjectName("label")

        # widget for image 
        self.widget = QtWidgets.QLabel(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(190, 30, 611, 361))
        self.widget.setObjectName("widget")
        self.widget.setScaledContents(True)
        self.widget.mousePressEvent = self.getPixel
        self.get_coords_from_plot_counter = 0
        # self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        # self.pushButton_4.setGeometry(QtCore.QRect(180, 560, 75, 21))
        # self.pushButton_4.setObjectName("pushButton_4")
        # self.label_2 = QtWidgets.QLabel(self.centralwidget)
        # self.label_2.setGeometry(QtCore.QRect(80, 500, 47, 41))
        # self.label_2.setObjectName("label_2")
        # миниальное значение напряжения
        self.U0_field = QtWidgets.QLineEdit(self.centralwidget)
        self.U0_field.setGeometry(QtCore.QRect(190, 410, 113, 20))
        self.U0_field.setObjectName("U0_field")
        self.U0_field.setText('0')
        
        
        self.label_U0 = QtWidgets.QLabel(self.centralwidget)
        self.label_U0.setGeometry(QtCore.QRect(190, 390, 113, 20))
        self.label_U0.setObjectName("label")
        
        self.U_max_field = QtWidgets.QLineEdit(self.centralwidget)
        self.U_max_field.setGeometry(QtCore.QRect(690, 420, 113, 20))
        self.U_max_field.setObjectName("U_max_field")
       
        
        self.label_U_max = QtWidgets.QLabel(self.centralwidget)
        self.label_U_max.setGeometry(QtCore.QRect(690, 400, 113, 20))
        self.label_U_max.setObjectName("label"  )      
        
        self.I_max_field = QtWidgets.QLineEdit(self.centralwidget)
        self.I_max_field.setGeometry(QtCore.QRect(60, 30, 113, 20))
        self.I_max_field.setObjectName("I_max_field")

   
        
        self.label_I_max = QtWidgets.QLabel(self.centralwidget)
        self.label_I_max.setGeometry(QtCore.QRect(60, 10, 113, 20))
        self.label_I_max.setObjectName("label"  )     
        # миниальное значение тока
        self.I0_field = QtWidgets.QLineEdit(self.centralwidget)
        self.I0_field.setGeometry(QtCore.QRect(60, 370, 113, 20))
        self.I0_field.setObjectName("I0_field")
        self.I0_field.setText('0')


        self.label_I0 = QtWidgets.QLabel(self.centralwidget)
        self.label_I0.setGeometry(QtCore.QRect(60, 350, 113, 20))
        self.label_I0.setObjectName("label"  )
        
        self.Ug_field = QtWidgets.QLineEdit(self.centralwidget)
        self.Ug_field.setGeometry(QtCore.QRect(60, 500, 100, 20))
        self.Ug_field.setObjectName("U0_field")
        self.Ug_field.setText('0')



        self.label_Ug = QtWidgets.QLabel(self.centralwidget)
        self.label_Ug.setGeometry(QtCore.QRect(60, 480, 113, 20))
        self.label_Ug.setObjectName("label"  )

        self.input_Ug = QtWidgets.QPushButton(self.centralwidget)
        self.input_Ug.setGeometry(QtCore.QRect(170, 500, 75, 23))
        self.input_Ug.clicked.connect(self.input_Ug_button)
        # self.pushButton_3.setObjectName("pushButton_3")
        # self.save_IV_data = QtWidgets.QPushButton(self.centralwidget)
        # self.save_IV_data.setGeometry(QtCore.QRect(180, 510, 75, 23))
        # self.save_IV_data.setObjectName("save_IV_data")
        
        
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(323, 450, 321, 441))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        
        # self.tableView = QtWidgets.QTableView(self.centralwidget)
        # self.tableView.setGeometry(QtCore.QRect(280, 500, 621, 341))
        # self.tableView.setObjectName("tableView")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1067, 19))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")

        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        # open dialogue
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("open.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpen.setIcon(icon)
        self.actionOpen.triggered.connect(self.open_img)

        # save dialogue
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave.setIcon(icon1)
        self.actionSave.triggered.connect(self.save_tubedata_button)
        # self.actionSave.triggered.connect(self.save_img)
        
        self.menuParameters = QtWidgets.QMenu(self.menubar)
        self.menuParameters.setObjectName("menuParameters")
        self.actionCrop_image = QtWidgets.QAction(MainWindow)
        self.actionCrop_image.setObjectName("actionParamater1")
        self.actionCrop_image.triggered.connect(self.crop_image_button)

        self.actionParameter_2 = QtWidgets.QAction(MainWindow)
        self.actionParameter_2.setObjectName("actionParameter_2")
        self.menuFile.addAction(self.actionOpen)
        self.actionParameter_2.triggered.connect(self.fit_data)
        self.menuFile.addSeparator()

        self.menuFile.addAction(self.actionSave)
        self.menuParameters.addAction(self.actionCrop_image)
        self.menuParameters.addAction(self.actionParameter_2)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuParameters.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Getting Current-Voltage numerical data from datasheets plots"))
        self.update .setText(_translate("MainWindow", "update image"))
        self.label_update.setText(_translate("MainWindow", "update image after changes"))
        self.input_Ug .setText(_translate("MainWindow", "input grid V"))
        self.label_tube_name.setText(_translate("MainWindow", "tube name"))
        
        self.label_U0.setText(_translate("MainWindow", "zero-point voltage"))
        self.label_U_max.setText(_translate("MainWindow", "max voltage"))
        self.label_I_max.setText(_translate("MainWindow", "max current, mA"))
        self.label_I0.setText(_translate("MainWindow", "zero-point current, mA"))

        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "U_g"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "I_a"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "U_ak"))
        self.label_Ug .setText(_translate("MainWindow", "grid voltage"))
             
        # self.pushButton_4.setText(_translate("MainWindow", "PushButton"))
        # self.label_2.setText(_translate("MainWindow", "TextLabel"))
        # self.pushButton_3.setText(_translate("MainWindow", "PushButton"))
        # self.save_IV_data.setText(_translate("MainWindow", "PushButton"))
        
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuParameters.setTitle(_translate("MainWindow", "data processing"))
        self.actionOpen.setText(_translate("MainWindow", "Open current-voltage plot"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionCrop_image.setText(_translate("MainWindow", "crop image"))
        self.actionParameter_2.setText(_translate("MainWindow", "fit with Koren model"))
    def update_button(self):
        print('image updated')
        self.widget.clear()
        self.pixmap = ImageStorage.crop_result
        self.widget.setPixmap( self.pixmap)
        self.widget.setScaledContents(True)
    def crop_image_button(self):
            self.window = QtWidgets.QMainWindow()
            self.ui =        Test_Resize()

    def image_preprocessor(self, fname):
        image  = Image.open(fname)   
        image  = image.convert("RGBA")

        qim = ImageQt(image)
        print(type(qim))
        self.pixmap =QtGui. QPixmap(QtGui.QImage(qim))
       
       
        self.widget.setPixmap(self.pixmap)
        ImageStorage.crop_result =  self.pixmap
        ImageStorage.image  = image
    
    def open_img(self):
        fname, filter = QFileDialog.getOpenFileName(self.window, 'Open File', 'E:\Google\Progs\Python\Chrevo_progs\DAE-Scipy-main', "Image Files (*)")
        if fname:
            self.image_preprocessor(fname)
            ImageStorage.fname = fname
            
            print('showing image')
        else:
            print("Invalid Image")
    def max_min_IV( MainWindow, self):
        self.U0= (self.U0_field.text())
        self.U_max= (self.U_max_field.text())
        self.I_max= (self.I_max_field.text())
        self.I0= (self.I0_field.text())
        try:
           
            U0_ = float(self.U0)
            I0_ = float(self.I0)
            I_max_ = float(self.I_max)
            U_max_ = float(self.U_max)
          
            self.dU = U_max_ - U0_
            self.dI = I_max_ - I0_
        except:
            print('no values!')

    def table_processing( MainWindow, self):
        # с каждым тиком счеткика нажатия на график увеличивается таблица
        self.tableWidget.setRowCount(self.get_coords_from_plot_counter)
        rowPosition = self.tableWidget.rowCount()
        self.tableWidget.insertRow(rowPosition)
        self.tableWidget.setItem(rowPosition , 0, QtWidgets.QTableWidgetItem(str(self.Ug)))
        self.tableWidget.setItem(rowPosition , 1, QtWidgets.QTableWidgetItem(str(self.i)  ))
        self.tableWidget.setItem(rowPosition , 2, QtWidgets.QTableWidgetItem(str(self.u)  ))
        # self.tableWidget.insertRow(row)        # here you decide in which row
        # item = QTableWidgetItem(str(val))   # create a new Item
        # self.tableWidget.setItem(row,Y, item)
        # self.Ug = None
    list_to_save = []
    
    def save_to_dict( MainWindow, self):
 
    
        self.list_to_save.append([self.Ug, self.u, self.i])
        print(self.list_to_save)
    # получаем значения тока и напряжения в указанной мышкой точке графика
    def getPixel(self, event):
        self.max_min_IV(self)
        self.x = event.pos().x()
        self.y = event.pos().y()
        x_scale = self.widget.size().width()
        y_scale = self.widget.size().height()
        self.i = self.dI -  self.dI*self.y/y_scale
        self.u =   self.dU*self.x/x_scale
        self.i = round(self.i , 2)
        self.u = round(self.u , 2)
        print(self.i , self.u)
        # каждое нажатие увеличивает на 1 счетчик 
        self.get_coords_from_plot_counter+=1 
        # записываем значения в таблицу
        self.table_processing(self)
        self.save_to_dict(self)
        # return x, y
    # собираем все значения dict_to_save с одним ключом в листы
    
    def dict_sort( MainWindow, self):
       
        U_g_list = []
        self.dict_to_save = dict()
        for sublist in self.list_to_save:  
             U_g = sublist[0]
             U_g_list.append(U_g)
        U_g_list = sorted(set(U_g_list))
        for U_g_sorted in U_g_list:
            self.dict_to_save[U_g_sorted] = []
            UI_list_for_U_g = []
            for sublist in self.list_to_save:  
                U_g = sublist[0]
                U_a = sublist[1]
                I_a = sublist[2]
                data = (U_a, I_a)
                if U_g_sorted == U_g:
                    UI_list_for_U_g.append(data)
          
            self.dict_to_save[U_g_sorted] = UI_list_for_U_g
            
            
    def startupCheck(self):
        if os.path.isfile('TubeIVlib.json'):
        # checks if file exists
                print ("File exists and is readable")
        else:
            print ("Either file is missing or is not readable, creating file...")
            with open ('TubeIVlib.json', 'w+') as file:
                json.dump(dict(), file)
    # сохраняем сырые данные в библиотеку
    def save_tubedata_button(self):
        self.dict_sort(self)
        print('записывается словарь')
        print(self.dict_to_save)
        ImageStorage.dict_data  = self.dict_to_save
        self.tube_name = self.tube_name_field.text()
        # print(pd.DataFrame.from_dict(self.dict_to_save) )
        print()
        print(self.tube_name)
        print()
        self.startupCheck()
        with open(str(self.tube_name) +'.txt', 'w') as f:
                f.write(str(self.dict_to_save) )
        with open ('TubeIVlib.json', 'w+') as file:
            try:
                TubeIVdict = json.load(file)
            except:
                TubeIVdict = dict()
            TubeIVdict[self.tube_name]=self.dict_to_save
            json.dump(TubeIVdict, file)
        with open ('TubeIVlib.json', 'r') as file:
            TubeIVdict = json.load(file)
            print(TubeIVdict)
        # self.tubename
    def input_Ug_button(self):
       self.Ug_= (self.Ug_field.text())
       try:
           self.Ug = float( self.Ug_)
           self.Ug = round(self.Ug, 2)
       except:
            print('no values!')
            
    def fit_data(self):
       self.tube_name = self.tube_name_field.text()
       function_fit(str(self.tube_name))

    def del_from_table(self):
        pass

        
if __name__ == "__main__":
    import sys
    app =  QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())