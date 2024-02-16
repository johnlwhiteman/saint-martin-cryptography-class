import numpy as np
import matplotlib.pyplot as plt
from mpl_tookits.mplot3d import Axes3D

# https://en.wikipedia.org/wiki/Linear_congruential_generator
rNums = np.zeros(cnt)
def lcg(x0, cnt, a = 75, c = 74, m = 67108865):
    for i in range(0, cnt):
        x1 = (a * x0 + c) % m
        rNums[i] = x1
        x0 = x1

seed = 4
rNums = 10**4

rNums = lcg(seed, rNums)