from numpy import *
from numpy.linalg import *
from pylab import *
from test import *

#n=128
d1=4
d2=5
d3=6
dimension=[d1,d2,d3]
r=2
u=randn(dimension[0],r)
v=randn(dimension[1],r)
w=randn(dimension[2],r)

a,u0=randomtensor(r,dimension,size(dimension))
norma=norm(a)
appr=zeros(((d1,d2,d3)))
f=zeros((dimension[0],r))
while(norma>10**(-6)):
  m=(dot(v.transpose(),v))*(dot(w.transpose(),w))
  f=zeros((dimension[0],r))
  for i in range (0,dimension[0]):
    for alf in range(0,r):
      s=0
      for j in range(0,dimension[1]):
        for k in range(0,dimension[2]):
          s=a[i,j,k]*v[j,alf]*w[k,alf]+s
      f[i,alf]=s
  u=(solve(m,f.transpose())).transpose()

  dimension=roll(dimension,-1)
  f=zeros((dimension[0],r))
  m=(dot(u.transpose(),u))*(dot(w.transpose(),w))
  for j in range (0,dimension[0]):
    for alf in range(0,r):
      s1=0
      for k in range(0,dimension[1]):
        for i in range(0,dimension[2]):
          s1=a[i,j,k]*u[i,alf]*w[k,alf]+s1
      f[j,alf]=s1
  v=(solve(m,f.transpose())).transpose()

  dimension=roll(dimension,-1)
  f=zeros((dimension[0],r))
  m=(dot(v.transpose(),v))*(dot(u.transpose(),u))
  for k in range (0,dimension[0]):
    for alf in range(0,r):
      s2=0
      for i in range(0,dimension[1]):
        for j in range(0,dimension[2]):
          s2=a[i,j,k]*v[j,alf]*u[i,alf]+s2
      f[k,alf]=s2
  w=(solve(m,f.transpose())).transpose()

#Compute || a[i,j,k]-appr[i,j,k] ||
  dimension=[d1,d2,d3]
  appr[:,:,:]=0
  for i in range(0,dimension[0]):
    for j in range(0,dimension[1]):
      for k in range(0,dimension[2]):
        for alf in range(0,r):
          appr[i,j,k]=appr[i,j,k]+u[i,alf]*v[j,alf]*w[k,alf]
  norma=norm(a-appr)
  
  print('norma nevyazki',norma)
