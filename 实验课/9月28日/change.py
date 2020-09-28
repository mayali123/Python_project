val = input("请输入一个带符号的钱:")
if val[-1] in ['$']:
    chang_num=float(val[0:-1])*6
    print("%.2f美元转换为%.2f人民币" %(float(val[0:-1]), chang_num))
elif val[-1] in ['￥']:
    chang_num=float(val[0:-1])/6
    print("%.2f人民币转换为%.2f美元" % (float(val[0:-1]),chang_num))
else :
    print("格式错误")
