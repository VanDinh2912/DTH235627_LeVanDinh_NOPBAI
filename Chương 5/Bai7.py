def ToiUuChuoiDanhTu(s: str):
    words = s.strip().split()
    words = [w.capitalize() for w in words]
    return " ".join(words)


s = input("Nhập vào một chuỗi:")
print(ToiUuChuoiDanhTu(s))
