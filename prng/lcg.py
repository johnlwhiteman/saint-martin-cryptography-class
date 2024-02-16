import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import Axes3D
from IPython.display import display, Math, Latex
import numpy as np
from pprint import pprint as pp

def lcgRandu(seed, cnt):
    a = 65539
    c = 0
    m = 2**31
    return lcg(seed, m, a, c, cnt, 'RANDU')

def lcg(seed, m, a, c, cnt, name='LCG', stopAtDup=False):
    prNums = []
    prDups = set()
    period = m
    for i in range(0, cnt):
        seed = ((seed * a) + c) % m
        prNums.append(seed)
        if seed in prDups:
            period = i
            if stopAtDup:
                break
        prDups.add(seed)
    return {
        'name': name,
        'seed': seed,
        'm': m,
        'a': a,
        'c': c,
        'cnt': cnt,
        'period': period,
        'nums': np.array(prNums) / m,
    }

def plot(prNums, bins=10, title="PRNG"):
    plt.figure(1)
    plt.hist(prNums['nums'], bins = bins)
    plt.title(title, fontsize = 17)
    plt.xlabel('Bins', fontsize = 13)
    plt.ylabel(f'Total: {len(prNums)}', fontsize = 13)
    plt.show()
    print(f"Seed: {prNums['seed']}, a: {prNums['a']}, c: {prNums['c']}, m: {prNums['m']},  Period: {prNums['period']}, Count: {prNums['cnt']}")

def plot3D(prNums, bins=10, title="PRNG"):
    print(f"Seed: {prNums['seed']}, a: {prNums['a']}, c: {prNums['c']}, m: {prNums['m']},  Period: {prNums['period']}, Count: {prNums['cnt']}")
    cnt = prNums['cnt']
    y0 = prNums['nums'][0:cnt-2]
    y1 = prNums['nums'][1:cnt-1]
    y2 = prNums['nums'][2:cnt]
    fig = plt.figure(3)
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(y0, y1, y2)
    ax.set_xlabel("ith random number")
    ax.set_ylabel("j_1th random number")
    ax.set_zlabel("j+2th random number")
    ax.set_title(title)
    plt.show()

bins = 10
seed = 4
cnt = 10**3
prNums = lcgRandu(seed, cnt)
#plot3D(prNums, bins, f"RANDU, Seed: {seed}")

x = [0,1,2,3,4,5,6,7,8,9]
cnt = len(x)

y0 = x[0:cnt-2]
y1 = x[1:cnt-1]
y2 = x[2:cnt]

print(x)
print(y0)
print(y1)
print(y2)