
from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
from PyQt5.QtWidgets import *
import os
from FormMain import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(450, 271)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-6, -5, 711, 511))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/newPrefix/Images/background.jpg"))

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20 ,40,141,21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: white")


        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20 ,90,141,21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: white")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20 ,140,141,21))

        self.groupbox = QtWidgets.QGroupBox(MainWindow)
        self.groupbox.setGeometry(QtCore.QRect(10,10,431,181))
        self.groupbox.setTitle("Vui lòng nhập đầy đủ thông tin")
        self.groupbox.setStyleSheet("color: white")
        self.groupbox.setFont(font)

        self.lineEdit2 = QtWidgets.QLineEdit(self.groupbox)
        self.lineEdit2.setGeometry(QtCore.QRect(200,40,181,20))
        self.lineEdit2.setStyleSheet("color: black ")

        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupbox)
        self.lineEdit_2.setGeometry(QtCore.QRect(200,90,181,20))
        self.lineEdit_2.setStyleSheet("color: black")
        
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupbox)
        self.lineEdit_3.setGeometry(QtCore.QRect(200,140,181,20))
        self.lineEdit_3.setStyleSheet("color: black")


        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: white")
        self.label_5.setObjectName("label_5")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(145,210,161,51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: purple;\n"
"color : white")
        self.pushButton.setObjectName("pushButton")

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.pushButton.clicked.connect(self.taolop)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Tạo Lớp"))
        self.label_3.setText(_translate("MainWindow", "Tên Lớp:"))
        self.label_4.setText(_translate("MainWindow", "Tên Môn Học:"))
        self.label_5.setText(_translate("MainWindow", "Số Lượng SV:"))
        self.pushButton.setText(_translate("MainWindow", "Tạo"))
        
    def taolop(self):
        tenlop=""
        monhoc=""
        soluong=0
        id_=0
        tenlop =self.lineEdit2.text()
        monhoc =self.lineEdit_2.text()
        soluong =self.lineEdit_3.text()
        if tenlop.strip(" ")!="" and monhoc.strip(" ")!="" and soluong.strip(" ")!="":
            self.conn=sqlite3.connect('Database\Lop.db')
            self.c=self.conn.cursor()
        
            self.c.execute("INSERT INTO lop(tenlop, monhoc, soluong) VALUES(?, ?, ?)",(tenlop,monhoc,soluong))
            self.conn.commit()
            self.c.close()
            self.conn.close()
            QMessageBox.warning(QMessageBox(),"Thong bao","Ban da them thanh cong")
            self.TaoThuMuc()
        else: 
            QMessageBox.warning(QMessageBox(),"Thong bao","Ban chua nhap thong tin")

    def TaoThuMuc(self):
        self.conn = sqlite3.connect('Database\Lop.db')
        name = self.lineEdit2.text()
        result = self.conn.execute("Select id from lop where tenlop =" + "'" + str(name) + "'")
        self.conn.commit()
        for row_number, data in enumerate (result):
            x = data[0]
        self.conn.close()
        path = 'Database\Dataset\ ' + str(x) + "." + str(name)
        os.mkdir(path)
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
