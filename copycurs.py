from test import *
from numpy import *
from pylab import *
d=3
dimension=[9,9,9]
r=23
a=zeros(dimension)
a[0,0,0]=a[0,3,3]=a[0,6,6]=1
a[1]=roll(a[0],1)
a[2]=roll(a[1],1)
a[3]=roll(a[2],1, axis=0)
a[4]=roll(a[3],1, axis=0)
a[5]=roll(a[4],-1)
a[6]=roll(a[5],-1)
a[7]=roll(a[6],-1, axis=0)
a[8]=roll(a[7],1)
eps=1e-8
a1, u,no=ALSproc(a,d,r,dimension,eps)
plot(no)
xlabel('Iterations')
ylabel('Norm')
title('Graphic of norm')
#fname="nonrnd5.pdf"
#savefig(fname)
#clf()
#print "[[file:%s]]" % fname
