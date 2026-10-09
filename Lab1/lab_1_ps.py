# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 14:26:38 2026

@author: Student
"""

import matplotlib.pyplot as plt
import numpy as np


#ex 1

x = lambda t : np.cos(260*2*np.pi*t+np.pi/3)
y = lambda t : np.cos(140*2*np.pi*t-np.pi/3)
z = lambda t : np.cos(60*2*np.pi*t+np.pi/3)

#a)

timp = np.linspace(0,0.1,1000)

#b)

fig, axs = plt.subplots(3)
fig.suptitle("Graficele functiilor la ex1")
axs[0].plot(timp,x(timp))
axs[1].plot(timp,y(timp))
axs[2].plot(timp,z(timp))
plt.savefig('Graficele functiilor la ex1.pdf')

#c)
fr = 200 # Hz

timp_sample = []
x_sample = []
y_sample = []
z_sample = []

for n in range(0,200):
    timp_sample.append(n/fr)
    x_sample.append(x(n/fr))
    y_sample.append(y(n/fr))
    z_sample.append(z(n/fr))
    
fig, axs = plt.subplots(3)
fig.suptitle("Esantioanele cu plot la ex1")
axs[0].plot(timp_sample,x_sample)
axs[1].plot(timp_sample,y_sample)
axs[2].plot(timp_sample,z_sample)
plt.savefig('Esantioanele cu plot la ex1.pdf')



fig, axs = plt.subplots(3)
fig.suptitle("Esantioanele cu stem la ex1")
axs[0].stem(timp_sample,x_sample)
axs[1].stem(timp_sample,y_sample)
axs[2].stem(timp_sample,z_sample)
plt.savefig('Esantioanele cu stem la ex1.pdf')


#%%

#ex2

import matplotlib.pyplot as plt
import numpy as np

#a)

x = lambda t : np.sin(400*2*np.pi*t) # frecventa 400

timp = np.linspace(0,0.1,1000)

# cu 1600 de esantioane

timp_sample = []
x_sample = []

for n in range(0,1600):
    timp_sample.append(n/200)
    x_sample.append(x(n/200))
    
fig, axs = plt.subplots(2)
fig.suptitle("Functia si esantionul 2-a")
axs[0].plot(timp,x(timp))
axs[1].stem(timp_sample,x_sample)
plt.savefig('Functia si esantionul 2-a.pdf')

#b)

y = lambda t : np.sin(800*2*np.pi*t) # frecventa 800

timp = np.linspace(0,0.1,30000)

fig, axs = plt.subplots(1)
fig.suptitle("Functia la 2-b")
axs.plot(timp,y(timp))
plt.savefig('Functia la 2-b.pdf')

#c)

z = lambda t : np.mod(240*t,1)

timp = np.linspace(0,0.04,1000)

fig, axs = plt.subplots(1)
fig.suptitle("Functia la 2-c")
axs.plot(timp,z(timp))
plt.savefig('Functia la 2-c.pdf')

#d)

w = lambda t : np.sign(np.sin(300*2*np.pi*t))

timp = np.linspace(0,0.1,1000)

fig, axs = plt.subplots(1)
fig.suptitle("Functia la 2-d")
axs.plot(timp,w(timp))
plt.savefig('Functia la 2-d.pdf')


#%%

#e)
import matplotlib.pyplot as plt
import numpy as np


matr = np.random.random((128,128))

fig, axs = plt.subplots(1)
fig.suptitle("Matricea la 2-e  cu random")
plt.imshow(matr)
plt.savefig('Matricea la 2-e  cu random.pdf')

matr = np.zeros((128,128))

for i in range(128):
    for j in range(128):
        matr[i,j]=np.random.uniform()

fig, axs = plt.subplots(1)
fig.suptitle("Matricea la 2-e  uniform")
plt.imshow(matr)
plt.savefig('Matricea la 2-e  uniform.pdf')

matr = np.zeros((128,128))

for i in range(128):
    for j in range(128):
        matr[i,j]=np.random.normal()

fig, axs = plt.subplots(1)
fig.suptitle("Matricea la 2-e  normala")
plt.imshow(matr)
plt.savefig('Matricea la 2-e  normala.pdf')

#%%

#f)

import matplotlib.pyplot as plt
import numpy as np

my = np.zeros((128,128))

for i in range(128):
    for j in range(128):
        my[i,j]=(abs(i-64)**(2)+abs(j-64)**(2))**(1/2)

fig, axs = plt.subplots(1)
fig.suptitle("Matricea la 2-f")
plt.imshow(my)
plt.colorbar()
plt.savefig('Matricea la 2-f.pdf')

#%%

my2 = np.zeros((128,128))

for i in range(128):
    for j in range(128):
        my2[i,j]=np.mod((abs(i-64)**(2)+abs(j-64)**(2))**(1/2),10)

fig, axs = plt.subplots(1)
fig.suptitle("Matricea la 2-f  extra")
plt.imshow(my2)
plt.colorbar()
plt.savefig('Matricea la 2-f  extra.pdf')







#%%

#3

fr = 2000 # Hz
print("Frecventa este",fr)


#a)
T = 1/fr # sec
print("intervalul de timp intre doua esantioane este",T)


#b)
nr_biti = 4*3600*fr
print("Numarul de biti este",nr_biti)
print("Numarul de Bytes este",nr_biti/(2**3))
print("Numarul de Kb este:",nr_biti/(2**13))
print("Numarul de Mb este:",nr_biti/(2**23))
print("Numarul de Gb este:",nr_biti/(2**33))



