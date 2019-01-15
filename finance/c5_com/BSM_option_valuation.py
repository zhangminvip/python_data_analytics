import math
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from scipy.integrate import quad

mpl.rcParams['font.family'] = 'serif'


def dlf(St, K, t, T, r, sigma):
    d1 = (math.log(St / K) + (r + 0.5 * sigma ** 2)
          * (T - t)) / (sigma * math.sqrt(T - t))


def dN(x):
    return math.exp(-0.5 * x ** 2) / math.sqrt(2 * math.pi)


def N(d):
    return quad(lambda x: dN(x), -20, d, limit=50)[0]


def BSM_call_value(St, K, t, T, r, sigma):
    d1 = dlf(St, K, t, T, r, sigma)
    d2 = d1 - sigma * math.sqrt(T - t)
    call_value = St * N(d1) - math.exp(-r * (T - t)) * K * N(d2)
