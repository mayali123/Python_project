import numpy as np
a = np.random.randint(0,10,12).reshape(3,4)
print ('原数组：')
print (a)
print ('\n')
print ('对换数组：')
print (a.T)
