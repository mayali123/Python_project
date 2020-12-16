import numpy as np
a = np.random.randint(1,10,12).reshape(3,4)
b = np.random.randint(1,10,12).reshape(3,4)
print ('原数组：')
print (a)
print ('\n')
# 最大值
print (np.max(a))

# 最小值
print (np.min(a))

# 求和
print (np.sum(a))

# a - b
print("a-b:")
print(a-b)

# a + b
print("a+b:")
print(a+b)

print("a/b:")
print(a/b)




