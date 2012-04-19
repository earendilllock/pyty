
import numpy
from pylab import *


r=2
d=3
a=zeros(((4,5,6)))
dimension=zeros(d, dtype = int)
dimension[0]=4
dimension[1]=5
dimension[2]=6
#ytyt=randomtensor(r,dimension,d)
u=list(arange(d))
for i in range(0,d):
  u[i]=randn(dimension[i],r)
for i in range(0,dimension[0]):
  for j in range(0,dimension[1]):
    for k in range(0,dimension[2]):
      for alf in range(0,r):
        a[i,j,k]=u[0][i,alf]*u[1][j,alf]*u[2][k,alf]
  
  
s=1
tr=u[0]
temp=zeros((r,r*dimension[1]))
for i in range(0,r):
  temp[i,i*dimension[1]:i*dimension[1]+dimension[1]]=u[1][:,i].transpose()
u[1]=temp.transpose()
for i in range(0,d-1):
  tr=dot(tr,u[i+1].transpose())
  s=size(tr)/r
  tr=tr.reshape(s,r,order='F')
tr=tr.reshape(dimension,order='F')

