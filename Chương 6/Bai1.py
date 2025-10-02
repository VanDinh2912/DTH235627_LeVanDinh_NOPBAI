from random import randrange

print("Chương trình xử lý List")
n = int(input("Nhập số phần tử: "))
lst = [0] * n

for i in range(n):
    lst[i] = randrange(-100, 100)

print("List ngẫu nhiên là:")
print(lst)

print("Mời bạn thêm số mới:")
value = int(input())
lst.append(value)
print(lst)

print("Bạn muốn đếm số nào:")
k = int(input())
dem = lst.count(k)
print(k, "xuất hiện", dem, "lần trong list")


# Hàm kiểm tra số nguyên tố
def CheckPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


demnt = 0
tongnt = 0
for x in lst:
    if CheckPrime(x):
        demnt += 1
        tongnt += x

print("Có", demnt, "số nguyên tố trong list")
print("Tổng =", tongnt)


# Quick sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


lst = quick_sort(lst)
print("List sau khi quick sort:")
print(lst)

# Làm rỗng list (không gây lỗi như del)
lst.clear()
print("List sau khi xóa (rỗng):")
print(lst)
del lst
