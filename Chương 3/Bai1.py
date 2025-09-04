n = int(input("Nhập vào một năm bất kì  : "))
if n < 0:
    print("Vui lòng nhập số nguyên dương.") 
else:
    if (n % 4 ==0 and n % 100 != 0) or n % 400 == 0:
        print("Năm", n, "là năm nhuần")
    else:
        print("Năm", n, "không nhuần") 