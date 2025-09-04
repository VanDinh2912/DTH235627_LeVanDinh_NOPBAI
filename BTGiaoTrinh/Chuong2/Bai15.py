
import Ham

inp = input("Nhập 3 số dương a,b,c cách nhau bằng dấu phẩy: ")

try:
    a_str, b_str, c_str = inp.split(",")
    a, b, c = float(a_str), float(b_str), float(c_str)
    
    # Gọi hàm kiểm tra
    if Ham.kiem_tra_tam_giac(a, b, c):
        print("Có thể tạo thành một tam giác")
    else:
        print("Không thể tạo thành một tam giác")
except ValueError:
    print("Vui lòng nhập đúng 3 số, cách nhau bằng dấu phẩy")
