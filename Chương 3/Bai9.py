month = int(input("Nhập tháng (1-12): "))
if month < 1 or month > 12:
    print("Tháng không hợp lệ!")
else:
    if month <= 3:
        q = 1
    elif month <= 6:
        q = 2
    elif month <= 9:
        q = 3
    else:
        q = 4

    print(f"Tháng {month} thuộc quý {q} trong năm.")