def max_mangoes(x,y,z):
    if y>=z:
        return 0
    return (z-y)//x
x,y,z=map(int,input().split())
print(max_mangoes(x,y,z))
