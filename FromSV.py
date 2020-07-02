from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys
import time
import os
import ScanFace
import train


class Ui_From(object):
    def setupUi(self, From,name_subject,name_class,name_folder_class,number_students):
        From.setObjectName("From")
        From.resize(870, 550)
        From.setWindowFilePath("")

        self.nameFolder = name_folder_class
        self.Background = QtWidgets.QLabel(From)
        self.Background.setGeometry(QtCore.QRect(0, 0, 900, 550))
        self.Background.setPixmap(QtGui.QPixmap(":/newPrefix/Images/background.jpg"))
        self.groupBox = QtWidgets.QGroupBox(From)
        self.groupBox.setGeometry(QtCore.QRect(0, 20, 901, 231))
        self.groupBox.setMouseTracking(False)
        self.groupBox.setTabletTracking(False)
        self.groupBox.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.groupBox.setAcceptDrops(False)
        self.groupBox.setAutoFillBackground(False)
        self.groupBox.setStyleSheet("color:white;")
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName("groupBox")
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)

        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(20, 120, 71, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:white;")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(20, 160, 71, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color:white;")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(20, 200, 71, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color:white;")
        self.label_4.setObjectName("label_4")

        self.lbLop = QtWidgets.QLabel(self.groupBox)
        self.lbLop.setGeometry(QtCore.QRect(20, 40, 211, 20))
        self.lbLop.setText(name_class)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setWeight(50)
        font.setBold(True)
        self.lbLop.setStyleSheet("color:white;")
        self.lbLop.setFont(font)

        self.lbMonHoc = QtWidgets.QLabel(self.groupBox)
        self.lbMonHoc.setGeometry(QtCore.QRect(20, 80, 201, 20))
        self.lbMonHoc.setText(name_subject)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(True)
        self.lbMonHoc.setStyleSheet("color:white;")
        self.lbMonHoc.setFont(font)
        
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(20, 200, 71, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color:white;")
        self.label_6.setObjectName("label_6")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(100, 110, 201, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setStyleSheet("color: black;")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_2.setGeometry(QtCore.QRect(100, 150, 201, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setStyleSheet("color: black;")
        self.comboBox_2 = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_2.setGeometry(QtCore.QRect(100, 190, 201, 31))
        self.comboBox_2.setObjectName("comboBox_2")   
        self.comboBox_2.setStyleSheet("color: black;")

        self.comboBox_2.addItem("NAM")
        self.comboBox_2.addItem("NỮ")

        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)

        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(330, 130, 100, 91))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setStyleSheet("background: purple;color:white;")
        self.pushButton.setFont(font)
        self.pushButton.setEnabled(False)

        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(560, 180, 111, 40))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setStyleSheet("background: purple;color:white;")
        self.pushButton_2.setFont(font)

        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_3.setGeometry(QtCore.QRect(440, 180, 111, 40))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setStyleSheet("background: purple;color:white;")
        self.pushButton_3.setFont(font)

        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_4.setGeometry(QtCore.QRect(440, 130, 111, 40))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.setStyleSheet("background: purple;color:white;")
        self.pushButton_4.setFont(font)

        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_5.setGeometry(QtCore.QRect(560, 130, 111, 40))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.setStyleSheet("background: purple;color:white;")
        self.pushButton_5.setFont(font)
        
        self.pushButton_6 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_6.setGeometry(QtCore.QRect(680, 180, 111, 40))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.setStyleSheet("background: purple;color:white;")
        self.pushButton_6.setFont(font)
        
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(500, 30, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("")
        self.label_8.setObjectName("label_8")

        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setGeometry(QtCore.QRect(680, 10, 140, 160))
        self.label_9.setObjectName("label_9")

        self.label_10 = QtWidgets.QLabel(self.groupBox)
        self.label_10.setGeometry(QtCore.QRect(450,10,150,21))
        self.label_10.setText(number_students)

        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        
        self.groupBox_2 = QtWidgets.QGroupBox(From)
        self.groupBox_2.setStyleSheet("color: white;")
        self.groupBox_2.setGeometry(QtCore.QRect(0, 260, 901, 291))
        self.groupBox_2.setObjectName("groupBox_2")
        self.groupBox_2.setFont(font)

        self.btnTim = QtWidgets.QPushButton(self.groupBox_2)
        self.btnTim.setGeometry(QtCore.QRect(720,20, 121,31))
        self.btnTim.setText("SEARCH")
        self.btnTim.setStyleSheet("background: purple;")
        self.btnTim.setFont(font)

        self.thanhtimkiem = QtWidgets.QLineEdit(self.groupBox_2)
        self.thanhtimkiem.setGeometry(QtCore.QRect(540,20 , 201, 31))
        self.thanhtimkiem.setStyleSheet("color: black;")
       
        self.listView = QtWidgets.QTableWidget(self.groupBox_2)
        self.listView.setGeometry(QtCore.QRect(10, 60, 851, 221))
        self.listView.setObjectName("listView")
        self.listView.setStyleSheet("color: black")
        self.listView.setColumnCount(6)
        self.listView.setAlternatingRowColors(True)
        self.listView.setHorizontalHeaderLabels(("MSSV","Họ và tên","Lớp","Giới Tính","Môn Học","Hình ảnh"))
        self.listView.horizontalHeader().setCascadingSectionResizes(False)
        self.listView.horizontalHeader().setSortIndicatorShown(False)
        self.listView.horizontalHeader().setStretchLastSection(True)
        self.listView.verticalHeader().setVisible(False)
        self.listView.verticalHeader().setCascadingSectionResizes(False)
        self.listView.verticalHeader().setStretchLastSection(False)
        self.listView.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.listView.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.listView.setFont(font)

        self.pushButton_2.clicked.connect(self.LoadData)
        self.pushButton_4.clicked.connect(self.addstudent)
        self.pushButton_5.clicked.connect(self.delstudent)
        self.pushButton_3.clicked.connect(self.updateST)
        self.btnTim.clicked.connect(self.TimKiem)
        self.pushButton.clicked.connect(self.ScanKhuonMat)
        self.listView.itemSelectionChanged.connect(self.selectionChanged)
        self.pushButton_6.clicked.connect(self.SaveAndTrain)

        self.retranslateUi(From)
        QtCore.QMetaObject.connectSlotsByName(From)

    def retranslateUi(self, From):
        _translate = QtCore.QCoreApplication.translate
        From.setWindowTitle(_translate("From", "Quản lý sinh viên "))
        self.groupBox.setTitle(_translate("From", "Thông tin sinh viên::"))
        self.label_2.setText(_translate("From", "Họ và tên::"))
        self.label_3.setText(_translate("From", "MSSV::"))
        self.label_6.setText(_translate("From", "Giới tính:"))
        self.pushButton.setText(_translate("From", "SCAN"))
        self.pushButton_2.setText(_translate("From", "REFRESH"))
        self.pushButton_3.setText(_translate("From", "UPDATE"))
        self.pushButton_4.setText(_translate("From", "ADD"))
        self.pushButton_5.setText(_translate("From", "DELETE"))
        self.pushButton_6.setText(_translate("From", "SAVE"))

        self.label_9.setText(_translate("From", "Picture"))
        self.groupBox_2.setTitle(_translate("From", "Student List:"))

    def SaveAndTrain(self):
        self.form = QMainWindow()
        self.label_anima=QtWidgets.QLabel(self.form)
        self.movie = QtGui.QMovie('image/loading.gif')
        self.label_anima.setMovie(self.movie)
        self.movie.start()
        self.form.show()
        train.trainning(self.nameFolder)
        print("Da Training xong")

    def DocHinhAnh(self, mssv, ten, row_number):
        demfile = 0
        path1 = "Database\Dataset\ " + str(self.nameFolder) +"\ "+ str(mssv) + "." + str(ten)
       
        for root, dirs, files in os.walk(path1):
            for file in files:
                if file.endswith("png"):
                    demfile +=1
        if(demfile>=1):
            self.listView.setItem(row_number,5,QTableWidgetItem("Có"))
        else:
            self.listView.setItem(row_number,5,QTableWidgetItem("Không có"))

    def ScanKhuonMat(self):
        mssv = self.lineEdit_2.text()
        ten = self.lineEdit.text()
        if(mssv.strip(" ")!="" and ten.strip(" ")!=""):
            path = "Database\Dataset\ " + str(self.nameFolder) +"\ "+ str(mssv) + "." + str(ten)
            ScanFace.QuetKhuonMat(path)
            QMessageBox.warning(QMessageBox(),"Thông báo", "Đã Scan Xong!")
        else:
            QMessageBox.warning(QMessageBox(),"Thong bao loi", "Ban chua chon sinh vien")

    
    def LoadData(self):
        self.clearData()
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.connect = sqlite3.connect("Database\SinhVien.db")
        query = "SELECT * FROM SINHVIEN WHERE lop =" + "'" + str(self.lbLop.text()) + "'"
        result = self.connect.execute(query)
        for row_number, row_data in enumerate(result):
            self.listView.insertRow(row_number)
            for column_number, data in  enumerate(row_data):
                self.listView.setItem(row_number,column_number, QtWidgets.QTableWidgetItem(str(data)))
            mssv = self.listView.item(row_number,0).text()
            name = self.listView.item(row_number,1).text()
            self.DocHinhAnh(mssv,name,row_number)
        self.connect.close()
        self.label_9.setText("No Picture")

    def ResultData(self, query):
        self.conn = sqlite3.connect("Database\SinhVien.db")
        result =  self.conn.execute(query)
        for row_number, row_data in enumerate(result):
            self.listView.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.listView.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        self.conn.close()


    def clearData(self):
        self.listView.clearSelection()
        while (self.listView.rowCount()) > 0:
            self.listView.removeRow(0)
            self.listView.clearSelection()

    def selectionChanged(self):
        self.pushButton.setEnabled(True)
        self.LayThongTin()

    def LayThongTin(self):
        index = self.listView.currentRow()
        mssv = self.listView.item(index,0).text()
        name = self.listView.item(index,1).text()
        self.thumuc = mssv + "." + name
        self.lineEdit.setText(name)
        self.lineEdit_2.setText(mssv)
        path = "Database\Dataset\ "+ str(self.nameFolder) +"\ " + str(mssv)+"."+str(name)+"\ "+"1"+"."+"png"
        self.label_9.setPixmap(QtGui.QPixmap(path))
        self.label_9.setScaledContents(1)


    def TimKiem(self):
        id_ =  self.thanhtimkiem.text()
        index = self.listView.currentRow()
        mssv = self.listView.item(index,0).text()
        name = self.listView.item(index,1).text()
        if self.thanhtimkiem.text().strip(" ") != "":
            try:
                query = "SELECT * from SinhVien WHERE mssv =" + str(id_)
                self.thanhtimkiem.clear()
                self.clearData()
                self.ResultData(query)
                self.DocHinhAnh(mssv,name,0)
            except Exception:
                QMessageBox.warning(QMessageBox(),'Loi roi','Loi ket noi')
        else:
            QMessageBox.warning(QMessageBox(),'Loi','Ban chua nhap thong tin tim kiem')

    def updateST(self):
        ten  = self.lineEdit.text()
        mssv = self.lineEdit_2.text()
        path = 'Database\Dataset\ 1.17dtha5'
        self.thumucmoi = mssv + "." + ten
        lop = self.lbLop.text()
        giotinh= self.comboBox_2.itemText(self.comboBox_2.currentIndex())
        monhoc = self.lbMonHoc.text()
        if(ten.strip(" ")!="" and mssv.strip(" ")!=""):
            try:
                os.rename(path + "\ " + self.thumuc,  path + '\ ' + self.thumucmoi)
                user = (mssv, ten,lop,giotinh,monhoc)
                self.conn = sqlite3.connect('Database\SinhVien.db')
                self.conn.execute("UPDATE SinhVien SET mssv=?,hoten=?,lop=?,gioitinh=?,monhoc=? WHERE mssv ="+str(mssv),user)
                self.conn.commit()
                self.conn.close()
                self.clearData()
                self.LoadData()
                

            except Exception:
                QMessageBox.warning(QMessageBox(),'Loi roi','Loi ket noi')
        else: 
            QMessageBox.warning(QMessageBox(),'Thong tin', 'Trong')

    def delstudent(self):
        mssv=""
        mssv = self.lineEdit_2.text()
        ten = self.lineEdit.text()
        if(mssv.strip(" ")!="" and ten.strip(" ")!=""):
            dialog = QMessageBox.warning(QMessageBox(), "Thong bao", "Ban co muon xoa " + str(mssv) +" "+ str(ten) + " khong ?",QMessageBox.Yes, QMessageBox.No)
            if  dialog == QMessageBox.Yes:
                try:
                    query = " delete from SinhVien where mssv =" + str(mssv)
                    self.conn =  sqlite3.connect('Database\SinhVien.db')
                    self.c = self.conn.cursor()
                    self.c.execute(query)
                    self.conn.commit()
                    self.c.close()
                    self.conn.close()
                    self.xoaThumuc()
                    self.LoadData()
                except Exception:
                    QMessageBox.information(QMessageBox(),"Thong bao","Loi khong the xoa!")
    
    # tao thu muc chua hinh anh cua doi tuong
    def taoThuMuc(self, mssv = 0):
        mssv = self.lineEdit_2.text()
        ten = self.lineEdit.text()
        path = "Database\Dataset\ " + str(self.nameFolder) +"\ "+ str(mssv) + "." + str(ten)
        os.mkdir(path)
        print("da tao thu muc")

    def xoaThumuc(self):
        mssv = self.lineEdit_2.text()
        ten = self.lineEdit.text()
        path = "Database\Dataset\ " + str(self.nameFolder) +"\ "+ str(mssv) + "." + str(ten)
        os.rmdir(path)
        print("da xoa thu muc")

    def addstudent(self):
        hoten=""
        mssv=""
        lop=""
        gioitinh=""
        monhoc=""
        hinhanh = 0 
        
        hoten = self.lineEdit.text()
        mssv = self.lineEdit_2.text()
        gioitinh = self.comboBox_2.itemText(self.comboBox_2.currentIndex())
        lop = self.lbLop.text()
        monhoc = self.lbMonHoc.text()
        
        if(hoten.strip(" ")!="" and mssv.strip(" ") !=""):
            try:    
                self.conn = sqlite3.connect('Database\SinhVien.db')
                self.c = self.conn.cursor()
                self.c.execute("INSERT INTO SinhVien (mssv,hoten,lop,gioitinh,monhoc,hinhanh) VALUES (?,?,?,?,?,?)",(mssv,hoten,lop,gioitinh,monhoc,hinhanh))
                self.conn.commit()
                self.c.close()
                self.conn.close()
                QMessageBox.information(QMessageBox(),'Successful','Đã thêm thành công')
                self.taoThuMuc(mssv)
                self.clearData()
                self.LoadData()
            except Exception:
                QMessageBox.information(QMessageBox(),'Unsuccessful','bi loi')
        else:
            QMessageBox.information(QMessageBox(),'Unsuccessful','Ban chua nhap thong tin')
import Source_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    From = QtWidgets.QWidget()
    ui = Ui_From()
    ui.setupUi(From)
    From.show()
    sys.exit(app.exec_())
