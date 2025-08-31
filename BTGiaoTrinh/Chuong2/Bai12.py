import Ham
n = int(input("Nhập số thập phân : "))
if n < 1 :
     print(f"{n} không hợp lệ")
else:
    print("Số nhị phân la:",Ham.chuyen_np(n)[2:])