st = int(input("请选择是解密还是加密(加密输入0，解密输入1)："))

if st == 0:
    st2 = input("输入要加密的内容:")
    for p in st2:
        if 'a' <= p <= 'z':
            print(chr(ord('a')+(ord(p)-ord('a')+5)%26),end='')
        elif 'A' <=p <= 'Z':
            print(chr(ord('A')+(ord(p)-ord('A')+5)%26),end='')
elif st==1:
    st3 = input("输入要解密的内容:")
    for p in st3:
        if 'a' <= p <= 'z':
            print(chr(ord('a')+(ord(p)-ord('a')-5)%26),end='')
        elif 'A' <=p <= 'Z':
            print(chr(ord('A')+(ord(p)-ord('A')-5)%26),end='')
else:
    print("格式错误！")
