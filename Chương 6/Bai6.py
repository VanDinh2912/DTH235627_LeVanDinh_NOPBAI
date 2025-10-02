import random

N = int(input("Nhập N: "))

# sinh N số ngẫu nhiên KHÔNG TRÙNG trong khoảng 1..100
lst = random.sample(range(1, 101), N)

print("List:", lst)
