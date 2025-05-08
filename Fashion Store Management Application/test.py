from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QApplication, QMainWindow
import sys
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QMessageBox


import warnings
warnings.simplefilter("ignore", DeprecationWarning)

# kết nối với database
import mysql.connector
def connect():
    try:
        conn = mysql.connector.connect(
            host='127.0.0.1',
            user='root',      
            password='2004',      
            database='dangnhap'  
        )
        return conn
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None


# Cửa sổ đăng nhập
class Login_w(QMainWindow):
    def __init__(self):
        super(Login_w, self).__init__()
        uic.loadUi("dangnhap.ui", self)  
        self.btndangky.clicked.connect(self.go_to_register)  
        self.btndangnhap.clicked.connect(self.login)  

    def login(self):
        un = self.txtdangnhap.text()
        password = self.txtmk.text()

        if not un or not password:
            QMessageBox.warning(self, "Lỗi", "Vui lòng nhập đầy đủ thông tin!")
            return

        db = connect()
        query = db.cursor()
        query.execute("SELECT * FROM admins WHERE ten=%s AND matkhau=%s", (un, password))
        ktra = query.fetchone()

        if ktra:
            QMessageBox.information(self, "Đăng Nhập", "Đăng nhập thành công!")
            widget.setCurrentWidget(Menu_form)
            widget.resize(780, 510)  # Đổi kích thước phù hợp với menu
        else:
            QMessageBox.warning(self, "Đăng Nhập", "Sai thông tin đăng nhập!")

        query.close()
        db.close()

    def go_to_register(self):
        # chuyển về form đăng ký
        widget.setCurrentWidget(Res_form)

    def __init__(self):
        super(Login_w, self).__init__()
        uic.loadUi("dangnhap.ui", self)  # Load giao diện
        self.btndangky.clicked.connect(self.go_to_register)  # Gọi hàm chuyển sang đăng ký
        # sự kiện khi click vào buton đăng nhập để nó đăng nhập
        self.btndangnhap.clicked.connect(self.login)
        # set kiểu chữ là cỡ chữ
        # thiết lập cỡ chữ và kiểu chữ
        # định nghĩa font 
        font = QFont()
        font1 = QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font1.setPointSize(14)
        # cho lên thành chữ in đậm 
        font.setBold(True)
        font1.setBold(True)
        # set chữ in đậm phần lbl đăng nhập thành chữ đậm
        self.lbldangnhap.setFont(font)
        # set in đậm phần lbl mật khẩu thành chữ in đậm
        self.lblmatkhau.setFont(font)
        # set in đậm chữ trong nút button 
        self.btndangky.setFont(font)
        # set in đậm phần chữ trong nut button
        self.btndangnhap.setFont(font)
        self.label.setFont(font1)
# xử lý kết đăng nhập
    def login(self):
        # lấy dữ liệu từ ô txt 
        un = self.txtdangnhap.text()
        password = self.txtmk.text()
        if not un or not password:
            QMessageBox.warning(self, "Lỗi", "Vui lòng nhập đầy đủ thông tin!")
            return

        # kết nối với database 
        db = connect()
        query = db.cursor()
        # truy vấn vào database
        query.execute("select * from admins where ten= '" +un+"' and matkhau= '" +password+"' ")
        ktra = query.fetchone()
        if ktra:
            QMessageBox.information(self,"Đăng Nhập","Đăng Nhập thành công!")
            widget.resize(780,510)
            widget.setCurrentWidget(Menu_form) 
            self.txtdangnhap.clear()
            self.txtmk.clear()
        else:
            QMessageBox.information(self, "Đăng Nhập","Lỗi!")
            
        # Đóng kết nối database
        query.close()
        db.close()
# Chuyển qua form đăng ký
    def go_to_register(self):
        widget.setCurrentWidget(Res_form) 
# Cửa sổ đăng ký
class Reg_w(QMainWindow):
    def __init__(self):
        super(Reg_w, self).__init__()
        uic.loadUi("dangky.ui", self)  # Load giao diện
        self.btndangnhap.clicked.connect(self.go_to_login)  # Chuyển lại form đăng nhập
        self.btnnguoidung.clicked.connect(self.go_to_users) # Chuyển sang form user
        self.btndangky.clicked.connect(self.res)
        # set kiểu chữ là cỡ chữ
        # thiết lập cỡ chữ và kiểu chữ
        # định nghĩa font 
        font = QFont()
        font1 = QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font1.setPointSize(14)
        # cho lên thành chữ in đậm 
        font.setBold(True)
        font1.setBold(True)
        # set chữ in đậm phần lbl đăng nhập thành chữ đậm
        self.tendangnhap.setFont(font)
        # set in đậm phần lbl mật khẩu thành chữ in đậm
        self.matkhau.setFont(font)
        # set in đậm chữ trong nút button 
        self.btndangky.setFont(font)
        # set in đậm phần chữ trong nut button
        self.btndangnhap.setFont(font)
        self.label.setFont(font1)
        self.btnnguoidung.setFont(font)
# xử lý form đăng ký
    def res(self):
        dangky = self.txtdky.text()
        matkhau = self.txtmk.text()
        # kiểm tra đầy đủ thông tin
        if not dangky or not matkhau:
            QMessageBox.warning(self, "Lỗi", "Vui lòng nhập đầy đủ thông tin!")
            return

        db = connect()
        if db is None:
            QMessageBox.critical(self, "Lỗi", "Không thể kết nối database!")
            return

        try:
            query = db.cursor()
            query.execute("INSERT INTO users (ten, pasword) VALUES (%s, %s)", (dangky, matkhau))
            db.commit()  # Lưu thay đổi

            QMessageBox.information(self, "Đăng Ký", "Đăng Ký thành công")
            # xóa nội dung ô nhập
            self.txtdky.clear()
            self.txtmk.clear()
        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Lỗi", f"Lỗi khi đăng ký: {err}")
        finally:
            query.close()
            db.close()

# Quay lại form đăng nhập
    def go_to_login(self):
        widget.setCurrentWidget(Login_form) 
 
# Quay lại form Đăng ký
    def go_to_users(self):
        widget.setCurrentWidget(User_form)
# Cửa sổ User
class users(QMainWindow):
    def __init__(self):
        super(users, self).__init__()
        uic.loadUi("tknguoidung.ui",self) # Load giao diện
        self.btnquaylai.clicked.connect(self.go_to_registesr)
        self.btndangnhap.clicked.connect(self.login_user) 
        font = QFont()
        font1 = QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font1.setPointSize(14)
        # cho lên thành chữ in đậm 
        font.setBold(True)
        font1.setBold(True)
        # set chữ in đậm phần lbl đăng nhập thành chữ đậm
        self.tendangnhap.setFont(font)
        # set in đậm phần lbl mật khẩu thành chữ in đậm
        self.matkhau.setFont(font)
        # set in đậm chữ trong nút button 
        self.btnquaylai.setFont(font)
        # set in đậm phần chữ trong nut button
        self.btndangnhap.setFont(font)
        self.label.setFont(font1)
# logic form đăng nhập dưới dạng người dùng 
    def login_user(self):
        tendangnhap = self.txtdky.text()
        matkhau = self.txtmk.text()
        if not tendangnhap or not matkhau:
            QMessageBox.warning(self, "Lỗi", "Vui lòng nhập đầy đủ thông tin!")
            return

        db = connect()
        query = db.cursor()
        query.execute("select * from users where ten= '" +tendangnhap+"' and pasword= '" +matkhau+"' ")
        ktra = query.fetchone()
        if ktra:
            QMessageBox.information(self, "Đăng Nhập","Đăng Nhập thành công!")
            widget.setCurrentWidget(Menu_form) 
            query.fetchall()
        else: 
            QMessageBox.information(self, "Đăng Nhập")
        query.close()
        db.close()
    def go_to_registesr(self):
        widget.setCurrentWidget(Res_form)

# CỬA SỔ MENU ĐĂNG NHẬP
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
        # chuyển về form đăng xuất khi bấm đăng xuất
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
        # ẩn hết fream
        

    def go_to_res(self):
        widget.resize(460, 400)  # Thay đổi kích thước trước khi chuyển form
        widget.setCurrentWidget(Res_form)
        
  

# CỬA SỔ SẢN PHẨM
class SanPham(QMainWindow):
    def __init__(self):
        super(SanPham, self).__init__()
        uic.loadUi("sanpham.ui", self)








# Xử lý ứng dụng
# Xử lý ứng dụng
app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()

# Khởi tạo các form
Login_form = Login_w()
Res_form = Reg_w()
Menu_form = Menu_w()
User_form = users()
San_Pham = SanPham()

# Thêm các form vào QStackedWidget
widget.addWidget(Login_form)
widget.addWidget(Res_form)
widget.addWidget(Menu_form)
widget.addWidget(User_form)
widget.addWidget(San_Pham)

# Đặt cửa sổ mặc định khi chạy
widget.setCurrentWidget(Menu_form)  # Nếu muốn hiện form đăng nhập trước

# Hiển thị giao diện
widget.setWindowTitle("Ứng dụng Quản lý")  # Đặt tiêu đề cửa sổ
widget.resize(460, 400)
widget.show()

# Chạy chương trình
sys.exit(app.exec())

