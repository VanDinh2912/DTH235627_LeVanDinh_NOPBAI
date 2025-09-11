def oscillate(a,b):
    for i in range(a,b):
        yield i
        print(" ",end=" ")
        yield-i
        print(" ",end=" ")

for n in oscillate(-3,5):
    print( n ,end="")
print()