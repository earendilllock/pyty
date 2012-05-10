from numpy import *
from numpy.linalg import *
from pylab import *
from test import randomtensor

def rights(a,u,dimension,d,r,k):
  f=zeros((dimension[k],r))
  
  for i in range (0,dimension[k]):
    for alf in range(0,r):
      kol=0
      for j in range(0,d):
        if (j<>k):
          if(kol<>1):
            s=dot(u[j][:,alf],a.take([i],axis=k).reshape(size(u[j][:,alf]),size(a.take([i],axis=k))/size(u[j][:,alf]),order='F'))
            
            kol=1
          else:
            s=s.reshape(size(u[j][:,alf]),size(s)/size(u[j][:,alf]),order='F')
            s=dot(u[j][:,alf],s)
#            print(shape(s))
      f[i,alf]=s
            
  
  return f
d=5
d1=4
d2=5
d3=6
d4=7
d5=8
dimension=[d1,d2,d3,d4,d5]
r=4


a,u0=randomtensor(r,dimension,size(dimension))
norma=norm(a)

f1=rights(a,u0,dimension,d,r,3)
f=zeros((dimension[0],r))

