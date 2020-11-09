def move(n,a,b,c):
    if n ==1:
        print("%c->%c"%(a,c))
    else:
        move(n-1,a,c,b)
        print("%c->%c"%(a,c))
        move(n-1,b,a,c)
n=int(input("请输入层数:"))
move(n,'A','B','C')
