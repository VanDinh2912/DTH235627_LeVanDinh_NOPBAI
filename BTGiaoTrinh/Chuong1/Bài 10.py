so_sao = [1, 3, 7, 3, 5, 11, 2, 2]
chieu_rong = max(so_sao)  
for n in so_sao:
    khoang_trang = (chieu_rong - n) // 2
    print(" " * khoang_trang + "*" * n)