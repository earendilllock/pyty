from numpy import *
from numpy.linalg import *
from pylab import *
from time import *
from test import *
    
d=3
d1=2
d2=2
d3=2
d4=2
d5=2
#dimension=[d1,d2,d3]
d=3
dimension=[32,32,32]
r=5
#a1=zeros(dimension)
#for i in xrange(0,dimension[0]):
#  for j in xrange(0,dimension[1]):
#    for k in xrange(0,dimension[2]):
#    	a1[i,j,k]=1.0/(i+j+k+1)


a1,u0=randomtensor(r,dimension,size(dimension))
norma=norm(a1)
nrm=norma
no=[nrm]
a=a1.copy()
u=list(arange(d))
for i in xrange(0,d):
    u[i]=randn(dimension[i],r)
eps=1e-6
t=time()
while(norma>eps*nrm):
    for i in xrange(0,d):
        y=rights(a,u,dimension,d,r,i)
        l=lefts(u,i,d,r)
        u[i]=solve(l,y.transpose()).transpose()
    a1=gettensor(u,r,dimension,d)
    norma=norm(a1-a)
    no=no+[norma]
    
#    print('norma nevyazki',norma)
t=time()-t
plot(no)
show()  
