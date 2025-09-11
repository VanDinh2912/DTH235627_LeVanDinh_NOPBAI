import Ham
thang = int(input("Nhập tháng (1-12): "))
nam = 0; 
if thang == 2:
    nam = int(input("Nhập năm: "))
ngay = Ham.so_ngay_trong_thang(thang, nam)

if thang == 2:
        if Ham.la_nam_nhuan(nam):
           print(f"Số ngày trong tháng {thang} ( Nhuan ) năm {nam} là: {ngay} ngày" if ngay else "Tháng không hợp lệ!")
        else:
            print(f"Số ngày trong tháng {thang} (Khong nhuan ) năm {nam} là: {ngay} ngày" if ngay else "Tháng không hợp lệ!")       
else :
    print(f"Số ngày trong tháng {thang} là: {ngay} ngày" if ngay else "Tháng không hợp lệ!")
