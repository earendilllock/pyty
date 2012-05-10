from numpy import *
from numpy.linalg import *
from pylab import *
from test import randomtensor

def gettensor(u1,r,dimension,d):
  u=[x.copy() for x in u1]
  s=1
  tr=u[0]
  temp=list(arange(d-2))
  for j in range(0,d-2):
    temp[j]=zeros((r,r*dimension[j+1]))
    for i in range(0,r):
      temp[j][i,i*dimension[j+1]:i*dimension[j+1]+dimension[j+1]]=u[j+1][:,i].transpose()
    u[j+1]=temp[j].transpose()	
  for i in range(0,d-1):
    tr=dot(tr,u[i+1].transpose())
    s=size(tr)/r
    tr=tr.reshape(s,r,order='F')
  tr=tr.reshape(dimension,order='F')
  return tr


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
      f[i,alf]=s              
  return f

def lefts(u,k,d):
  m=ones((r))
  for i in range(0,d):
    if (i<>k):
      
      m=m*dot(u[i].transpose(),u[i])
  return m
    
d=5
d1=4
d2=5
d3=6
d4=7
d5=8
dimension=[d1,d2,d3,d4,d5]
r=2


a1,u0=randomtensor(r,dimension,size(dimension))
norma=norm(a1)
a=a1.copy()
u=list(arange(d))
for i in range(0,d):
  u[i]=randn(dimension[i],r)

#f1=rights(a,u,dimension,d,r,1)
while(norma>10**(-6)):
  for i in range(0,d):
    y=rights(a,u,dimension,d,r,i)
    l=lefts(u,i,d)
    u[i]=solve(l,y.transpose()).transpose()
  a=gettensor(u,r,dimension,d)
  norma=norm(a1-a)
  print('norma nevyazki',norma)

  

