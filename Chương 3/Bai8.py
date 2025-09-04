try :
    a = float(input("Nhập giá trị a: "))
    b = float(input("Nhập giá trị b: "))

    op = input("Nhập phép toán (+, -, *, /): ")

    if op == '+':
        result = a + b
    elif op == '-':
        result = a - b
    elif op == '*':
        result = a * b
    elif op == '/':
        if b != 0:
            result = a / b
        else:
            print("Lỗi: Không thể chia cho 0")
            exit()
    else:
        print("Phép toán không hợp lệ")
        exit()

    print(f"Kết quả: {a} {op} {b} = {result}")
except ValueError:
    print("Vui lòng nhập số hợp lệ !")