# Hàm nhập ma trận
def nhap_ma_tran(m, n, ten="A"):
    print(f"Nhập ma trận {ten} ({m}x{n}):")
    M = []
    for i in range(m):
        row = []
        for j in range(n):
            x = int(input(f"{ten}[{i}][{j}] = "))
            row.append(x)
        M.append(row)
    return M


# Hàm in ma trận
def xuat_ma_tran(M, ten="Matrix"):
    print(f"{ten}:")
    for row in M:
        print(row)


# Hàm cộng 2 ma trận
def cong_ma_tran(A, B):
    m, n = len(A), len(A[0])
    C = [[A[i][j] + B[i][j] for j in range(n)] for i in range(m)]
    return C


# Hàm chuyển vị ma trận
def chuyen_vi(M):
    m, n = len(M), len(M[0])
    T = [[M[j][i] for j in range(m)] for i in range(n)]
    return T


# Hàm nhập kích thước hợp lệ
def nhap_kich_thuoc(ten="A"):
    while True:
        m = int(input(f"Nhập số hàng của {ten}: "))
        n = int(input(f"Nhập số cột của {ten}: "))
        if m > 0 and n > 0:
            return m, n
        else:
            print("Kích thước không hợp lệ (phải > 0). Vui lòng nhập lại!")


# --- Chương trình chính ---
# Nhập ma trận A
m1, n1 = nhap_kich_thuoc("A")
A = nhap_ma_tran(m1, n1, "A")

# Nhập ma trận B
m2, n2 = nhap_kich_thuoc("B")
B = nhap_ma_tran(m2, n2, "B")

# Kiểm tra đồng nhất
if m1 == m2 and n1 == n2:
    print("\nHai ma trận đồng nhất, tiến hành cộng và hoán vị:")
    xuat_ma_tran(A, "Ma trận A")
    xuat_ma_tran(B, "Ma trận B")

    # Cộng ma trận
    C = cong_ma_tran(A, B)
    xuat_ma_tran(C, "A + B")

    # Chuyển vị
    AT = chuyen_vi(A)
    BT = chuyen_vi(B)
    xuat_ma_tran(AT, "A^T (chuyển vị A)")
    xuat_ma_tran(BT, "B^T (chuyển vị B)")
else:
    print("\nKhông thể cộng hoặc hoán vị hai ma trận vì khác kích thước:")
    xuat_ma_tran(A, "Ma trận A")
    xuat_ma_tran(B, "Ma trận B")
