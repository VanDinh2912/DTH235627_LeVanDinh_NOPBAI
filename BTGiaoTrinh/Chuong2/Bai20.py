import Ham
n = int(input("Nhập n: "))
m = int(input("Nhập m: "))

if Ham.f(n, m):
    print("Số nguyên tố lớn nhất",Ham.f(n, m))
else:
    print(0) 