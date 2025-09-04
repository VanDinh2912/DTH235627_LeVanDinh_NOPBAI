
so_ngay_thang = [31,28,31,30,31,30,31,31,30,31,30,31]
month = int(input("Nhập tháng: "))

if month == 2:
    year = int(input("Nhập năm: "))
    if year < 0:
        print("Năm không hợp lệ")
        exit()
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        max_day = 29
    else:
        max_day = 28
else:
    max_day = so_ngay_thang[month-1]
print(f"Tháng {month} có {max_day} ngày")