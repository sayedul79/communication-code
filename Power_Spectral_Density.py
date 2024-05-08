import numpy as np
from scipy.signal import welch

# Sampling frequency
fs = 1000  # Hz
t = np.linspace(0, 1, 1000)  # 1 second duration with 1000 samples
# Sample data (replace with your actual data)
data = np.sin(2*np.pi*10*t) + 5*np.random.rand(1000)  # 10Hz sine wave with noise

# Welch method for PSD estimation
freqs, psd = welch(data, fs, nperseg=512)  # Adjust nperseg for desired frequency resolution

# Plot the PSD
import matplotlib.pyplot as plt

plt.plot(freqs, psd)
plt.xlabel('Frequency (Hz)')
plt.ylabel('Power Spectral Density (units^2/Hz)')
plt.title('PSD of the signal')
plt.show()