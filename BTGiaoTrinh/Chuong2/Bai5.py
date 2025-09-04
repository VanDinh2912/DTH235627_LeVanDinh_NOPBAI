import Ham
n = int(input("Nhập số nguyên dương n: "))
if n < 0 or n > 99:
      print(n,"không hợp lệ!")
else:
    print("Chữ số cua n là:", Ham.doc_so(n))
