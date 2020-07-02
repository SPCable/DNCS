from PyQt5 import *
from FormMain import *
import Source_rc
from PyQt5.QtGui import QIcon


class Ui_Form(object):

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(850, 450)
        Form.setWindowTitle("Phần mềm điểm danh by @team2")
        Form.setWindowIcon(QIcon('Images\Icon.png'))
        self.Background = QtWidgets.QLabel(Form)
        self.Background.setGeometry(QtCore.QRect(90, 0, 850, 450))
        self.Background.setText("")
        self.Background.setPixmap(QtGui.QPixmap(":/newPrefix/Images/background.jpg"))
        self.Background.setObjectName("Background")
        self.LogoQA = QtWidgets.QLabel(Form)
        self.LogoQA.setGeometry(QtCore.QRect(0, 0, 434, 451))
        self.LogoQA.setText("")
        self.LogoQA.setPixmap(QtGui.QPixmap(":/newPrefix/Images/face_detection@2x.png"))
        self.LogoQA.setScaledContents(True)
        self.LogoQA.setObjectName("LogoQA")
        self.Logo_Hutech = QtWidgets.QLabel(Form)
        self.Logo_Hutech.setGeometry(QtCore.QRect(495, 0, 321, 103))
        self.Logo_Hutech.setText("")
        self.Logo_Hutech.setPixmap(QtGui.QPixmap(":/newPrefix/Images/Logo_Hutech.jpg"))
        self.Logo_Hutech.setObjectName("Logo_Hutech")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(541, 158, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Sitka Banner")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: white;")
        self.label_4.setObjectName("label_4")
        self.label_4.setText("Tài khoản: ")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(541, 209, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Sitka Banner")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: white;")
        self.label_5.setObjectName("label_5")
        self.label_5.setText("Mật khẩu: ")
        self.txtAcc = QtWidgets.QLineEdit(Form)
        self.txtAcc.setGeometry(QtCore.QRect(548, 179, 214, 30))
        self.txtAcc.setObjectName("txtAcc")
        self.txtPass = QtWidgets.QLineEdit(Form)
        self.txtPass.setGeometry(QtCore.QRect(548, 230, 214, 30))
        self.txtPass.setObjectName("txtPass")
        self.txtPass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.btnDangNhap = QtWidgets.QPushButton(Form)
        self.btnDangNhap.setGeometry(QtCore.QRect(575, 309, 160, 50))
        self.btnDangNhap.setText("Đăng Nhập")

        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btnDangNhap.setFont(font)
        self.btnDangNhap.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnDangNhap.setStyleSheet("background:#371f57; color: white;")
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.btnDangNhap.clicked.connect(self.Login)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Phần mềm điểm danh by@team2"))
        self.label_4.setText(_translate("Form", "Tài khoản:"))
        self.label_5.setText(_translate("Form", "Mật khẩu:"))
        self.btnDangNhap.setText(_translate("Form", "Đăng nhập"))


    def Login(self):
        if (self.txtAcc.text() == "admin"):
            self.FormMain = QtWidgets.QMainWindow()
            self.ui = Ui_Main()
            self.ui.setup(self.FormMain)
            self.FormMain.show()
            FormLogin.hide()
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Đăng nhập")
            msg.setText("Không Thành công")
            msg.setStandardButtons(QMessageBox.Ok)
            x=msg.exec_()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FormLogin = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(FormLogin)
    FormLogin.show()
    sys.exit(app.exec_())
