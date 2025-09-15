def ChuHoa(chuoi):
    dem = 0
    for i in chuoi:
        if ord(i) <= 90 and ord(i) >= 65:
            dem += 1
    return dem


def ChuThuong(chuoi):
    dem = 0
    for i in chuoi:
        if ord(i) <= 122 and ord(i) >= 97:
            dem += 1
    return dem


chuoi = input("Nhập vào chuỗi :")
print("chu hoa:", ChuHoa(chuoi))
# ChuThuong(chuoi)
