
import math
while True:
    a_str = input("Nhập tọa độ A (dạng A(x,y)): ").replace(" ", "").strip().upper()
    b_str = input("Nhập tọa độ B (dạng B(x,y)): ").replace(" ", "").strip().upper()
    if a_str[0] != "A" or b_str[0] !='B':
        print("Sai ten toa do ! Nhap lai :",False )
    else:
        break
def tach_toa_do(s):
    s = s.replace("A", "").replace("B", "").replace("(", "").replace(")", "")
    x_str, y_str = s.split(",")
    
    return float(x_str), float(y_str)

xA, yA = tach_toa_do(a_str)
xB, yB = tach_toa_do(b_str)


dAB = math.sqrt((xB - xA) ** 2 + (yB - yA) ** 2)
print(f"Khoảng cách |AB| = {dAB:.2f}")
