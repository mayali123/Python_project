def prime(p):
    for i  in range(2,int(p**(1/2))+1):
        if p % i ==0:
            return False
    return True
for i in range(2,101):
    if prime(i):
        print(i)
