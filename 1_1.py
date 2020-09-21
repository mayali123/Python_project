# 温度得转化
val=eval(input("请输入温度值:"))
Type=input("请输入温度符号:")
print(val)
if Type in ['F','f']:
    C=(float(val)-32)/1.8
    print("转换后得温度为%dC"%C)
elif Type in ['C','c'] :
    F=float(val)*1.8+32
    print("转换后得温度为%.dF"%F)
else :
    print("输入格式错误")
