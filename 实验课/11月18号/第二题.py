def ElemIsOne(ls):
    st = ''.join(ls)
    for i in ls:
        if st.count(i)>1:
            return True
    return False
ls = ['a','b','c','d']
ls1 =  ['a','b','c','d','d']
print("ls:",ElemIsOne(ls))
print("ls1:",ElemIsOne(ls1))
