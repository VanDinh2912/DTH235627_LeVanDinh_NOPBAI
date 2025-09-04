import math
import Ngay_Chuan


#Bai1
def tinh_lai_kep(X, Lai, Thang, TienTang):
    ChuKy = Thang // TienTang
    # Tien = X + X * Lai * TienTang * ChuKy
    Tien = X * ((1 + Lai * TienTang) ** ChuKy)
    return Tien


#Bai2
def tinh_toan(a, b, op):

    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        if b != 0:
            return round(a / b, 2)  # làm tròn 2 chữ số thập phân
        else:
            return "Lỗi: Không thể chia cho 0!"
    else:
        return "Ký tự nhập không hợp lệ!"
    
#Bai3

def dien_tich(r):

    return math.pi * (r ** 2)

#Bai4
def la_nam_nhuan(nam):

    return (nam % 400 == 0) or (nam % 4 == 0 and nam % 100 != 0)

def so_ngay_trong_thang(thang, nam):

    if thang in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif thang in [4, 6, 9, 11]:
        return 30
    elif thang == 2:
        return 29 if la_nam_nhuan(nam) else 28
    else:
        return None
    

#Bai5
def doc_so(n):
   
    
    Hang_don_vi = ["không", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]
    Hang_chuc = ["", "Mười", "Hai mươi", "Ba mươi", "Bốn mươi", "Năm mươi", "Sáu mươi", "Bảy mươi", "Tám mươi", "Chín mươi"]

    if n < 10:
        Hang_don_vi = ["Không", "Một", "Hai", "Ba", "Bốn", "Năm", "Sáu", "Bảy", "Tám", "Chín"]
        return Hang_don_vi[n]   
    else:
        chuc = n // 10
        don_vi = n % 10
        if don_vi == 0:
            return Hang_chuc[chuc]
        elif chuc == 1:
            return Hang_chuc[chuc] + " " + Hang_don_vi[don_vi]
        else:
            return Hang_chuc[chuc] + " " + Hang_don_vi[don_vi]
        

#Bai6
def giai_pt_bac2(a, b, c):
    if a == 0:          #1
        if b == 0 :     #2
            if c == 0:  #3
                return "Phương trình có vô số nghiệm."
            else:
                return "Phương trình vô nghiệm."
        else:
            return f"Phương trình có 1 nghiệm: x = {-c / b}"
    
    #delta
    delta = b**2 - 4*a*c
    
    if delta < 0:
        return "Phương trình vô nghiệm."
    elif delta == 0:
        x = -b / (2*a)
        return f"Phương trình có nghiệm kép: x = {x}"
    else:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        return f"Phương trình có 2 nghiệm phân biệt: x1 = {x1}, x2 = {x2}"
        
#Bai7 chưa rõ đề bài, giả sử n là một chữ số 0-9 ( n + n*2 + n*3 )

def tinh_tong(n):
    if 0 <= n <= 9:
        return n + n*2+ n*3
    else:
        return "n phải là một chữ số từ 0 đến 9"
    
#Bai8
def bang_cuu_chuong(n):
        bang = 0
        for i in range(1, 11):
            bang = n * i
            print(f"{n} x {i} = {bang}")

#Bai9

def Tong_1(n): # S = 1 + 2 + ... + n
        tong = 0
        for i in range(1, n+1):
            tong += i
        return tong
def Tong_2(n): # S = 1 + 2 + ... + 2n -1
        tong = 0
        s = 2*n - 1
        for i in range(1,s+1):
            if i % 2 != 0:
                tong += (2*i - 1)
        return tong
def Tong_3(n): # # S = 2 + 4 + ... + 2n
        tong = 0
        s = 2*n 
        for i in range(1,s+1):
            if i % 2 == 0:
                tong += i
        return tong
def Tong_4(n): # S = 1*2 + 2*2 + ... + n*2
    tong = 0
    for i in range(1, n+1):
            tong += i**2
    return tong
def Tong_5(n): # S = 1/1 + 1/2 + ... + 1/n
    tong = 0
    for i in range(1, n+1):
            tong += 1/i
    return tong

#Bai10
def in_bang_cuu_chuong():
    for i in range(2, 10):
        print(f"Bảng cửu chương của {i}:")  
        for j in range(1, 11):
            print(f"{i} x {j} = {i*j}")

#Bai11
def tinh_day_so(x,n):
    s= 0 
    GT = 1 
    for i in range(1,n+1):
        GT *= i
        s += (x**i)/GT
    return s

#Bai12
def chuyen_np(n): 
    return bin(n)

#Bai13
#Bai14 
def ngay_ve(di, so_ngay):
    
    D = ["Thứ 2", "Thứ 3", "Thứ 4", "Thứ 5", "Thứ 6", "Thứ 7", "Chủ nhật"]
    
    di = Ngay_Chuan.chuan_ngay(di) 
    if di is None:
        return None  
    else:
        ngay_di = D.index(di)
        ngay_ve = (ngay_di + so_ngay) % 7
    return D[ngay_ve]

#Bai15
def kiem_tra_tam_giac(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return False
    if a + b > c and a + c > b and b + c > a:
            return True
    else:
            return False
    
#Bai16
def nam_nhuan(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def kiem_tra_ngay(day, month, year):
    if year < 1:
        return False
    if month < 1 or month > 12:
        return False
    so_ngay_thang = [31,28,31,30,31,30,31,31,30,31,30,31]
    max_day = so_ngay_thang[month-1]
    if month == 2 and nam_nhuan(year):
        max_day = 29
    if day < 1 or day > max_day:
        return False
    return True

#Bai17 = Bai9
def Tong_so_N(n):
    tong = 0
    s = 2*n
    for i in range(1, s+1):
        tong += i
    return tong
def Tong_so_N_le(n):
    tong = 0
    for i in range(1, n+1):
        if i % 2 != 0:
            tong += i
    return tong
def Tong_so_N_chan(n):
    tong = 0
    for i in range(1, n+1):
        if i % 2 == 0:
            tong += i
    return tong 
    
#Bai18
def tinh_uoc_so(n):
    uoc_so = []
    for i in range(1, n + 1):
        if n % i == 0:
            uoc_so.append(i)
    return uoc_so
def tinh_tong_uoc_so(n):
    s = 0 
    uoc_so = []
    for i in range(1, n ):
        if n % i == 0:
            s += i
    return s
def Tinh_Tong_N(n):
    s = 0 
    for i in range(12, n + 1,10 ):
         s += i
    return s

#Bai19
def tong_tu_mot_den_n(n):
    tong = 0
    for i in range(1, n + 1):
        tong += i
    return tong
def nt_cungnhau(m,n):
     return math.gcd(m, n) == 1
def doi_giay(s):
    gio = s // 3600
    s %= 3600
    phut = s // 60
    giay = s % 60
    return f"{gio} giờ {phut} phút {giay} giây"
def tri_tuyet_doi(a, b):
    return abs(a - b)

#Bai20

def la_nguyen_to(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True
def f(m, n):
    ucln = math.gcd(m, n)
    key = 0
    for i in range(2, ucln + 1):
        if m % i == 0 and n % i == 0 and la_nguyen_to(i):
            key = i
    return key
    return 0
