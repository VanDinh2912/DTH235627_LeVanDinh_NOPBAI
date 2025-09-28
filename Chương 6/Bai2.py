from random import randrange


n = int(input("Nhập số phần tử:"))

# Tạo list ngẫu nhiên bằng list comprehension
lst = [randrange(0, 100) for _ in range(n)]
print("List sau khi tạo ngẫu nhiên là:")
print(lst)

# Thêm số mới
x = int(input("Mời bạn chèn thêm số mới: "))
lst.append(x)
print("List sau khi chèn:")
print(lst)

# Xóa tất cả số k
k = int(input("Mời nhập số để xóa: "))
lst = [val for val in lst if val != k]
print("List sau khi xóa:")
print(lst)


# Kiểm tra đối xứng (palindrome)
def CheckDoiXung(lst):
    return lst == lst[::-1]


if CheckDoiXung(lst):
    print("List đối xứng")
else:
    print("List không đối xứng")
