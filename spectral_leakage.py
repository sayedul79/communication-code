import numpy as np
import matplotlib.pyplot as plt
#change axs[2].set_xlim to visualize

# Define sampling frequency (Fs)
Fs = 2000

# Define number of data points (N) for two cases
N1 = 4080
N2 = 4096

# Create time vectors (t) based on Fs and N
t1 = np.linspace(0, N1, N1) / Fs
t2 = np.linspace(0, N2, N2) / Fs

# Generate sine wave signals (y, x2) with frequency 100 Hz
f0=100
signal_1 = np.sin(2*np.pi * f0 * t1)
signal_2 = np.sin(2*np.pi * f0 * t2)

# Calculate FFTs (signal_1, signal_2) and frequency vectors (f1, f2)
signal_1_fft = np.fft.fftshift(np.fft.fft(signal_1)) / np.sqrt(N1)
f1=np.fft.fftshift(np.fft.fftfreq(N1, 1/Fs))/N1
#f1 = Fs * np.linspace(0, 1, N1)/N1

signal_2_fft = np.fft.fftshift(np.fft.fft(signal_2)) / np.sqrt(N2)
f2=np.fft.fftshift(np.fft.fftfreq(N2, 1/Fs))/N2
#f2 = Fs * np.linspace(0, 1, N2)/N2

cycle=int(t1[-1]*f0) #number of cycle in the signal
# Plot the last 0.04 seconds of the signals
fig, axs = plt.subplots(3, 1, figsize=(10, 6))

axs[0].plot(t1[t1 >= (cycle-2)/f0], signal_1[t1 >= (cycle-2)/f0]) #draw last two cycle to end
axs[0].set_xlabel('t(sec)')
axs[0].set_ylabel('x(t)')
axs[0].set_title('The last cycle of x(t) when N=4080')
axs[0].grid(True)

axs[1].plot(t2[t2 >= (cycle-2)/f0], signal_2[t2 >= (cycle-2)/f0]) #draw last twocycle two enc
axs[1].set_xlabel('t(sec)')
axs[1].set_ylabel('x(t)')
axs[1].set_title('The last cycle of x(t) when N=4096')
axs[1].grid(True)

axs[2].plot(f1*N1, np.abs(signal_1_fft))
axs[2].plot(f2*N2, np.abs(signal_2_fft))
#axs[2].set_xlim(70, 140)
axs[2].legend(['N=4080', 'N=4096'])
axs[2].set_xlabel('Frequency (Hz)')
axs[2].set_ylabel('Magnitude')
axs[2].set_title('FFT of x(t) with different N')
axs[2].grid(True)

plt.tight_layout()
plt.show()
