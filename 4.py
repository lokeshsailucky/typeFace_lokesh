import numpy as np

def myfunc(ar):
    a=np.array(ar)
    r1=0
    r2=len(a)-1
    c1=0
    c2=len(a[0])-1
    if 0 not in a[r1]:
        r1=r1+1
    if 0 not in a[r2]:
        r2=r2-1
    if 0 not in a[:,c1]:
        c1=c1+1
    if 0 not in a[:,c2]:
        c2=c2-1
    return (r1,c1),(r1,c2),(r2,c1),(r2,c2)

  
R = int(input("Enter the number of rows:"))
C = int(input("Enter the number of columns:"))

ar= []
  
for i in range(R):
    b=[]
    for j in range(C):
         b.append(int(input()))
    ar.append(b)
myfunc(ar)