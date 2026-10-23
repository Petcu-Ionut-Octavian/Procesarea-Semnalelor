# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 10:29:01 2026

@author: User
"""



#EX 1

import numpy as np

N = 8
F = np.zeros((N,N),dtype=complex)


for m in range(N):
    for k in range(N):
        F[m][k] = np.exp(-2*np.pi*1j*k*m/N)
        
        
#print(np.round(F,4))




FHF = F.T.conj() @ F
print(np.round(FHF,3))
print("Matricea nenormalizata este aproape de un multiplu al identitatii:")
print(np.allclose(FHF,8*np.identity(N,dtype=complex)))

print("Norma diferentei:")
print(np.linalg.norm(FHF-8*np.identity(N,dtype=complex)))




#%%

#EX 2

import numpy as np
import matplotlib.pyplot as plt

A = 3
f = 10
x = lambda t: A*np.sin(f*2*np.pi*t)

t = np.linspace(0,1,100)

fig,ax = plt.subplots(2,1,num=4732,figsize=(10,10))

id = 0
ax[id].stem(t,x(t))
ax[id].set_title("Semnalul simplu")
ax[id].set_xlabel("Timp")
ax[id].set_ylabel("Amplitudine")
ax[id].grid(True)


y = lambda t: x(t)*np.exp(-2*np.pi*1j*t)
id = 1
ax[id].plot(np.real(y(t)),np.imag(y(t)))
ax[id].set_title("Semnalul infasurat")
ax[id].grid(True)


plt.tight_layout()
plt.savefig("Figura la ex2.pdf")


#%%

#EX 2 


import numpy as np
import matplotlib.pyplot as plt

A = 3

z = lambda t, w: A * np.sin(20 * 2 * np.pi * t) * np.exp(-2 * np.pi * 1j * w * t)

t = np.linspace(0, 1, 1000)

fig, ax = plt.subplots(2, 2, num=56642, figsize=(10, 10))

W = [5, 10, 20, 46]

for id, w in enumerate(W):
    i = id // 2
    j = id % 2

    x = np.real(z(t, w))
    y = np.imag(z(t, w))

    r = np.sqrt(x**2 + y**2)  # distanța față de origine

    sc = ax[i, j].scatter(
        x, y,
        c=r,
        cmap='RdBu',   # roșu aproape de origine, albastru spre exterior
        s=20
    )

    ax[i, j].set_title(f"w = {w}")
    ax[i, j].grid(True)
    ax[i, j].set_aspect('equal')

    fig.colorbar(sc, ax=ax[i, j], label='Distanța față de origine')

plt.tight_layout()
plt.show()


#%%


# # EX 2 animatie

# import numpy as np
# import matplotlib.pyplot as plt

# A = 3
# w = 46

# z = lambda t: A*np.sin(20*2*np.pi*t)*np.exp(-2*np.pi*1j*w*t)

# t = np.linspace(0, 1, 1000)

# x = np.real(z(t))
# y = np.imag(z(t))

# fig, ax = plt.subplots(num = 20311, figsize=(8, 8))

# ax.set_aspect('equal')
# ax.grid(True)

# ax.set_xlim(x.min()-0.5, x.max()+0.5)
# ax.set_ylim(y.min()-0.5, y.max()+0.5)

# for k in range(len(t)):
#     ax.scatter(x[k], y[k], c='red', s=10)
#     plt.pause(0.01)

# plt.show()


#%%


#EX 3 

s = lambda t: 7*np.sin(2*2*np.pi*t)+11*np.sin(3*2*np.pi*t)+9*np.sin(5*2*np.pi*t)
N = 40 # nr de puncte in care facem Fourier
fs = 20  # nr de esantioane pe secunda
f = fs/N

t = np.linspace(0,1/f,N,endpoint=False)

F = np.zeros((N,N),dtype=complex)

for m in range(N):
    for k in range(N):
        F[m][k] = np.exp(-2*np.pi*1j*k*m/N)/N




x = s(t)

X = F@x

y = 2*np.abs(X)  # am inmultit cu 2 sa obtin exact amplitudinile initiale A, nu A/2

plt.figure(num=1112334,figsize=(10,10))

a = []
b = []

for i,j in enumerate(y):
    a.append(i*f)
    b.append(j)
    
    
    
plt.figure(num = 123382,figsize = (10,10))
plt.stem(a,b)
plt.xlabel("frecventa Hz")
plt.ylabel("cat modulul componentei Fourier")
plt.savefig("ex3 figura.pdf")


