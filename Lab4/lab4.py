# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 16:11:56 2026

@author: User
"""

# EX 1

import matplotlib.pyplot as plt
import numpy as np
import time

A = 3
fr = 2 
phi = np.pi/3
s = lambda t : A*np.sin(2*np.pi*fr*t + phi)


fig, ax = plt.subplots(2, 1, num=54482, figsize=(10, 10))

# DFT

N = [128,256,512,1024,2048,4096,8192]

# F = np.zeros((N,N),dtype=complex)
# for m in range(N):
#     for k in range(N):
#         F[m][k] = np.exp(-2*np.pi*1j*k*m/N)

# F = np.exp(-2*np.pi*1j*np.outer(np.linspace(0, N-1,N) , np.linspace(0, N-1,N))/N)


print()
print("TABELUL PENTRU DFT")
print()
print(f"{"N":^10}|{"timp (s)":^10}")

ax[0].set_title("DFT")
ax[0].set_xlabel("N")
ax[0].set_ylabel("Timp (log)")
ax[0].set_yscale("log")

T_DFT = []

for n in N:
    F = np.exp(-2*np.pi*1j*np.outer(np.arange(n) , np.arange(n))/n)
    t = np.linspace(0,1,n)
    x = s(t)
    #DFT start
    start_time = time.perf_counter()
    X = F@x
    end_time = time.perf_counter()
    #DFT end    
    elapsed_time = end_time - start_time
    T_DFT.append(elapsed_time)
    print(f"{n:^10}|{elapsed_time:^10.6e}")
print()

ax[0].scatter(N,T_DFT)


# FFT

def my_fft(x):
    # Algoritmul Cooley-Turkey Radix-2
    N = x.shape[0]
    
    if N<=1:
        return x
    
    if N & (N-1) != 0:
        raise ValueError("Lungimea vectorului x nu este o putere a lui 2")
    
    even = my_fft(x[0::2])
    odd = my_fft(x[1::2])
    
    factor = np.exp(-2j*np.pi*np.arange(N//2)/N)
    
    term = factor*odd
    
    return np.concatenate([even + term, even - term])



print()
print("TABELUL PENTRU FFT")
print()
print(f"{"N":^10}|{"timp (s)":^10}")

ax[1].set_title("FFT")
ax[1].set_xlabel("N")
ax[1].set_ylabel("Timp (log)")
ax[1].set_yscale("log")

T_FFT = []

for n in N:
    F = np.exp(-2*np.pi*1j*np.outer(np.arange(n) , np.arange(n))/n)
    t = np.linspace(0,1,n)
    x = s(t)
    #DFT start
    start_time = time.perf_counter()
    X = my_fft(x)
    end_time = time.perf_counter()
    #DFT end    
    elapsed_time = end_time - start_time
    T_FFT.append(elapsed_time)
    print(f"{n:^10}|{elapsed_time:^10.6e}")
print()

ax[1].scatter(N,T_FFT)

plt.tight_layout()
plt.savefig("Figura la ex1.pdf")


#%%
# EX 2

import numpy as np
import matplotlib.pyplot as plt

# ==================================
# Parametri
# ==================================

f0 = 5      # frecventa initiala
fs = 7      # frecventa de esantionare (sub Nyquist)

n_signals = 4   # cate semnale afisam

ts = 1 / fs

# timp continuu
t = np.linspace(0, 2, 3000)

# momente de esantionare
n = np.arange(15)
t_sample = n * ts

# ==================================
# Figura
# ==================================

fig, axs = plt.subplots(
    n_signals,
    1,
    figsize=(12, 3 * n_signals),
    sharex=True
)

# daca avem un singur subplot
if n_signals == 1:
    axs = [axs]

for k in range(n_signals):

    f = f0 + k * fs

    # semnal continuu
    x = np.sin(2 * np.pi * f * t)

    # esantioane
    xs = np.sin(2 * np.pi * f * t_sample)

    axs[k].plot(
        t,
        x,
        linewidth=2,
        label=f"f = {f0} + {k}·{fs} = {f} Hz"
    )

    axs[k].stem(
        t_sample,
        xs,
        linefmt="r-",
        markerfmt="ro",
        basefmt="k-"
    )

    axs[k].grid(True)
    axs[k].legend()

plt.suptitle(
    f"Aliasing pentru f0 = {f0} Hz si fs = {fs} Hz",
    fontsize=14
)

plt.xlabel("Timp (s)")
plt.tight_layout()
plt.savefig("Figura la ex2.pdf")
plt.show()


#%%
# EX 3

import numpy as np
import matplotlib.pyplot as plt

f0 = 5
fs = 20          # peste Nyquist
n_signals = 3

T = 2            # durata observatiei
N = int(fs * T)

t = np.arange(N) / fs

fig, axs = plt.subplots(
    n_signals,
    2,
    figsize=(12, 8)
)

for k in range(n_signals):

    f = f0 + k * fs

    x = np.sin(2 * np.pi * f * t)

    X = np.fft.fft(x)
    freq = np.fft.fftfreq(N, d=1/fs)

    positive = freq >= 0

    axs[k, 0].stem(
        t,
        x,
        basefmt=" "
    )

    axs[k, 0].set_title(
        f"Semnal esantionat: f={f} Hz"
    )

    axs[k, 0].set_xlabel("Timp [s]")
    axs[k, 0].set_ylabel("Amplitudine")
    axs[k, 0].grid(True)

    axs[k, 1].plot(
        freq[positive],
        np.abs(X)[positive]
    )

    axs[k, 1].set_title(
        f"FFT: f={f} Hz"
    )

    axs[k, 1].set_xlabel("Frecventa [Hz]")
    axs[k, 1].set_ylabel("|X(f)|")
    axs[k, 1].grid(True)

plt.suptitle(
    "Demonstratie fara aliasing folosind FFT"
)

plt.tight_layout()
plt.savefig("Figura_ex3_FFT.pdf")
plt.show()


#%%


# Exercitiul 4
#
# Frecventele produse de contrabas sunt cuprinse intre 40 Hz si 200 Hz.
# Prin urmare, cea mai mare frecventa prezenta in semnal este:
#
# B = 200 Hz
#
# Conform teoremei Nyquist-Shannon:
#
#     fs >= 2B
#
# unde:
#     fs = frecventa de esantionare
#     B  = frecventa maxima continuta in semnal
#
# Inlocuind:
#
#     fs >= 2 * 200
#     fs >= 400 Hz
#
# Rezultat:
#
# Frecventa minima de esantionare este 400 Hz.
#
# Daca fs < 400 Hz apare fenomenul de aliasing,
# iar unele componente de frecventa ale contrabasului
# nu vor mai putea fi reconstruite corect.
#
# Raspuns final:
#
#     fs_min = 400 Hz
#


#%%
# EX 5
import numpy as np
import matplotlib.pyplot as plt

vowels = {
    "a": [700, 1200],
    "e": [500, 1900],
    "i": [300, 2500],
    "o": [500, 900],
    "u": [350, 800]
}

fig, axs = plt.subplots(5, 1, figsize=(8, 10))

freqs = np.linspace(0, 3000, 500)
times = np.linspace(0, 1, 100)

for ax, (vowel, formants) in zip(axs, vowels.items()):

    S = np.zeros((len(freqs), len(times)))

    for f in formants:
        S += np.exp(-(freqs[:, None] - f) ** 2 / (2 * 80 ** 2))

    ax.imshow(
        S,
        aspect="auto",
        origin="lower",
        extent=[0, 1, 0, 3000],
        cmap="magma"
    )

    ax.set_title(f'Vocala "{vowel}"')
    ax.set_ylabel("Hz")

axs[-1].set_xlabel("Timp [s]")

plt.tight_layout()
plt.savefig("Spectrograme_vocale.pdf")
plt.show()

#%%
# EX 5 - Spectrograme sintetice pentru vocalele a, e, i, o, u
# Frecvența este afișată pe scară logaritmică

import numpy as np
import matplotlib.pyplot as plt

vowels = {
    "a": [700, 1200],
    "e": [500, 1900],
    "i": [300, 2500],
    "o": [500, 900],
    "u": [350, 800]
}

fig, axs = plt.subplots(5, 1, figsize=(8, 10))

# frecvențe pe scară logaritmică
freqs = np.logspace(np.log10(50), np.log10(3000), 500)

times = np.linspace(0, 1, 100)

for ax, (vowel, formants) in zip(axs, vowels.items()):

    S = np.zeros((len(freqs), len(times)))

    # for f in formants:
    #     S += np.exp(
    #         -(freqs[:, None] - f) ** 2 /
    #         (2 * 80 ** 2)
    #     )
    
    for f in formants:
        S += np.exp(
            -(freqs[:, None] - f) ** 2 /
            (2 * 80 ** 2)
        ) * (1 + 0.1 * np.random.randn(1, len(times)))

    ax.pcolormesh(
        times,
        freqs,
        S,
        shading="auto",
        cmap="magma"
    )

    ax.set_yscale("log")

    ax.set_title(f'Vocala "{vowel}"')
    ax.set_ylabel("Hz (log)")

    ax.set_yticks([100, 200, 500, 1000, 2000, 3000])
    ax.get_yaxis().set_major_formatter(
        plt.ScalarFormatter()
    )

axs[-1].set_xlabel("Timp [s]")

plt.tight_layout()

plt.savefig(
    "Spectrograme_vocale.pdf",
    bbox_inches="tight"
)

plt.show()
#%%
#extra
import numpy as np
from scipy.io import wavfile

def genereaza_vocala_a(
        filename="vocala_a.wav",
        durata=2,
        fs=44100):

    t = np.linspace(
        0,
        durata,
        int(fs * durata),
        endpoint=False
    )

    # frecventa fundamentala (voce)
    F0 = 120

    # formanti aproximativi pentru "a"
    F1 = 700
    F2 = 1200
    F3 = 2600

    x = (
        1.0 * np.sin(2 * np.pi * F0 * t)
        + 0.8 * np.sin(2 * np.pi * F1 * t)
        + 0.5 * np.sin(2 * np.pi * F2 * t)
        + 0.3 * np.sin(2 * np.pi * F3 * t)
    )

    x /= np.max(np.abs(x))

    wavfile.write(
        filename,
        fs,
        (x * 32767).astype(np.int16)
    )

genereaza_vocala_a()
#%%
# EX 6
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

# =====================================
# (a) Citirea semnalului audio
# =====================================

fs, s = wavfile.read("vocala_a.wav")

# daca semnalul este stereo
if len(s.shape) > 1:
    s = s[:, 0]

s = s.astype(float)

N = len(s)

# =====================================
# (b) Grupuri de 1% cu overlap 50%
# =====================================

window_size = int(0.01 * N)

# 50% overlap
step = window_size // 2

# =====================================
# (c) FFT pentru fiecare grup
# =====================================

spectrogram = []

for start in range(0, N - window_size, step):

    segment = s[start:start + window_size]

    # optional: fereastra Hann
    segment = segment * np.hanning(window_size)

    X = np.fft.fft(segment)

    # (d) valoare absoluta
    spectrogram.append(np.abs(X[:window_size // 2]))

# fiecare coloana = un FFT
spectrogram = np.array(spectrogram).T

# =====================================
# (e) Afisarea spectrogramei
# =====================================

plt.figure(figsize=(10, 6))

plt.imshow(
    spectrogram,
    aspect='auto',
    origin='lower',
    cmap='magma'
)

plt.colorbar(label='Amplitudine')

plt.xlabel('Fereastra temporala')
plt.ylabel('Indice frecventa')
plt.title('Spectrograma construita manual')

plt.tight_layout()
plt.savefig("spectrograma.pdf")
plt.show()


#%%
# EX 6

import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

# =====================================
# (a) Citirea semnalului audio
# =====================================

fs, s = wavfile.read(
    r"C:\Users\User\OneDrive\Desktop\Procesarea Semnalelor\Lab4\a.wav"
)

# dacă este stereo -> păstrăm un singur canal
if len(s.shape) > 1:
    s = s[:, 0]

s = s.astype(float)

N = len(s)

# =====================================
# (b) Grupuri de 1% cu overlap 50%
# =====================================

window_size = int(0.01 * N)
step = window_size // 2

# =====================================
# (c) FFT pentru fiecare grup
# =====================================

spectrogram = []

for start in range(0, N - window_size, step):

    segment = s[start:start + window_size]

    # fereastră Hann
    segment = segment * np.hanning(window_size)

    X = np.fft.rfft(segment)

    spectrogram.append(np.abs(X))

spectrogram = np.array(spectrogram).T

# =====================================
# Axe reale
# =====================================

freqs = np.fft.rfftfreq(window_size, d=1/fs)

times = np.arange(spectrogram.shape[1]) * step / fs

# =====================================
# (d) Afișare
# =====================================

plt.figure(figsize=(10, 6))

plt.pcolormesh(
    times,
    freqs,
    20 * np.log10(spectrogram + 1e-10),
    shading="auto",
    cmap="magma"
)

plt.yscale("log")
plt.ylim(50, 16000)

plt.colorbar(label="Amplitudine [dB]")

plt.xlabel("Timp [s]")
plt.ylabel("Frecvență [Hz]")
plt.title('Spectrograma vocalei "a"')

plt.tight_layout()

plt.savefig("spectrograma.pdf")

plt.show()
#%%

# Exercitiul 7
#
# Se cunosc:
#
# P_semnal = 90 dB
# SNR_dB = 80 dB
#
# Formula raportului semnal-zgomot este:
#
# SNR_dB = P_semnal_dB - P_zgomot_dB
#
# Inlocuind valorile:
#
# 80 = 90 - P_zgomot
#
# P_zgomot = 90 - 80
#
# P_zgomot = 10 dB
#
# Raspuns:
#
# Puterea zgomotului este 10 dB.
#









