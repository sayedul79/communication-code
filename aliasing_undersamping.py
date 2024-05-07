import numpy as np
import matplotlib.pyplot as plt

# Define signal parameters
f0 = 100  # Hz, fundamental frequency of the signal
fs = 50   # Hz, sampling frequency

# Simulate a simple sine wave as the signal
t = np.linspace(0, 1, 1000)  # Time vector
x = np.sin(2*np.pi*f0*t)  

# Calculate the original signal's spectrum (Fourier Transform)
fft_x = np.fft.fft(x)
freqs = np.fft.fftfreq(len(x), d=t[1] - t[0])  # Corresponding frequencies

# Undersampling: Select only a portion of the data for a lower effective sampling rate
decimation_factor = 2  # How much to reduce the sampling rate
sampled_x = x[::decimation_factor]
effective_fs = fs / decimation_factor  # Effective sampling rate after decimation

# Calculate the undersampled signal's spectrum
fft_sampled_x = np.fft.fft(sampled_x)
freqs_sampled = np.fft.fftfreq(len(sampled_x), d=1/effective_fs)  # Frequencies for undersampled data

# Plot the results
plt.figure(figsize=(10, 6))

# Original spectrum
plt.plot(freqs, np.abs(fft_x), label='Original Spectrum')
plt.axvline(x=f0, color='r', linestyle='--', label='f0')  # Mark fundamental frequency
plt.axvline(x=-f0, color='r', linestyle='--')

# Undersampled spectrum (shifted and potentially aliased)
plt.plot(freqs_sampled, np.abs(fft_sampled_x), label='Undersampled Spectrum')
#plt.axvline(x=effective_fs/2, color='g', linestyle='--', label='f_s/2 (Nyquist)')
#plt.axvline(x=-effective_fs/2, color='g', linestyle='--')

plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude (FFT)')
plt.title('Original vs. Undersampled Signal Spectrum')
plt.legend()
plt.grid(True)
plt.xlim(-effective_fs-f0, effective_fs+f0)  # Adjust x-axis limits for better visualization

plt.show()