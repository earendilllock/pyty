from numpy import *
from numpy.linalg import *
from pylab import *
<<<<<<< HEAD
from test import *
=======
from test import randomtensor


def gettensor(u1,r,dimension,d):
  u=[x.copy() for x in u1]
  s=1
  tr=u[0]
  temp=list(arange(d-2))
  for j in range(0,d-2):
    temp=zeros((r,r*dimension[j+1]))
    for i in range(0,r):
      temp[i,i*dimension[j+1]:i*dimension[j+1]+dimension[j+1]]=u[j+1][:,i].transpose()
    u[j+1]=temp.transpose()	
  for i in range(0,d-1):
    s=size(tr)/r
    tr=tr.reshape(s,r,order='F')
    tr=dot(tr,u[i+1].transpose())
  tr=tr.reshape(dimension,order='F')
  return tr
>>>>>>> c449b6552dbe1bc42c0bf2c9e543a0ffc75c27c3

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
<<<<<<< HEAD
d1=4
d2=5
d3=6
d4=7
d5=8
dimension=[d1,d2,d3]
r=2
=======
d1=2
d2=2
d3=2
d4=2
d5=2
#dimension=[d1,d2,d3]
d=3
dimension=[128,128,128]
r=3
>>>>>>> c449b6552dbe1bc42c0bf2c9e543a0ffc75c27c3


a1,u0=randomtensor(r,dimension,size(dimension))
norma=norm(a1)
nrm=norma
a=a1.copy()
u=list(arange(d))
for i in range(0,d):
<<<<<<< HEAD
  u[i]=randn(dimension[i],r)


while(norma>10**(-6)):
  for i in range(0,d):
    y=rights(a,u,dimension,d,r,i)
    u[i]=solve(lefts(u,i,d,r),rights(a,u,dimension,d,r,i).transpose()).transpose()
  a=gettensor(u0,r,dimension,d)
  norma=norm(a1-a)
  print('norma nevyazki',norma)

=======
    u[i]=randn(dimension[i],r)
eps=1e-6
while(norma>eps*nrm):
    for i in range(0,d):
        y=rights(a,u,dimension,d,r,i)
        l=lefts(u,i,d)
        u[i]=solve(l,y.transpose()).transpose()
    a1=gettensor(u,r,dimension,d)
    norma=norm(a1-a)
    print('norma nevyazki',norma)
  
>>>>>>> c449b6552dbe1bc42c0bf2c9e543a0ffc75c27c3

