from numpy import *
from numpy.linalg import *
from pylab import *
from time import *
from test import *


d=3
dimension=[32,32,32]
r=5
#a1=zeros(dimension)
#for i in xrange(0,dimension[0]):
#  for j in xrange(0,dimension[1]):
#    for k in xrange(0,dimension[2]):
#    	a1[i,j,k]=1.0/(i+j+k+1)


a,u0=randomtensor(r,dimension,size(dimension))

eps=1e-6
t=time()
a1,u,no=ALSproc(a,d,r,dimension,eps)
t=time()-t

