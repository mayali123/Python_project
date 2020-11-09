def cubic(n):
    num = 0
    for i in range(1,n+1):
        num += i**3
    return num
n=int(input("请输入一个n:"))
print(cubic(n))
