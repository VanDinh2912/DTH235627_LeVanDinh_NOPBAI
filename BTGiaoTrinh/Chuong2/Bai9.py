import Ham
n = int(input("Nhập n : "))
if n < 1 :
     print(f"{n} không hợp lệ")
else:
    print(f"Tổng 1 + 2 + ... + {n} là: {Ham.Tong_1(n)}")
    print(f"Tổng 1 + 3 + ... + {2*n-1} là: {Ham.Tong_2(n)}")
    print(f"Tổng 2 + 4 + ... + {2*n} là: {Ham.Tong_3(n)}")
    print(f"Tổng 2*1 + 2*2 + ... + 2*{n} là: {Ham.Tong_4(n)}")
    print(f"Tổng 1/1 + 1/2 + ... + 1/{n} là: {Ham.Tong_5(n)}")