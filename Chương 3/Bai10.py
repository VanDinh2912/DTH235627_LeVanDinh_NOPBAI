n = int(input("Nhập n: "))
x = float(input("Nhập x: "))
if n < 1 or x < 0:
     print(f"{n} hoặc {x} không hợp lệ")
else:
    s= 0 
    GT = 1 
    for i in range(n+1):
        GT *= i
        s += (x**i)/GT
    print(f"Giá trị của dãy số là: {s}")