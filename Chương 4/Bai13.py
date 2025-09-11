import math

def tong_uoc(n):
    s = 1  
    can = int(math.sqrt(n))
    for i in range(2, can + 1):
        if n % i == 0:
            s += i
            if i != n // i and n // i != n:  
                s += n // i
    return s

def la_hoan_thien(n):
    return tong_uoc(n) == n

def la_thinh_vuong(n):
    return tong_uoc(n) > n

while True:
    n = int(input("Nhập số nguyên dương n: "))

    if la_hoan_thien(n):
        print(f"{n} là số hoàn thiện.")
    elif la_thinh_vuong(n):
        print(f"{n} là số thịnh vượng.")
    else:
        print(f"{n} không phải số hoàn thiện, cũng không phải số thịnh vượng.")

    tiep = input("Bạn có muốn nhập tiếp không? (c/k): ").lower().strip()
   

    if tiep in ["c", "co", "có"]:
        continue   # quay lại vòng while, nhập tiếp
    else:
        print("Kết thúc chương trình.")
        break