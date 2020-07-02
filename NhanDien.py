import cv2
import numpy as np
import pickle
from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import uic
import sys
import dlib

class UI_NhanDien(QMainWindow):

    def __init__(self, name):
        super(UI_NhanDien,self).__init__()
        uic.loadUi("form3.ui",self)
        self.path =  name
        print(self.path)
        self.btnXuat = self.findChild(QPushButton,"btnXuat")
        self.btnKetThuc = self.findChild(QPushButton,"btnDangNhap_3")
        self.btnLamMoi = self.findChild(QPushButton,"btnLamMoi")
        self.Danhsach = self.findChild(QTableWidget,"DSdiemdanh")
        self.ThoiGian = self.findChild(QLabel,"lbthoigian")
        self.NgayThang = self.findChild(QLabel,"lbngaythang")
        self.lbten = self.findChild(QLabel,"lbtensinhvien")
        self.lbmssv = self.findChild(QLabel,"lbmasinhvien")
        self.lbtrangthai = self.findChild(QLabel,"label_4")

        self.ThoiGian.setText(QTime.currentTime().toString())
        self.NgayThang.setText(QDate.currentDate().toString(Qt.DefaultLocaleShortDate))

        self.btnXuat.clicked.connect(self.XuatEX)
        self.btnLamMoi.clicked.connect(self.LamMoi)
        self.btnKetThuc.clicked.connect(self.NhanDienKhuonMat)

    def XuatEX(self):
        try:
            conn = sqlite3.connect('Database\SinhVien.db')
            result = conn.execute("Select mssv,hoten,lop,gioitinh,monhoc,trangthai From SinhVien")
            for row_number, row_data in enumerate(result):
                self.Danhsach.insertRow(row_number)
                for column_number, data in  enumerate(row_data):
                    self.Danhsach.setItem(row_number,column_number, QtWidgets.QTableWidgetItem(str(data)))
        except Exception:
            print("Loi")
    def LamMoi(self):
        self.XoaDS()
        try:
            conn = sqlite3.connect('Database\SinhVien.db')
            conn.execute("Update SinhVien set trangthai = 0")
            conn.commit()
        except Exception:
            print("Loi")

    def NhanDienKhuonMat(self):
        p = self.path +".yml"
        print(p) 
        detector = dlib.get_frontal_face_detector()
        recognizer = cv2.face.LBPHFaceRecognizer_create()
        recognizer.read(self.path+".yml")
        labels={"person_name": 1}
        with open("labels.pickle", 'rb') as f:
            og_labels = pickle.load(f)
            labels = {v:k for k,v in og_labels.items()}
        cap = cv2.VideoCapture(0)
        f = 0
        i = 0
        maso=[]
        while(True):
            ret, frame = cap.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
            faces = detector(gray)
            f=0
            for face in faces:
                f = 0
                x1 = face.left()
                y1 = face.top()
                x2 = face.right()
                y2 = face.bottom()
                roi_gray = gray[y1:y2,x1:x2]  
                roi_color = frame[y1:y2,x1:x2]  
                stroke = 2
                color = (255, 0 , 0)
                id_,conf = recognizer.predict(roi_gray)
                if conf>=45 and conf<=85:
                        color = (255, 255 , 255)
                        a = str(labels[id_]).split(".")
                        a[0] = int(a[0])*-1
                        try:
                            conn = sqlite3.connect('Database\SinhVien.db')
                            check = conn.execute("SELECT trangthai FROM SinhVien where mssv ="+str(a[0]))
                            conn.commit()
                            for row, data in enumerate(check):
                                checkTrangThai = data[0]
                            if checkTrangThai != 1:
                                conn.execute("Update SinhVien set trangthai = 1 where mssv="+str(a[0]))
                                conn.commit()
                                result = conn.execute("select mssv,hoten,lop,gioitinh,monhoc,trangthai from SinhVien where mssv="+str(a[0]))
                                conn.commit()
                                for row_number, row_data in enumerate(result):
                                    self.Danhsach.insertRow(row_number)
                                    for column_number, data in enumerate(row_data):
                                        self.Danhsach.setItem(row_number, column_number, QTableWidgetItem(str(data)))
                                        self.Danhsach.setItem(row_number,5,QTableWidgetItem("Có mặt"))
                                

                                print("Da them")
                            else:
                                print("Da ton tai")
                            conn.close()
                        except Exception:
                            print("Loi")
                        
                        font = cv2.FONT_HERSHEY_SIMPLEX
                        name = ("Name: " + str(a[1]))
                        stroke = 2
                        color = (255,100,0)
                        cv2.putText(frame, name, (x1,y1),font,1,color,stroke,cv2.LINE_AA)
                else:
                    font = cv2.FONT_HERSHEY_SIMPLEX
                    name = ("UNKNOWN")
                    stroke = 2
                    color = (255,100,0)
                    cv2.putText(frame, name, (x1,y1),font,1,color,stroke,cv2.LINE_AA)
                cv2.rectangle(frame, (x1,y1), (x2,y2), color, stroke)
            
            if cv2.waitKey(20) & 0xFF == ord('q') or f==1:
                break
            cv2.imshow('Quet khuon mat',frame)
        cap.release()
        cv2.destroyAllWindows()
    def ThemVaoDanhSach(self):
        try:
            conn = sqlite3.connect('Database\SinhVien.db')
            result = conn.execute("Select mssv,hoten,lop,gioitinh,monhoc,trangthai from SinhVien")
            for row_number, row_data in enumerate(result):
                self.Danhsach.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.Danhsach.setItem(row_number, column_number, QTableWidgetItem(str(data)))
            conn.close()
        except Exception:
            print("LOI")
    def XoaDS(self):
        self.Danhsach.clearSelection()
        while (self.Danhsach.rowCount()) > 0:
            self.Danhsach.removeRow(0)
            self.Danhsach.clearSelection()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    UIwindow = UI_NhanDien()
    UIwindow.show()
    sys.exit(app.exec_())