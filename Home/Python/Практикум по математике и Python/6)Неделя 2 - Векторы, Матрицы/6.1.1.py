import numpy as np

l = input().split(",")
l = list(map(float, l))
V1 = np.array(l)
V2 = np.array(V1[-2])
V3 = V1[::-1]
V4 = V1[::3]
V5 = np.array([i for i in range(len(l))])
