try:
    while True:  
        n = int(input("Nhập vào chiều cao n: "))
        chon = input("Nhập hình bạn muốn chọn (1-3, hoặc 'e' để thoát): ").lower().strip()

        if chon == "e":   
            print("Thoát chương trình!")
            break

       
        options = [
            ["1", "mot", "một", "hình 1", "hinh 1", "hinh mot", "hình một"],
            ["2", "hai", "hình 2", "hinh 2", "hinh hai", "hình hai"],
            ["3", "ba", "hình 3", "hinh 3", "hinh ba", "hình ba"]
        ]

        chon_num = 0
        for idx, keywords in enumerate(options, start=1):
            if chon in keywords:
                chon_num = idx
                break

        if chon_num == 1:
          
            for i in range(n):
                for j in range(n):
                    if i == 0 or i == n-1 or j == 0 or j == n-1:
                        print("*", end=" ")
                    else:
                        print(" ", end=" ")
                print()

        elif chon_num == 2:
         
            for i in range(n, 0, -1):
                for j in range(i):
                    print("*", end=" ")
                print()

        elif chon_num == 3:
            # Hình X
            size = 2 * n - 1
            for i in range(size):
                for j in range(size):
                    if i == n - 1:                      
                        print("*", end=" ")
                    elif i < n - 1 and (j == 0 or j == i):   
                        print("*", end=" ")
                    elif i > n - 1 and (j == i or j == size - 1):  
                        print("*", end=" ")
                    else:
                        print(" ", end=" ")
                print()
        else:
            print("⚠ Chỉ có dữ liệu hình từ 1 đến 3 !")

        # Hỏi có muốn tiếp tục không
        tiep = input("Bạn có muốn vẽ lại hình khác? (y/n): ").lower().strip()
        if tiep != "y":
            print("Kết thúc chương trình!")
            break

except Exception as e:
    print("Nhập sai dữ liệu!", e)
