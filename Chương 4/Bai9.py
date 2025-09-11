import math
def s(n):
    if n==1:
        return math.sqrt(2)
    return math.sqrt(2+s(n-1))

n = int(input("Nhập n: "))
print(f"S({n}) =", s(n))