<<<<<<< HEAD
# main.py
=======

>>>>>>> dev
import Ham
import Ngay_Chuan

di = input("Nhập ngày đi (ví dụ: hai, thứ hai,...): ")
di_chuan = Ngay_Chuan.chuan_ngay(di) 

if di_chuan is None:
    print(f"{di} không hợp lệ")
else:
    so_ngay = int(input("Nhập số ngày đi: "))
    if so_ngay < 1:
        print(f"{so_ngay} không hợp lệ")
    else:
        ngay_ve = Ham.ngay_ve(di, so_ngay)
        print("Ngày về:", ngay_ve)
