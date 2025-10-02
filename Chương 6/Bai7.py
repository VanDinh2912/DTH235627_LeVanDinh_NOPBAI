def nhap_day_tang(N):
    lst = []
    for i in range(N):
        while True:
            x = int(input(f"Nhập số thứ {i+1}: "))
            # nếu là phần tử đầu tiên hoặc số mới > số cuối cùng thì chấp nhận
            if i == 0 or x > lst[-1]:
                lst.append(x)
                break
            else:
                print("Số phải lớn hơn số trước đó! Nhập lại !")
    return lst


n = int(input("Nhập số lượng phần tử: "))
day = nhap_day_tang(n)

print("Dãy số tăng dần vừa nhập là:", day)
