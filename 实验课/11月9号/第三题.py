def factorial(n):
    j = 1
    num  = 0
    for i in range(1,n+1):
        j *= i
        num+=j
    return num
n=int(input("请输入一个n:"))
print(factorial(n))
