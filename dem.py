from scipy.optimize import root
from scipy.optimize import minimize
from math import cos


def eqn(x):
    return x + cos(x)

myroot = root(eqn,0)
mymin = minimize(eqn,0)

print(myroot.x)
print(mymin)
