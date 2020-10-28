num  =int(input("请输入一个数字："))
if num%2== 0:
    if num %3==0:
        print("你输入的数可以整除2和3")
    else:
        print("你输入的数可以整除2,但不可以整除3")
else:
    if num %3==0:
        print("你输入的数可以整除3,但不可以整除2")
    else:
        print("你输入的数不能整除2和3")
            
