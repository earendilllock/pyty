from scipy import *
from numpy import *
from pylab import *


def f(x):
  if(x>=0):
    return 100*exp(-x)
  else:
    return 100*exp(x)

def integr(a,b):
  return (f(b)+f(a))/2*(b-a)

ab=list()
a=-1
b=-0.1
ab.append(a)
ab.append(b)

def listdo(ab,a,b):
  i=1
  while (True):
    flag=True
    integ=integr(ab[i-1],ab[i])
    promint=integr(ab[i-1],ab[i-1]+(ab[i]-ab[i-1])/2.0)+integr(ab[i-1]+(ab[i]-ab[i-1])/2.0,ab[i])
    if(abs(promint-integ)>10**(-6)):
      ab.append(ab[i-1]+(ab[i]-ab[i-1])/2.0)
      ab.sort()
      
    else:
      if(ab[i]<b):
        i=i+1
        flag=False
    if((ab[i]==b) & flag):
      break
  return ab

def integriruy(a,b):
  i=0
  integral=0
  ab=list()
  ab.append(a)
  ab.append(b)
  ab=listdo(ab,a,b)
  while(ab[i]<b):
    integral=integral+integr(ab[i],ab[i+1])
    i=i+1
  return integral


integral=integriruy(a,b)

