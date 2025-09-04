
day = int(input("Nhập ngày: "))
month = int(input("Nhập tháng: "))
year = int(input("Nhập năm: "))
if year < 0:
    print("Năm không hợp lệ!")
    exit()

days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if month < 1 or month > 12:
    print("Tháng không hợp lệ!")
    exit()
elif month == 2:
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) :
        max_day = 29
else:
    max_day = days_in_month[month]

if day != max_day and (day < 1 or day > max_day):
    print("Ngày không hợp lệ!")
    exit()
elif day < max_day:
    next_day = day + 1
    next_month = month
    next_year = year
else:  
    next_day = 1
    if month == 12: 
        next_month = 1
        next_year = year + 1
    else:
        next_month = month + 1
        next_year = year

print(f"Ngày kế tiếp là: {next_day}/{next_month}/{next_year}")
