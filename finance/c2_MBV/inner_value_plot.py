# coding:utf-8

# European Call Option Inner Value Plot

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
mpl.rcParams['font.family'] = 'serif'

K = 8000

S = np.linspace(7000, 9000, 100)
h = np.maximum(S - K, 0)

plt.figure()
plt.plot(S, h, lw=2.5)
plt.xlabel('index level $S_t$ at maturity')
plt.ylabel('inner value of European call option')
plt.grid(True)
plt.show()