import Ham
n = int(input("Nhập n (0-9): "))
if n < 1 or n > 9:
     print(f"{n} không phải là một chữ số từ 1 đến 9")
else:
    print(f"Bảng cửu chương của {n} là:")
    Ham.bang_cuu_chuong(n)