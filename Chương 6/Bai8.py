n = int(input("Nhập số lượng phần tử n: "))


M = []
for i in range(n):
    x = float(input(f"Nhập M[{i}]: "))
    M.append(x)


M.sort(reverse=True)
print("Dãy số sau khi sắp xếp giảm dần:", M)
