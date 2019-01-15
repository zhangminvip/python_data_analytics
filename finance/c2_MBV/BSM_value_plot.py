import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
mpl.rcParams['font.family'] = 'serif'
import sys
sys.path.append('c5_com')
from BSM_option_valuation import BSM_call_value

K = 8000
T = 1.0
r = 0.025
vol = 0.2 # constant volatility

# Sample Data Generation

S = np.linspace(4000, 12000, 150)
h = np.maximum(S - K , 0)
C = [BSM_call_value(S0, K, 0, T, r, vol ) for S0 in S]


plt.figure()
plt.plot(S, h, 'b-', lw=2.5, label='inner value' )
plt.plot(S, C, 'r', lw=2.5, label='present value' )

plt.show()






