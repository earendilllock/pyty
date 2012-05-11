from numpy import *
from numpy.linalg import *
from pylab import *
from test import *

def rights(a,u,dimension,d,r,k):
  f=zeros((dimension[k],r))
  
  for i in range (0,dimension[k]):
    for alf in range(0,r):
      kol=0
      for j in range(0,d):
        if (j<>k):
          if(kol<>1):
            tmp=a.take([i],axis=k)
            sh=shape(tmp)
            print(sh)
            tmp=tmp.reshape(sh,order='F')
            s=dot(u[j][:,alf],tmp.reshape(size(u[j][:,alf]),size(tmp)/size(u[j][:,alf]),order='F'))
            
            kol=1
          else:
            s=s.reshape(size(u[j][:,alf]),size(s)/size(u[j][:,alf]),order='F')
            s=dot(u[j][:,alf],s)
      f[i,alf]=s
  return f
    
d=3
d1=4
d2=5
d3=6
d4=7
d5=8
dimension=[d1,d2,d3]
r=2


a1,u0=randomtensor(r,dimension,size(dimension))
norma=norm(a1)
a=a1.copy()
u=list(arange(d))
for i in range(0,d):
  u[i]=randn(dimension[i],r)


while(norma>10**(-6)):
  for i in range(0,d):
    y=rights(a,u,dimension,d,r,i)
    u[i]=solve(lefts(u,i,d,r),rights(a,u,dimension,d,r,i).transpose()).transpose()
  a=gettensor(u0,r,dimension,d)
  norma=norm(a1-a)
  print('norma nevyazki',norma)


