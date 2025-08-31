import Ham
n = int(input("Nhập n (n>0): "))
if n <= 0:
    print(f"{n} không phải là số nguyên dương")
else:
    print("Tổng 3 dãy số là:")
    print("1. S = 1 + 2 + ... + 2n =", Ham.Tong_so_N(n))
    print("2. S = 2 + 4 + ... + n  =", Ham.Tong_so_N_chan(n))
    print("3. S = 1 + 3 + ... + n =", Ham.Tong_so_N_le(n))