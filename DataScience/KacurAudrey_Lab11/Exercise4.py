import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy import stats
# You can use the sum() and mean() built-inn functions

# based on your dataset from Ex. 1 compute the: SST, SSR, SSE (slide 336) and the: r, R^2 (slide 337).
xli = [-5, -1, 3, 7, 5, 9]
x = np.array(xli)
yli = [-10, -3, 5, 8, 7, 9]
y = np.array(yli)

# compute the: SST (sum of squares total) = sum (yi - y)^2
SST = np.sum((y-np.mean(y))**2)
print("SST: ", SST)

# compute the: SSR
slope, intercept, r, p, std_err = stats.linregress(x, y)

# find the parameters of the line (slope and y-intercept)
mymodel = (slope*x) + intercept
SSR = np.sum((mymodel-np.mean(y))**2)
print("SSR: ", SSR)

# compute the: SSE (slide 336) and the:
SSE = np.sum((mymodel - y)**2)
print("SSE: ", SSE)

# compute the:r, R^2 (slide 337).
r = ((np.sum((x-np.mean(x))*(y-np.mean(y)))) /
     (((np.sum((x-np.mean(x))**2)) * (np.sum((y-np.mean(y))**2)))**.5))
print("r: ", r)

R2 = 1 - ((sum((y-mymodel)**2)) / sum((y-np.mean(y))**2))
print("R2: ", R2)
