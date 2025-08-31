import Ham
a = float(input("Nhập số a: "))
b = float(input("Nhập số b: "))
op = input("Nhập phép toán (+, -, *, /): ")
KQ = Ham.tinh_toan(a, b, op)
print("Kết quả:", KQ)