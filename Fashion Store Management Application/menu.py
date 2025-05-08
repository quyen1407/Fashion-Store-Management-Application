from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QApplication, QMainWindow
import sys
from PyQt6.QtGui import QFont
import warnings
warnings.simplefilter("ignore", DeprecationWarning)

# Cửa sổ menu
class Menu_w(QMainWindow):
    def __init__(self):
        super(Menu_w, self).__init__()  
        uic.loadUi("menu.ui", self)
        self.btndangxuat.clicked.connect(self.go_to_res)
        
        # Thiết lập font chữ
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)

        self.btnsanpham.setFont(font)
        self.btnkhohang.setFont(font)
        self.btnnhaphanphoi.setFont(font)
        self.btnkhachhang.setFont(font)
        self.btnnhanvien.setFont(font)
        self.btndangxuat.setFont(font)

    def go_to_res(self):
        """Chuyển về form đăng ký khi bấm đăng xuất"""
        widget.setCurrentWidget(Res_form)
        widget.resize(460, 400)  # Đặt lại kích thước phù hợp với form đăng ký

    def __init__(self):
        super(Menu_w, self).__init__()  
        uic.loadUi("menu.ui", self)
        self.btndangxuat.clicked.connect(self.go_to_res)
        
        # Thiết lập font chữ
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)

        self.btnsanpham.setFont(font)
        self.btnkhohang.setFont(font)
        self.btnnhaphanphoi.setFont(font)
        self.btnkhachhang.setFont(font)
        self.btnnhanvien.setFont(font)
        self.btndangxuat.setFont(font)

    def go_to_res(self):
        widget.resize(460, 400)  # Thay đổi kích thước trước khi chuyển form
        widget.setCurrentWidget(Res_form)
class Login_w(QMainWindow):
    def __init__(self):
        super(Login_w, self).__init__()
        uic.loadUi("dangnhap.ui", self)  

# Xử lý ứng dụng
app = QApplication(sys.argv)  # Khởi tạo QApplication trước khi tạo bất kỳ widget nào
widget = QtWidgets.QStackedWidget()

Menu_form = Menu_w()  # Chỉ tạo 1 instance duy nhất của Menu_w
Res_form = Login_w()

# Thêm Menu_form vào widget
widget.addWidget(Res_form)
widget.addWidget(Menu_form)

# Đặt cửa sổ mặc định khi chạy
widget.setCurrentWidget(Menu_form)
widget.resize(780, 510)  # Thiết lập kích thước ban đầu nhưng có thể thay đổi

# Hiển thị giao diện
widget.show()

# Thoát chương trình khi đóng ứng dụng
sys.exit(app.exec())
