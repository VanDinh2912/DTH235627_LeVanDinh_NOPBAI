try : 
    i = int(input("Nhập số nguyên i: "))
    j = int(input("Nhập số nguyên j: "))
    k = int(input("Nhập số nguyên k: "))
    if i < j :
        if j < k :
            i = j
        else:
            j = k
    else:
        if j > k :
            j = i
        else:
            i = k
    print(f"i = {i}, j = {j}, k = {k}")
except ValueError:
    print("Vui lòng nhập số nguyên hợp lệ !")