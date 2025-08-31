import Ham 

day = int(input("Nhập ngày: "))
month = int(input("Nhập tháng: "))
year = int(input("Nhập năm: "))

if Ham.kiem_tra_ngay(day, month, year):
    print(f"Ngày hợp lệ: {day}/{month}/{year}")
else:
    print("Ngày tháng năm không hợp lệ")
