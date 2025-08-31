import Ham
n = int(input("Nhập n: "))
x = float(input("Nhập x: "))
if n < 1 or x < 0:
     print(f"{n} hoặc {x} không hợp lệ")
else:
    print(f"Giá trị của dãy số là: {Ham.tinh_day_so(x,n)}")