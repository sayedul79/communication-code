import numpy as np
import matplotlib.pyplot as plt

# Parameters
t_min = -10
t_max = 10
num_samples = 1000
t = np.linspace(t_min, t_max, num_samples, endpoint=False)
sinc_signal = np.sinc(t)  # Sinc function

# Compute Fourier Transform
sinc_fft = np.fft.fftshift(np.fft.fft(sinc_signal))
freq = np.fft.fftshift(np.fft.fftfreq(num_samples, t[1] - t[0]))

# Plotting
plt.figure(figsize=(10, 6))

# Plot sinc function
plt.subplot(2, 1, 1)
plt.plot(t, sinc_signal, label='Sinc Function', color='blue')
plt.title('Sinc Function')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.grid(True)
plt.legend()

# Plot frequency domain
plt.subplot(2, 1, 2)
plt.plot(freq, np.abs(sinc_fft), label='Magnitude Spectrum', color='red')
plt.title('Frequency Domain (Magnitude Spectrum)')
plt.xlabel('Frequency')
plt.ylabel('Magnitude')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()
