import Ham
n = int(input("Nhập n: "))
m = int(input("Nhập m: "))
s = int(input("Nhập s: "))
a = int(input("Nhập a: "))
b = int(input("Nhập b: "))


print("Tổng các số 1 + 2 + ... + n là:", Ham.tong_tu_mot_den_n(n))
if Ham.nt_cungnhau(m,n):
    print(f"Hai số này là nguyên tố cùng nhau")
else:
    print(f"Hai số này không phải là nguyên tố cùng nhau")


print("Thông báo:",Ham.doi_giay(s))
print("Trị tuyệt đối của |a - b| là:", Ham.tri_tuyet_doi(a, b))
