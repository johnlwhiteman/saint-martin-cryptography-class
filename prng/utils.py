import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import Axes3D
import numpy as np

def plot(prNums, bins=10, title="PRNG"):
    plt.figure(1)
    plt.hist(prNums['nums'], bins = bins)
    plt.title(title, fontsize = 17)
    plt.xlabel('Bins', fontsize = 13)
    plt.ylabel(f'Total: {len(prNums)}', fontsize = 13)
    print(f"Seed: {prNums['seed']}, a: {prNums['a']}, c: {prNums['c']}, m: {prNums['m']},  Period: {prNums['period']}, Count: {prNums['cnt']}")
    
def plot3D(prNums, bins=10, title="PRNG"):
    fig = plt.figure(figsize=(12, 5))
    ax1 = fig.add_subplot(121, projection='3d')
    ax2 = fig.add_subplot(122, projection='3ds')
    
    # generating 2d data
    xdata = np.random.normal(10,2,10000)
    ydata = np.random.normal(20,3,10000)
    h, xbins, ybins = np.histogram2d(xdata,ydata, bins=10)
    
    # a mesh grid with
    _xx, _yy = np.meshgrid(xbins[:-1], ybins[:-1])
    
    # bottom will be zero, top the h value
    bottom = np.zeros_like(_xx)
    top = h
    
    # bars width and depth is the bin size
    width = xbins[1]-xbins[0]
    depth = ybins[1]-ybins[0]
    
    # bard3d wants 1d arrays
    ax1.bar3d(_xx.flatten(), _yy.flatten(), bottom.flatten(), width, depth, h.flatten(), shade=True)
    ax1.set_title('shade=True')
    ax2.bar3d(_xx.flatten(), _yy.flatten(), bottom.flatten(), width, depth, h.flatten(), shade=False)
    ax2.set_title('shade=False')
    plt.show()
    
def show(prNums, asFloats=False):
    if asFloats:
        fmt = "{:.3f}".format
        with np.printoptions(threshold=np.inf, suppress=True, formatter={'float_kind':fmt}):
            print(prNums) 
    else:
        with np.printoptions(threshold=np.inf, suppress=True):
            print(prNums.astype(int))
