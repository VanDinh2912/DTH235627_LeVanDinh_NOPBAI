import Ham
X = float(input("Nhập số tiền gốc: "))
L = float(input("Nhập lãi suất (theo tháng): "))    
Thang = int(input("Nhập số tháng đã gửi: "))
Lup = int(input("Nhập số tháng cộng dồn lãi vào gốc: "))
Tien = Ham.tinh_lai_kep(X, L, Thang, Lup)
print("Tổng số tiền sau", Thang, "tháng là:", round(Tien, 2))