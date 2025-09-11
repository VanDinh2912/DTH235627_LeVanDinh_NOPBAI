from math import sqrt

print("Chương trình tính diện tích Tam Giác")

while True:
    try:
        a = float(input("Nhập cạnh a>0: "))
        b = float(input("Nhập cạnh b>0: "))
        c = float(input("Nhập cạnh c>0: "))

        if (a > 0 and b > 0 and c > 0) and (a + b > c and a + c > b and b + c > a):
            break
        else:
            print("Lỗi cú pháp, nhập lại :")
    except:
        print("Lỗi cú pháp, nhập lại :")

if (a <= 0 or b <= 0 or c <= 0) or (a + b) <= c or (a + c) <= b or b + c <= a:
    print("Tam giác không hợp lệ")
else:
    cv = a + b + c
    p = cv / 2
    dt = sqrt(p * (p - a) * (p - b) * (p - c))
    print("Diện tích =", dt)
