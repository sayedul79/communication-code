import numpy as np
import matplotlib.pyplot as plt

# Sample size (adjust as needed)
N = 1000

# Generate white noise (limited bandwidth)
white_noise = 5*np.random.rand(N)

# Sampling frequency (adjust as needed)
fs = 1000  # Hz

# Calculate PSD using FFT (assuming real signal)
fft_freqs = np.fft.fftfreq(N, d=1/fs)[:N//2]  # Positive frequencies only
psd = np.abs(np.fft.fft(white_noise))[:N//2] * 2 / fs  # Double-sided PSD

# Plot the PSD (limited by sampling frequency)
plt.plot(fft_freqs, psd)
plt.xlabel('Frequency (Hz)')
plt.ylabel('Power Spectral Density (units^2/Hz)')
plt.title('PSD of (limited bandwidth) white noise')
plt.xlim(0, fs/2)  # Limit x-axis to half the sampling frequency (Nyquist limit)
plt.ylim(0, 0.5)
plt.show()