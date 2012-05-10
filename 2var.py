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
            s=dot(u[j][:,alf],s.reshape(size(u[j][:,alf]),size(s)/size(u[j][:,alf]),order='F'))
      f[i,alf]=s
            
  
  return f
d=4
d1=4
d2=5
d3=6
d4=7
dimension=[d1,d2,d3,d4]
r=2


a,u0=randomtensor(r,dimension,size(dimension))
norma=norm(a)

f1=rights(a,u0,dimension,d,r,0)
f=zeros((dimension[0],r))
for i in range (0,dimension[0]):
  for alf in range(0,r):
    s=0
    for j in range(0,dimension[1]):
      for k in range(0,dimension[2]):
        s=a[i,j,k]*u0[1][j,alf]*u0[2][k,alf]+s
    f[i,alf]=s
