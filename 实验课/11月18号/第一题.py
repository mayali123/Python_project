import random
ls  = []
for i in range(ord('a'),ord('z')+1):
    if i !='o':
        ls.append(chr(i))
        ls.append(chr(i-ord('a')+ord('A')))
for i in range(1,10):
    ls.append(i)
for i in range(0,10):
    result = []
    while(True):
        word = random.choice(ls)
        if word in result:
            continue
        result.append(str(word))
        # print(result)
        if len(result)==8:
            password = ''.join(result)
            print(password)
            break
