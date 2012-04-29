
import numpy
from pylab import *



def randomtensor(r,dimension,d):
  u=list(arange(d))
  for i in range(0,d):
    u[i]=randn(dimension[i],r)
  u0=[x.copy() for x in u]
  s=1
  tr=u[0]
  temp=list(arange(d-2))
  for j in range(0,d-2):
    temp[j]=zeros((r,r*dimension[j+1]))
    for i in range(0,r):
      temp[j][i,i*dimension[1]:i*dimension[1]+dimension[1]]=u[j+1][:,i].transpose()
    u[j+1]=temp[j].transpose()	
  for i in range(0,d-1):
    tr=dot(tr,u[i+1].transpose())
    s=size(tr)/r
    tr=tr.reshape(s,r,order='F')
  tr=tr.reshape(dimension,order='F')
  return tr,u0

