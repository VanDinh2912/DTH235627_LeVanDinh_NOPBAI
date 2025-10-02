from random import randrange


# Tạo ma trận m x n ngẫu nhiên (0..99)
def TaoMaTran(m, n):
    return [[randrange(100) for _ in range(n)] for _ in range(m)]


# Xuất ma trận
def XuatMaTran(D):
    for row in D:
        print("\t".join(map(str, row)))


# Lấy dòng r
def LayDong(D, r):
    return D[r]


# Lấy cột c
def LayCot(D, c):
    return [row[c] for row in D]


# Xuất list 1 chiều
def XuatList1Chieu(L):
    print("\t".join(map(str, L)))


# Tìm max trong ma trận
def TimMax(D):
    return max(map(max, D))


# --- Main ---
m = int(input("Nhập số dòng: "))
n = int(input("Nhập số cột: "))

D = TaoMaTran(m, n)
print("Ma trận ngẫu nhiên:")
XuatMaTran(D)

r = int(input("Mời bạn nhập dòng muốn xuất: "))
print("Dòng", r, ":")
XuatList1Chieu(LayDong(D, r))

c = int(input("Mời bạn nhập cột muốn xuất: "))
print("\nCột", c, ":")
XuatList1Chieu(LayCot(D, c))

print("\nSố lớn nhất trong ma trận =", TimMax(D))
