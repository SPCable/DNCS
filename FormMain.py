from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QAction, QInputDialog, QDialog
import os
from CLL import *
from FromSV import Ui_From
import sys
from NhanDien import *
import pandas as pd
import random
from pandas import DataFrame

class Ui_Main(object):
    def setup(self, Main):
        Main.setObjectName("Main")
        Main.resize(900, 550)
        Main.setWindowIcon(QIcon('Images\Icon.png'))
        self.centralwidget = QtWidgets.QWidget(Main)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 900, 555))
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/newPrefix/Images/background.jpg"))
        self.label.setObjectName("label")
        self.menuBox2 = QtWidgets.QLabel(self.centralwidget)
        self.menuBox2.setGeometry(QtCore.QRect(0, 0, 232, 555))
        self.menuBox2.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.menuBox2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.menuBox2.setAutoFillBackground(False)
        self.menuBox2.setStyleSheet("  height: 232px;\n"
"  width: 555px;\n"
"  background-color: #674ea7;\n"
"")
        self.menuBox2.setFrameShape(QtWidgets.QFrame.Box)
        self.menuBox2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.menuBox2.setText("")
        self.menuBox2.setObjectName("menuBox2")
        self.menuBox1 = QtWidgets.QLabel(self.centralwidget)
        self.menuBox1.setGeometry(QtCore.QRect(0, 0, 232, 58))
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.menuBox1.setFont(font)
        self.menuBox1.setStyleSheet("background-color: #351c75;\n"
"color: white;\n"
"")
        self.menuBox1.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.menuBox1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.menuBox1.setObjectName("menuBox1")
        self.btnDS = QtWidgets.QPushButton(self.centralwidget)
        self.btnDS.setGeometry(QtCore.QRect(0, 60, 231, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.btnDS.setFont(font)
        self.btnDS.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnDS.setStyleSheet("color: rgb(255, 255, 255);")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("D:/Data/Python/Đồ án cơ sở/Images/1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnDS.setIcon(icon)
        self.btnDS.setIconSize(QtCore.QSize(32, 32))
        self.btnDS.setCheckable(False)
        self.btnDS.setFlat(True)
        self.btnDS.setObjectName("btnDS")
        self.btnLS = QtWidgets.QPushButton(self.centralwidget)
        self.btnLS.setGeometry(QtCore.QRect(0, 120, 231, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.btnLS.setFont(font)
        self.btnLS.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnLS.setStyleSheet("color: rgb(255, 255, 255);")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("D:/Data/Python/Đồ án cơ sở/Images/2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnLS.setIcon(icon1)
        self.btnLS.setIconSize(QtCore.QSize(32, 32))
        self.btnLS.setCheckable(False)
        self.btnLS.setFlat(True)
        self.btnLS.setObjectName("btnLS")
        self.btnThoat = QtWidgets.QPushButton(self.centralwidget)
        self.btnThoat.setGeometry(QtCore.QRect(0, 180, 231, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnThoat.sizePolicy().hasHeightForWidth())
        self.btnThoat.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.btnThoat.setFont(font)
        self.btnThoat.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnThoat.setStyleSheet("color: rgb(255, 255, 255);")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("D:/Data/Python/Đồ án cơ sở/Images/5.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnThoat.setIcon(icon2)
        self.btnThoat.setIconSize(QtCore.QSize(32, 32))
        self.btnThoat.setCheckable(False)
        self.btnThoat.setFlat(True)
        self.btnThoat.setObjectName("btnThoat")
        
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(17, 12, 32, 32))
        self.label_4.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("D:/Data/Python/Đồ án cơ sở/Images/7.png"))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(1, 0, 901, 58))
        self.label_5.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_5.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_5.setAutoFillBackground(False)
        self.label_5.setStyleSheet("  height: 232px;\n"
"  width: 555px;\n"
"  background-color: #674ea7;\n"
"")
        self.label_5.setFrameShape(QtWidgets.QFrame.Box)
        self.label_5.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        
        self.btnLeft = QtWidgets.QPushButton(self.centralwidget)
        self.btnLeft.setGeometry(QtCore.QRect(210, 250, 41, 41))
        self.btnLeft.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnLeft.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("D:/Data/Python/Đồ án cơ sở/Images/6.png"))
        self.btnLeft.setIcon(icon5)
        self.btnLeft.setObjectName("btnLeft")
        self.btnLeft.setIconSize(QtCore.QSize(32,32))
        self.btnLeft.setFlat(True)

        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(690, 0, 211, 58))
        self.widget1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.widget1.setEnabled(True)
        self.widget1.setObjectName("widget1")
        self.widget1.hide()
        
        self.btnAdd = QtWidgets.QPushButton(self.widget1)
        self.btnAdd.setGeometry(QtCore.QRect(30, 0, 58, 58))
        self.btnAdd.setText("")
        iconAdd = QtGui.QIcon()
        iconAdd.addPixmap(QtGui.QPixmap("D:/Data/Python/Đồ án cơ sở/Images/plus.png"))
        self.btnAdd.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnAdd.setIcon(iconAdd)
        self.btnAdd.setObjectName("btnAdd")
        self.btnAdd.setIconSize(QtCore.QSize(50,50))
        self.btnAdd.setFlat(True)

        self.btnDel = QtWidgets.QPushButton(self.widget1)
        self.btnDel.setGeometry(QtCore.QRect(90, 0, 58, 58))
        self.btnDel.setText("")
        iconAdd = QtGui.QIcon()
        iconAdd.addPixmap(QtGui.QPixmap("D:/Data/Python/Đồ án cơ sở/Images/close.png"))
        self.btnDel.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnDel.setIcon(iconAdd)
        self.btnDel.setObjectName("btnDel")
        self.btnDel.setIconSize(QtCore.QSize(50,50))
        self.btnDel.setFlat(True)

        self.btnSua = QtWidgets.QPushButton(self.widget1)
        self.btnSua.setGeometry(QtCore.QRect(150, 0, 58, 58))
        self.btnSua.setText("")
        iconAdd = QtGui.QIcon()
        iconAdd.addPixmap(QtGui.QPixmap("D:/Data/Python/Đồ án cơ sở/Images/question.png"))
        self.btnSua.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnSua.setIcon(iconAdd)
        self.btnSua.setObjectName("btnSua")
        self.btnSua.setIconSize(QtCore.QSize(50,50))
        self.btnSua.setFlat(True)

        self.widget2 = QtWidgets.QWidget(self.centralwidget)
        self.widget2.setGeometry(QtCore.QRect(232, 58, 670, 492))
        self.widget2.setEnabled(True)
        self.widget2.setObjectName("widget2")
        self.widget2.hide()

        self.widget3 = QtWidgets.QWidget(self.widget2)
        self.widget3.setGeometry(QtCore.QRect(430, 0, 241, 492))
        self.widget3.setEnabled(True)
        self.widget3.setObjectName("widget3")
        self.widget3.setStyleSheet("background: #9370DB")

        self.ListClass = QtWidgets.QListWidget(self.widget2)
        self.ListClass.setGeometry(0,0,430,492)
        self.ListClass.setFrameShape(QtWidgets.QFrame.NoFrame)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(75)
        self.ListClass.setFont(font)

        self.label_info = QtWidgets.QLabel(self.widget3)
        self.label_info.setGeometry(60,20,121,41)
        self.label_info.setText("Thông tin")
        self.label_info.setStyleSheet("color: white;")
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(16)
        self.label_info.setFont(font)

        self.box_info = QtWidgets.QGroupBox(self.widget3)
        self.box_info.setGeometry(10,60,221,301)
        self.box_info.setFlat(1)

        self.btnDD = QtWidgets.QPushButton(self.widget3)
        self.btnDD.setGeometry(40,390,160,50)
        self.btnDD.setText("Điểm danh")
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        font.setBold(True)
        self.btnDD.setFont(font)
        self.btnDD.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnDD.setStyleSheet("color: white; background-color: #371f57;")
        self.btnDD.setObjectName("btnDD")

        self.widget4 = QtWidgets.QWidget(self.centralwidget)
        self.widget4.setGeometry(QtCore.QRect(232, 58, 670, 492))
        self.widget4.setEnabled(True)
        self.widget4.setObjectName("widget4")
        self.widget4.hide()

        self.ListH = QtWidgets.QTableWidget(self.widget4)
        self.ListH.setGeometry(QtCore.QRect(0,0,680,400))
        self.ListH.setObjectName("ListH")
        self.ListH.setStyleSheet("color: black")
        self.ListH.setColumnCount(5)
        self.ListH.setAlternatingRowColors(True)
        self.ListH.setHorizontalHeaderLabels(("Mã lớp","Tên lớp","Môn Học","Sỉ số","Vắng"))
        self.ListH.horizontalHeader().setCascadingSectionResizes(False)
        self.ListH.horizontalHeader().setSortIndicatorShown(False)
        self.ListH.horizontalHeader().setStretchLastSection(True)
        self.ListH.verticalHeader().setVisible(False)
        self.ListH.verticalHeader().setCascadingSectionResizes(False)
        self.ListH.verticalHeader().setStretchLastSection(False)
        self.ListH.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.ListH.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.btnhis = QtWidgets.QPushButton(self.widget4)
        self.btnhis.setGeometry(40,420,160,50)
        self.btnhis.setText("Xem chi tiết")
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        font.setBold(True)
        self.btnhis.setFont(font)
        self.btnhis.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnhis.setStyleSheet("color: white; background-color: #371f57;")
        self.btnhis.setObjectName("btnDD")

        self.btnex = QtWidgets.QPushButton(self.widget4)
        self.btnex.setGeometry(450,420,160,50)
        self.btnex.setText("Xuất Excel")
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        font.setBold(True)
        self.btnex.setFont(font)
        self.btnex.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnex.setStyleSheet("color: white; background-color: #371f57;")
        self.btnex.setObjectName("btnDD")


        font_info = QtGui.QFont()
        font_info.setFamily("MS Shell Dlg 2")
        font_info.setPointSize(11)
        font_info.setBold(True)

        self.label1 = QtWidgets.QLabel(self.box_info)
        self.label1.setText("Tên Lớp: ")
        self.label1.setGeometry(10,30,120,30)
        self.label1.setFont(font_info)
        self.label1.setStyleSheet("color: white")

        self.label2 = QtWidgets.QLabel(self.box_info)
        self.label2.setText("Tên Môn Học: ")
        self.label2.setGeometry(10,80,120,30)
        self.label2.setFont(font_info)
        self.label2.setStyleSheet("color: white")

        self.label3 = QtWidgets.QLabel(self.box_info)
        self.label3.setText("Sỉ Số Lớp: ")
        self.label3.setGeometry(10,130,120,30)
        self.label3.setFont(font_info)
        self.label3.setStyleSheet("color: white")

        self.label10 = QtWidgets.QLabel(self.box_info)
        self.label10.setText("Trống")
        self.label10.setGeometry(140,30,120,30)
        self.label10.setFont(font_info)
        self.label10.setStyleSheet("color: white")
        self.label10.setObjectName("class")

        self.label11 = QtWidgets.QLabel(self.box_info)
        self.label11.setText("Trống")
        self.label11.setGeometry(130,80,120,30)
        self.label11.setFont(font_info)
        self.label11.setStyleSheet("color: white")
        self.label11.setObjectName("subject")

        self.label12 = QtWidgets.QLabel(self.box_info)
        self.label12.setText("Trống")
        self.label12.setGeometry(130,130,120,30)
        self.label12.setFont(font_info)
        self.label12.setStyleSheet("color: white")
        self.label12.setObjectName("number")


        self.label.raise_()
        self.label_5.raise_()
        self.menuBox2.raise_()
        self.menuBox1.raise_()
        self.btnDS.raise_()
        self.btnLS.raise_()
        self.btnThoat.raise_()
        self.ListClass.raise_()
        self.label_4.raise_()
        self.widget1.raise_()  
        self.widget2.raise_()
        self.widget3.raise_()
        self.widget4.raise_()
        self.btnDD.raise_()  
        self.btnLeft.raise_() 
        Main.setCentralWidget(self.centralwidget)

        self.retranslateUi(Main)
        QtCore.QMetaObject.connectSlotsByName(Main)

    def retranslateUi(self, Main):
        _translate = QtCore.QCoreApplication.translate
        Main.setWindowTitle(_translate("Main", "Phần mềm điểm danh by@team2"))
        self.menuBox1.setText(_translate("Main", "        MENU"))
        self.btnDS.setText(_translate("Main", " Danh sách lớp học"))
        self.btnLS.setText(_translate("Main", " Lịch sử điểm danh"))
        self.btnThoat.setText(_translate("Main", " Thoát "))


        # su kien click cac nut
        self.btnLeft.clicked.connect(self.Click_Left)
        self.btnThoat.clicked.connect(self.Click_Exit)
        self.btnDS.clicked.connect(self.Click_btnDS)
        self.btnLS.clicked.connect(self.Click_btnLS)
        self.btnAdd.clicked.connect(self.Click_Add)
        self.btnDel.clicked.connect(self.Click_Del)
        self.btnSua.clicked.connect(self.Click_Ch)
        self.ListClass.itemSelectionChanged.connect(self.selectionChanged)
        self.ListClass.itemDoubleClicked.connect(self.MoFormSinhVien)
        self.btnDD.clicked.connect(self.DiemDanh)
        self.btnex.clicked.connect(self.Click_btnLS)

        self.f = 0
    def Click_Left(self):
        if self.f == 0:
            self.menuBox2.setGeometry(QtCore.QRect(0, 0, 65, 555))
            self.menuBox1.setGeometry(QtCore.QRect(0, 0, 65, 58))
            self.btnLeft.setGeometry(QtCore.QRect(45, 250, 41, 41))
            self.btnDS.setGeometry(QtCore.QRect(0, 60, 65, 61))
            self.btnLS.setGeometry(QtCore.QRect(0, 120, 65, 61))
            self.btnThoat.setGeometry(QtCore.QRect(0, 180, 65, 61))
            self.widget2.setGeometry(QtCore.QRect(65, 58, 881, 492))
            self.ListClass.setGeometry(QtCore.QRect(0,0,620,492))
            self.ListH.setGeometry(QtCore.QRect(0,0,680,400))
            self.widget3.setGeometry(QtCore.QRect(620, 0, 750, 492))
            self.widget4.setGeometry(QtCore.QRect(65, 58, 880, 492))

            self.btnDS.setText("")
            self.btnLS.setText("")
            self.btnThoat.setText("")
            self.f = 1
        else:
            self.menuBox2.setGeometry(QtCore.QRect(0, 0, 231, 555))
            self.menuBox1.setGeometry(QtCore.QRect(0, 0, 231, 58))
            self.btnLeft.setGeometry(QtCore.QRect(210, 250, 41, 41))
            self.btnDS.setGeometry(QtCore.QRect(0, 60, 231, 61))
            self.btnLS.setGeometry(QtCore.QRect(0, 120, 231, 61))
            self.btnThoat.setGeometry(QtCore.QRect(0, 180, 231, 61))
            self.widget2.setGeometry(QtCore.QRect(232, 58, 670, 492))
            self.ListClass.setGeometry(QtCore.QRect(0,0,430,492))
            self.widget3.setGeometry(QtCore.QRect(430, 0, 241, 492))
            self.widget4.setGeometry(QtCore.QRect(232, 58, 670, 492))
            self.ListH.setGeometry(QtCore.QRect(0,0,700,400))

            self.btnDS.setText(" Danh sách lớp học")
            self.btnLS.setText(" Lịch sử điểm danh")
            self.btnThoat.setText(" Thoát")
            self.f = 0
    # event de xu ly cac button:
    def MoFormSinhVien(self):
        row_number = self.ListClass.currentRow()
        self.newform = QtWidgets.QMainWindow()
        self.ui = Ui_From()
        index = self.ListClass.currentRow()
        self.ui.setupUi(self.newform,self.label11.text(), self.label10.text(),str(self.ListClass.item(row_number).text()),self.label12.text())
        self.ui.LoadData()
        self.newform.show()

    def DiemDanh(self):
        self.UIwindow = QMainWindow()
        self.UIwindow = UI_NhanDien(self.text)
        self.UIwindow.show()
    def Click_Exit(self):
        sys.exit(object)
        
    def Click_btnDS(self):
        self.widget1.show()
        self.widget2.show()
        self.widget4.hide()
        self.XoaDS()
        self.Hienthilop()

    def Click_btnLS(self):
        self.widget1.hide()
        self.widget2.hide()
        self.widget4.show()

    def Click_btnHD(self):
        self.widget1.hide()
        self.widget2.hide()

    def Click_Setting(self):
        self.widget1.hide()
        self.widget2.hide()

    def Click_Add(self):
        self.newform = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.newform)
        self.newform.show()

    def Click_Del(self):
        row = self.ListClass.currentRow()
        item = self.ListClass.item(row)
        try:
            x =  str(item.text())
            t =  x.split(".")
            reply = QtWidgets.QMessageBox.question(Main, "Xóa","Bạn có muốn xóa " + str(item.text()), QMessageBox.Yes | QMessageBox.No)
            if reply == QMessageBox.Yes:
                try:
                    self.conn = sqlite3.connect('Database\Lop.db')
                    query = 'delete from Lop Where id='+ str(t[0])
                    self.conn.execute(query)
                    self.conn.commit()
                    self.conn.close()
                    self.XoaThuMuc()
                    self.XoaDS()
                    self.Hienthilop()
                except Exception:
                    QMessageBox.warning(QMessageBox(),"Lỗi", "Chưa xóa được")
        except Exception:
            QMessageBox.warning(QMessageBox(),"Lỗi", "Hãy chọn đối tượng cần xóa")

    def Click_Ch(self):
        self.XoaDS()
        self.Hienthilop()
    
    def XoaThuMuc(self):
        row = self.ListClass.currentRow()
        item = self.ListClass.item(row)
        path  = 'Database\Dataset\ ' + str(item.text())
        os.rmdir(path)

    def Hienthilop(self):
        try:
            self.conn = sqlite3.connect('Database\Lop.db')
            query = "SELECT * From Lop"
            result = self.conn.execute(query)
            self.conn.commit()          
            for row_number, row_data in enumerate (result):
                self.ListClass.addItem(str(row_data[0]) +"."+ row_data[1])
            self.conn.close()
        except Exception:
            QMessageBox.warning(QMessageBox(),"ket noi","Ket noi that bai")
    def XoaDS(self):
        self.ListClass.clear()

    def selectionChanged(self):
        index =  self.ListClass.currentRow()
        id_ = self.ListClass.item(index).text()
        self.text = str(id_)
        x = self.text.split(".")
        self.conn = sqlite3.connect('Database\Lop.db')
        result = self.conn.execute("select * from Lop where id=" + str(x[0]))
        self.conn.commit()
        for row, data in enumerate(result):
            self.y =  data[2]
            self.z = data[3]
        self.conn.close()
        self.label10.setText(str(x[1]))
        self.label11.setText(str(self.y))
        self.label12.setText(str(self.z))
        

import Source_rc
from base64 import main
from PyQt5.QtGui import QIcon
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Main = QtWidgets.QMainWindow()
    ui = Ui_Main()
    ui.setup(Main)
    Main.show()
    sys.exit(app.exec_())
