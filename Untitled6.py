#!/usr/bin/env python
# coding: utf-8

# exercie 1

# In[30]:


def modulo ():
    listmod=[]
    for i in range (2000,3200):
     if (((i%7)==0) &((i%5)!= 0)):
        listmod.append(i)
    return listmod


# In[31]:


list2=modulo()
print(list2)


# exercice 2

# In[32]:


def factoriel(t) :
    s=1
    for i in range (2,t+1):
        s=s*i
    print (s)
    
factoriel(4)


# exerice 3

# In[41]:


def dictpow(number):
    dicto={}
    for i in range(0,number+1):
        dicto.update({i:i*i})
    return dicto
result=dictpow(4)
print(result)
    
    


# exerice 4

# In[35]:


def deletter(char,index):
    a=char[0:index]
    b=char[index+1:]
    print(a+b)
deletter('lilia',2)


# exercice5

# In[36]:


import numpy as np
def tolist1(tabnum):
    return (tabnum.tolist())
numpytab=np.array([[0,1],[2,3],[4,5]])


print(tolist1(numpytab))


# exercice6

# In[37]:


npmat=np.array([0,1,2])
npmat2=np.array([2,1,0])
def covarience(npmat,npmat2):
     return (np.cov(npmat,npmat2))

npmat3=covarience(npmat,npmat2)
print (npmat3)


# exerice 7

# In[53]:


import math
x=True
list1=[]
while x==True:
    
    y=input("Donner moi une valeur")
    list1.append(int(y))
    
    y=input("voulez rajouter une valeur reponder par OUI ou NON")
    if (y=="NON"):
        x=False
def racine(listz) :
    for i in range(len(listz)):
        listz[i]=round(math.sqrt(listz[i]*100/30))
    print(str(listz)[:])
        
racine(list1)


# In[ ]:





# In[ ]:




