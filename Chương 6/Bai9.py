import math


# Hàm kiểm tra số nguyên tố
def snt(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


# Nhập mảng
n = int(input("Nhập số lượng phần tử của mảng: "))
M = []
for i in range(n):
    x = int(input(f"Nhập M[{i}]: "))
    M.append(x)

# Tách số lẻ và số chẵn
so_le = [x for x in M if x % 2 != 0]
so_chan = [x for x in M if x % 2 == 0]

# Tách số nguyên tố và không nguyên tố
so_nguyen_to = [x for x in M if snt(x)]
khong_so_nguyen_to = [x for x in M if not snt(x)]

# Xuất kết quả
print("- Số lẻ:", so_le, "=> Tổng cộng:", len(so_le))
print("- Số chẵn:", so_chan, "=> Tổng cộng:", len(so_chan))
print("- Số nguyên tố:", so_nguyen_to)
print("- Không phải số nguyên tố:", khong_so_nguyen_to)
