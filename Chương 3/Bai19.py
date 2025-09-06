import math


x = float(input("Nhập x: "))
n = int(input("Nhập n: "))

S = 0
for k in range(n + 1):
    tu_so = x ** (2 * k + 1)      
    mau_so = math.factorial(2 * k + 1)  
    S += tu_so / mau_so
print(f"S({x}, {n}) = {S}")
