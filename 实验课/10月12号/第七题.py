time = 365
capacity = 1
for i in range(1, time+1):
    if i % 7 not in [1, 2, 3]:
        capacity *= 1.01
print("连续学天%d，365天后的能力值为%f" % (365, capacity))
