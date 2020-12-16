import numpy as np
a = np.array([1,2,3,4,5])
print (a)

# pip install numpy==1.19.3 -i https://pypi.tuna.tsinghua.edu.cn/simple


# 多于一个维度
import numpy as np
a = np.array([[1, 2], [3, 4]]) # 二维
print (a)

# 最小维度
import numpy as np
a = np.array([1,2,3,4,5], ndmin = 2)
print (a)

#
import numpy as np
# 使用标量类型
dt = np.dtype(np.int32)
print(dt)

import numpy as np
# int8, int16, int32, int64 四种数据类型可以使用字符串 'i1', 'i2','i4','i8' 代替
dt = np.dtype('i4')
print(dt)

import numpy as np
# 字节顺序标注
dt = np.dtype('>i4')
print(dt)


# 首先创建结构化数据类型
import numpy as np
dt = np.dtype([('age',np.int8)])
print(dt)
