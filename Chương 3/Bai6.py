try:
    n = int(input("Nhập số nguyên dương n (0 <= n < 100): "))
    if n < 0 or n >= 100:
        print("Số không hợp lệ!")
    else:
        Hang_don_vi = ["", "một", "hai", "ba", "bốn", "lăm", "sáu", "bảy", "tám", "chín"]
        Hang_chuc = ["", "Mười", "Hai mươi", "Ba mươi", "Bốn mươi", "Năm mươi", "Sáu mươi", "Bảy mươi", "Tám mươi", "Chín mươi"]

        if n < 10:
            Hang_don_vi = ["Không", "Một", "Hai", "Ba", "Bốn", "Năm", "Sáu", "Bảy", "Tám", "Chín"]
            print(Hang_don_vi[n])  
        else:
            chuc = n // 10
            don_vi = n % 10
            if don_vi == 0:
                print(Hang_chuc[chuc])
            elif chuc == 1:
                print(Hang_chuc[chuc] + " " + Hang_don_vi[don_vi])
            else:
                print(Hang_chuc[chuc] + " " + Hang_don_vi[don_vi])
except ValueError:
    print("Vui lòng nhập một số nguyên hợp lệ.")