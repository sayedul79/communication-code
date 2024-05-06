import numpy as np
import matplotlib.pyplot as plt

# Generate some sample data (sine wave)
fs = 1000  # Sampling frequency
t = np.arange(0, 1, 1/fs)  # Time vector from 0 to 1 second
f1 = 50  # Frequency of the sine wave in Hz
signal = np.sin(2 * np.pi * f1 * t)+np.cos(2*np.pi*100*t)

# Compute the FFT
fft_output = np.fft.fft(signal)
n = len(signal)
freq = np.fft.fftfreq(n, 1/fs)  # Frequency bins

# Plot the frequency spectrum
plt.figure(figsize=(8, 4))
plt.plot(freq[:n//2], np.abs(fft_output)[:n//2])  # Plot only positive frequencies
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.title('Frequency Spectrum')
plt.xlim(0, 200)
plt.tight_layout()
plt.grid(True)
plt.show()
