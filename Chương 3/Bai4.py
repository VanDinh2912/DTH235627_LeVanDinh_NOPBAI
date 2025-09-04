try :
    x = int(input("Nhập x: "))
    y = int(input("Nhập y: "))
    z = int(input("Nhập z: "))

    while True:
        expr = input("Nhập biểu thức boolean (hoặc 'exit/thoat' để thoát): ").strip().lower()
        
        # Nếu nhập exit hoặc thoát thì dừng vòng lặp
        if expr in ["exit", "thoát", "thoat"]:
            print("Đã thoát chương trình.")
            break

        try:
            # Thực hiện biểu thức Boolean
            result = eval(expr)
            print(f"Kết quả: {result}")
        except Exception as e:
            print(f"Lỗi khi thực hiện biểu thức: {e}")
except ValueError:
    print("Vui lòng nhập số nguyên hợp lệ !")