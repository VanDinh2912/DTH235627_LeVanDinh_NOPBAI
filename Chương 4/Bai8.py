import math

while True:
    try:
        a = float(input("Nhập cơ số a: "))
        x = float(input("Nhập số x: "))

        if a <= 0 or a == 1:
            print(" Cơ số a phải > 0 và khác 1. Nhập lại!")
            continue
        if x <= 0:
            print(" x phải > 0. Nhập lại!")
            continue

        result = math.log(x) / math.log(a)
        print(f"log_{a}({x}) = {result:.2f}")
        break

    except ValueError:
        print(" Vui lòng nhập số hợp lệ.")
