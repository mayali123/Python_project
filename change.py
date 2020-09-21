val=input("请输入一个带符号的钱")
if val[-1] in ['$']:
    change_num=6*float(val[0:-1])
    print("%.2f美元转换为人民币为%.2f"%(float(val[0:-1]),change_num))
elif val[-1] in ['￥']:
    change_num=float(val[0:-1])/6
    print("%.2f人民币转换为美元为%.2f"%(float(val[0:-1]),change_num))
else :
    print("格式错误")