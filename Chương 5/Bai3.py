def CheckPrime(x):
    dem = 0
    for i in range(1, x + 1):
        if x % i == 0:
            dem += 1
    return dem == 2


try:
    s = input("Nhập vào chuỗi (...;...) :")
    arr = s.split(";")
    sochan = 0
    soam = 0
    sont = 0
    sum = 0
    print("Các chữ số: ", end="")
    for x in arr:
        print("", x, end="")
        number = int(x)
        if number % 2 == 0:
            sochan += 1
        if number < 0:
            soam += 1
        if CheckPrime(number):
            sont += 1
        sum = sum + number
    print()
    print("Số chẵn =", sochan)
    print("Số âm =", soam)
    print("Số Nguyên tố =", sont)
    print("Trung bình=", sum / len(arr))
except:
    print("Nhập sai dữ liệu !")
