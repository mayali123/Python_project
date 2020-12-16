import numpy as np
a = np.random.randint(1,10,12).reshape(3,4)
print(a)
print("\na[0]:")
print(a[0])

print("\na[0][1]:")
print(a[0][1])



print("\n取第一二行:")
print(a[1:])

print("\n取第一列:")
print(a[:,0])
