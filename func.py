import numpy as np

def HCEFunc(x):
    D = len(x)
    R = 0
    for i in range(D):
        R += ((10 ** 6) ** (i / (D-1))) * (x[i] ** 2)
    return R

def BCFunc(x):
    D = len(x)
    R = x[0]**2
    for i in range(1, D):
        R += (10**6) * (x[i]**2)
    return R

def DFunc(x):
    D = len(x)
    R = (10**6) * (x[0]**2)
    for i in range(1, D):
        R += x[i]**2
    return R

def RoFunc(x):
    D = len(x)
    R = 0
    for i in range(D-1):
        R += (100*(((x[i]**2)-x[i+1])**2) + (x[i]-1)**2)
    return R

def AFunc(x):
    D = len(x)
    R = 0
    a = 0
    b = 0
    for i in range(D):
        a += x[i]**2
        b += np.cos(2*np.pi*x[i])
    R = -20*np.exp(-0.2*np.sqrt(a/D)) - np.exp(b/D) + 20 + np.e
    return R

def WFunc(x):
    D = len(x)
    R = 0
    a = 0.5
    b = 3
    kmax = 20
    p1 = 0
    p2 = 0
    for i in range(D):
        for k in range(0, kmax):
            p1 += (a**k) * np.cos(2*np.pi*(b**k)*(x[i] + 0.5))
    for k in range(0, kmax):
        p2 += (a**k) * np.cos(2*np.pi*(b**k)*0.5)
    R = p1 - (D*p2)
    return R

def GFunc(x):
    D = len(x)
    a = 0
    b = 1
    for i in range(D):
        a += x[i]**2
    for i in range(D):
        b *= np.cos(float(x[i]) / np.sqrt(i+1))
    R = 1 + (float(a)/4000.0) - float(b)
    return R

def RaFunc(x):
    D = len(x)
    R = 0
    for i in range(D):
        R += x[i]**2 - (10*np.cos(2*np.pi*x[i])) + 10
    return R

def KFunc(x):
    D = len(x)
    abcd = 10/(D**2)
    p1 = 0
    p2 = 1
    R = 0
    for i in range(D):
        for j in range(1, 33):
            p1 += (np.absolute((2**j)*x[i]-np.round((2**j)*x[i]))/(2**j))
        p2 *= (1 + i * p1) ** (10/(D**1.2))
    R = (abcd * p2) - abcd
    return R
