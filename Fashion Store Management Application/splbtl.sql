CREATE DATABASE dangnhap;
USE dangnhap;

-- database của addmin 
-- bảng admins 
CREATE TABLE admins (
    id INT AUTO_INCREMENT PRIMARY KEY,  
    ten NVARCHAR(255) NOT NULL,
    matkhau NVARCHAR(255) NOT NULL
);
insert into admins values(
(1,"quyen",123),
(2,"quynh",123)
);
-- bảng users 
CREATE TABLE users(
	id int  AUTO_INCREMENT PRIMARY KEY,
    ten nvarchar(255) not null,
    pasword nvarchar(255)
);
drop table taikhoan;
select * from users;

-- bảng nhân viên  
create table nhanvien(
	mavn int  AUTO_INCREMENT PRIMARY KEY,
    tennv nvarchar(255) not null,
    ngaysinhnv date,
    gioitinh nvarchar(255) not null,
    sodtnv int not null,
    emailnv nvarchar(255) not null,
    dcnv varchar(255) not null
);
select * from nhanvien;

-- Nhà Phân Phối
create table nhaphanphoi(
	manpp int  AUTO_INCREMENT PRIMARY KEY,
    tennpp nvarchar(255) not null,
    sdtnpp int,
    email nvarchar(255) not null,
    diachinpp nvarchar(255) not null
); 
select * from nhaphanphoi;

-- Sản Phẩm
create table sanpham(
	masp int auto_increment primary key,
    tensp nvarchar(255) not null,
    loaisp nvarchar(255) not null,
    trangthai nvarchar(255) not null,
    giatien DECIMAL(10,2),
    soluong int not null,
    manpp INT,
    FOREIGN KEY (manpp) REFERENCES nhaphanphoi(manpp)
); 
select * from sanpham;

-- khách hàng 
create table khachhang(
	makh int auto_increment primary key,
    tenkh nvarchar(255) not null,
    gioitinh nvarchar(255) not null,
    sdtkh int not null,
	email nvarchar(255) not null,
    diachi nvarchar(255) not null
); 
select * from khachhang;
select * from lichsugiaodich;
create table giohang(
	maspu int,
    tenspu nvarchar(255),
    loaispu nvarchar(255),
    giaspu decimal(10,2),
    slspu int
);
select * from lsgiaodich;
create table lsgiaodich(
	maspls int,
    tenspls nvarchar(255),
    loai nvarchar(255),
    gia decimal(10,2),
    sl int
);






