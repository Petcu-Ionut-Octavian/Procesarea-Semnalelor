# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 22:31:13 2026

@author: User
"""

#EX1

import numpy as np
import matplotlib.pyplot as plt

# Parametrii semnalului
A = 2          # amplitudinea
f = 5          # frecventa (Hz)
phi = np.pi/6  # faza (rad)

# Orizontul de timp
t = np.linspace(0, 1, 1000)

# Semnal sinus
sinus = A * np.sin(2 * np.pi * f * t + phi)

# Semnal cosinus identic cu sinusul
cosinus = A * np.cos(2 * np.pi * f * t + phi - np.pi/2)

# Afisare
fig, ax = plt.subplots(2, 1, figsize=(8, 6))

ax[0].plot(t, sinus, 'b')
ax[0].set_title('Semnal sinus')
ax[0].set_xlabel('Timp [s]')
ax[0].set_ylabel('Amplitudine')
ax[0].grid(True)

ax[1].plot(t, cosinus, 'r')
ax[1].set_title('Semnal cosinus echivalent')
ax[1].set_xlabel('Timp [s]')
ax[1].set_ylabel('Amplitudine')
ax[1].grid(True)

plt.tight_layout()
#plt.show()
plt.savefig('Sin si cos identice la ex1.pdf')

#%%

#EX2   prima parte

import numpy as np
import matplotlib.pyplot as plt

# Parametri
A = 1
f = 5
t = np.linspace(0, 1, 1000)

faze = [0, np.pi/4, np.pi/2, 3*np.pi/4]

fig, ax = plt.subplots(2, 2, num=2, figsize=(10, 6))

for i, phi in enumerate(faze):
    x = A * np.sin(2 * np.pi * f * t + phi)

    ax[i//2, i%2].plot(t, x)
    ax[i//2, i%2].set_title(f'φ = {phi:.2f} rad')
    ax[i//2, i%2].set_xlabel('Timp [s]')
    ax[i//2, i%2].set_ylabel('Amplitudine')
    ax[i//2, i%2].grid(True)

plt.tight_layout()
#plt.show()
plt.savefig('Semnal sinusoidal cu 4 faze diferite la ex2.pdf')



#%%

#EX2 a doua parte



import numpy as np
import matplotlib.pyplot as plt

A = 1
f = 5
phi = np.pi/4

t = np.linspace(0, 1, 1000)

x = A * np.sin(2 * np.pi * f * t + phi)

#Signal to Noise Ratio

snr_values = [0.1, 1, 10, 100]

plt.figure(num=3, figsize=(10, 8))

for i, snr in enumerate(snr_values, start=1):

    z = np.random.normal(0, 1, len(x))

    gamma = np.linalg.norm(x) / (np.sqrt(snr) * np.linalg.norm(z))

    x_noisy = x + gamma * z

    plt.subplot(2, 2, i)
    plt.plot(t, x, label='Semnal original')
    plt.plot(t, x_noisy, label=f'SNR={snr}')
    plt.title(f'SNR = {snr}')
    plt.grid(True)
    plt.legend()

plt.tight_layout()
#plt.show()
plt.savefig('Semnal cu zgomot la ex2.pdf')


#%%

#EX 3

# import numpy as np
# import sounddevice as sd
# from scipy.io.wavfile import write, read

# fs = 44100  # frecventa de esantionare

# # 2(a)
# x = lambda t: np.sin(400 * 2 * np.pi * t)

# # 2(b)
# y = lambda t: np.sin(800 * 2 * np.pi * t)

# # 2(c) - semnal dinte de fierastrau
# z = lambda t: np.mod(240 * t, 1)

# # 2(d) - semnal dreptunghiular
# w = lambda t: np.sign(np.sin(300 * 2 * np.pi * t))

# # durata de redare
# t = np.linspace(0, 2, 2 * fs, endpoint=False)

# semnale = {
#     "a": x(t),
#     "b": y(t),
#     "c": z(t),
#     "d": w(t)
# }

# # ascultare semnale
# for nume, semnal in semnale.items():
#     print(f"Redare semnal {nume}")
#     sd.play(semnal, fs)
#     sd.wait()

# # salvam unul dintre ele (de exemplu 2(a))
# semnal_salvat = semnale["a"]

# # conversie la int16 pentru wav
# semnal_wav = np.int16(
#     semnal_salvat / np.max(np.abs(semnal_salvat)) * 32767
# )

# write("semnal_2a.wav", fs, semnal_wav)

# print("Fisierul a fost salvat.")

# # verificare citire
# fs_read, semnal_citit = read("semnal_2a.wav")

# print("Frecventa de esantionare:", fs_read)
# print("Numar esantioane:", len(semnal_citit))

# # redare dupa citire
# sd.play(semnal_citit, fs_read)
# sd.wait()


#%%

# EX4

import numpy as np
import matplotlib.pyplot as plt

# semnalul sinusoidal
x = lambda t: np.sin(2 * 2 * np.pi * t)

# semnalul sawtooth
z = lambda t: np.mod(4 * t, 1)

# semnalul suma 
w = lambda t: x(t) + z(t)


t = np.linspace(0, 1, 1000)

fig, ax = plt.subplots(3, 1, num=5, figsize=(10, 6))

ax[0].plot(t,x(t))
ax[0].set_title("Semnalul sinusoidal")
ax[0].set_xlabel('Timp [s]')
ax[0].set_ylabel('Amplitudine')
ax[0].grid(True)

ax[1].plot(t,z(t))
ax[1].set_title("Semnalul sawtooth")
ax[1].set_xlabel('Timp [s]')
ax[1].set_ylabel('Amplitudine')
ax[1].grid(True)

ax[2].plot(t,w(t))
ax[2].set_title("Semnalul suma")
ax[2].set_xlabel('Timp [s]')
ax[2].set_ylabel('Amplitudine')
ax[2].grid(True)


plt.tight_layout()
#plt.show()
plt.savefig('Semnalele si suma lor la ex4.pdf')


#%%

# #EX 5

# import numpy as np
# import sounddevice as sd
# from scipy.io.wavfile import write, read

# fs = 44100  # frecventa de esantionare

# x = lambda t: np.sin(400 * 2 * np.pi * t)

# y = lambda t: np.sin(600 * 2 * np.pi * t)

# # durata de redare
# t = np.linspace(0, 2, 2 * fs, endpoint=False)

# semnal = np.concatenate((x(t),y(t)))


# print("Redare semnal ex5")
# sd.play(semnal, fs)
# sd.wait()

#%%

#Ex 6

import numpy as np
import matplotlib.pyplot as plt

fs = 33   # 0.1 100 1

fa = fs/2
fb = fs/4
fc = 0

t = np.arange(0,1,1/fs)

a = lambda t: np.sin(fa * 2 * np.pi * t)
b = lambda t: np.sin(fb * 2 * np.pi * t)
c = lambda t: np.sin(fc * 2 * np.pi * t)


fig,ax=plt.subplots(3,1,num=7,figsize=(10,10))




ax[0].stem(t,a(t))
ax[0].set_title("Semnalul a")
ax[0].set_xlabel('Timp [s]')
ax[0].set_ylabel('Amplitudine')
ax[0].grid(True)

ax[1].stem(t,b(t))
ax[1].set_title("Semnalul b")
ax[1].set_xlabel('Timp [s]')
ax[1].set_ylabel('Amplitudine')
ax[1].grid(True)

ax[2].stem(t,c(t))
ax[2].set_title("Semnalul c")
ax[2].set_xlabel('Timp [s]')
ax[2].set_ylabel('Amplitudine')
ax[2].grid(True)



plt.tight_layout()
#plt.show()
plt.savefig('Semnalele la ex6.pdf')


#%%


#Ex 7

import numpy as np
import matplotlib.pyplot as plt

x = lambda t: np.sin(10 * 2 * np.pi * t)

t = np.linspace(0,1,133)

fig,ax=plt.subplots(3,1,num=81,figsize=(10,10))

t1 = t[::4]
t2 = t[1::4]


ax[0].stem(t,x(t))
ax[0].set_title("Semnalul x")
ax[0].set_xlabel('Timp [s]')
ax[0].set_ylabel('Amplitudine')
ax[0].grid(True)

ax[1].stem(t1,x(t1))
ax[1].set_title("Semnalul x decimat 1/4")
ax[1].set_xlabel('Timp [s]')
ax[1].set_ylabel('Amplitudine')
ax[1].grid(True)

ax[2].stem(t2,x(t2))
ax[2].set_title("Semnalul x decomat 1/4 pornind de la al doilea")
ax[2].set_xlabel('Timp [s]')
ax[2].set_ylabel('Amplitudine')
ax[2].grid(True)



plt.tight_layout()
#plt.show()
plt.savefig('Semnalele la ex7.pdf')

#%%

#EX 8


import numpy as np
import matplotlib.pyplot as plt

pade = lambda t: (t-(7*t**3)/60)/(1+(t**2)/20)

t = np.linspace(-np.pi/2,np.pi/2,100)

fig,ax=plt.subplots(4,1,num=57,figsize=(10,20))


ax[0].plot(t,t,label="t")
ax[0].plot(t,np.sin(t),label="sin")
ax[0].set_title("Semnalul t si sin t")
ax[0].set_xlabel('Timp [s]')
ax[0].set_ylabel('Amplitudine')
ax[0].grid(True)
ax[0].legend()

ax[1].plot(t,np.abs(t-np.sin(t)))
ax[1].set_title("Eroarea |t - sin t|")
ax[1].set_xlabel('Timp [s]')
ax[1].set_ylabel('Amplitudine')
ax[1].grid(True)
ax[1].legend()

ax[2].plot(t,pade(t),label="pade(t)")
ax[2].plot(t,np.sin(t),label="sin(t)")
ax[2].set_title("Semnalul pade(t) si sin t")
ax[2].set_xlabel('Timp [s]')
ax[2].set_ylabel('Amplitudine')
ax[2].grid(True)
ax[2].legend()

ax[3].plot(t,np.abs(t-np.sin(t)))
ax[3].set_title("Eroarea |pade(t) - sin t|")
ax[3].set_xlabel('Timp [s]')
ax[3].set_ylabel('Amplitudine')
ax[3].grid(True)
ax[3].legend()

plt.tight_layout()
#plt.show()
plt.savefig('Graficele la ex8 cu scara y normala.pdf')

fig,ax=plt.subplots(4,1,num=56,figsize=(10,20))


ax[0].set_yscale("log")
ax[0].plot(t,t,label="t")
ax[0].plot(t,np.sin(t),label="sin")
ax[0].set_title("Semnalul t si sin t")
ax[0].set_xlabel('Timp [s]')
ax[0].set_ylabel('Amplitudine (log)')
ax[0].grid(True)
ax[0].legend()

ax[1].set_yscale("log")
ax[1].plot(t,np.abs(t-np.sin(t)))
ax[1].set_title("Eroarea |t - sin t|")
ax[1].set_xlabel('Timp [s]')
ax[1].set_ylabel('Amplitudine (log)')
ax[1].grid(True)
ax[1].legend()

ax[2].set_yscale("log")
ax[2].plot(t,pade(t),label="pade(t)")
ax[2].plot(t,np.sin(t),label="sin(t)")
ax[2].set_title("Semnalul pade(t) si sin t")
ax[2].set_xlabel('Timp [s]')
ax[2].set_ylabel('Amplitudine (log)')
ax[2].grid(True)
ax[2].legend()

ax[3].set_yscale("log")
ax[3].plot(t,np.abs(t-np.sin(t)))
ax[3].set_title("Eroarea |pade(t) - sin t|")
ax[3].set_xlabel('Timp [s]')
ax[3].set_ylabel('Amplitudine (log)')
ax[3].grid(True)
ax[3].legend()

plt.tight_layout()
#plt.show()
plt.savefig('Graficele la ex8 cu scara y logaritmica.pdf')








