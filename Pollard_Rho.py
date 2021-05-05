
'''
Created on 2012-3-10
@author: daweibalong
'''
 
from random import randint
 
f=[]
 
def gcd(m,n):
    if n>0:
        return gcd(n,m%n)
    return m
 
def isPrime(n):
    if n<2:
        return True
    for i in range(2,int(pow(n,0.5))+1):
        if n%i==0:
            return False
    return True
 
def ifenough(num):
    m=1
    for i in f:
        m*=i
    if m==num:
        return 0
    if m>num:
        return 1
    return 2
 
def PollardRho(num,n):
    if(isPrime(n)):
        f.append(n)        
        return;
    x=[]
    i=1    
    x.append(-1)
    x.append(randint(1,n))
        
    y=x[1]
    k=2
    while True:
        i+=1   
        x.append((abs(x[i-1]*x[i-1]-1))%n)
                
        d=gcd(abs(y-x[i]),n)
 
        if d>1 and d<n:   
            PollardRho(num,d)    
            PollardRho(num,n/d)
        
        if i==k:
            y=x[i]
            k=2*k
        
        if x.index(x[i],0,i+1)!=i or ifenough(num)==0 or ifenough(num)==1:
            break      
        
def repeat(n):
    while True:
        f[:]=[]
        PollardRho(n,n)
        if ifenough(n)==0:
            f.sort()
            for index,j in enumerate(f):
                if index!=len(f)-1:
                    print(int(j),'*',end='',sep='')
                else:
                    print(int(j))
            break
 
if __name__=='__main__':
    print('please enter the number you want to divide:')
    n=int(input())
    repeat(n)
