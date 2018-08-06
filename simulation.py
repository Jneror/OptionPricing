import numpy as np
#from pprint import pprint
import matplotlib.pyplot as plt
from alpha_vantage.timeseries import TimeSeries

def volatility(data):
    n = len(data)-1
    logaritmos = np.zeros(n)
    #dailyChange = np.zeros(n)
    for i in range(n):
        logaritmos[i] = np.log(data[i+1]/data[i])
        #dailyChange[i] = (data[i+1]-data[i])/data[i]
    return np.std(logaritmos, dtype=np.float64)
    #return np.std(logaritmos, dtype=np.float64)


ts = TimeSeries(key='7ERSLTME9P4Q0F6V', output_format = 'pandas')
data = ts.get_daily(symbol='FB', outputsize='full')[0]
#data['4. close'].plot()
#plt.show()
numSim = 1000
numIt = 100
t = 1 #t en años
dt = t/numIt
v = volatility(data['4. close'])
r = 0.01
s = 100
k = 100
brownian = np.exp((r - 0.5*v**2)*dt + v*np.random.normal(0, dt, (numSim, numIt)))
paths = s * np.cumprod(brownian,1)
print(dt, v, t)
print(np.max(paths))
for path in paths:
    plt.plot(path)
plt.show()
endValues = paths[:,-1]
plt.hist(endValues, 40)
plt.show()
print(np.mean((np.max(endValues-k, 0))*np.exp(-r*t)))
print(np.mean((np.max(k - endValues, 0))*np.exp(-r*t)))



