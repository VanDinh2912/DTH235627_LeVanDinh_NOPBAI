a = 0 
dem = 0
while a < 100:
    b = 0 
    while b < 100:
        if ( a+ b ) % 2 == 0:
            print('*', end=' ')
        b += 1
        dem += 1
    print()
    a+= 1  
print(f"Có tất cả {dem} dấu * được in ra.")     