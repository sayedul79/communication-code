import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

# Define functions for baseband and carrier signals
def baseband_signal(t, f_m, amplitude=1):
    """Simulates a baseband sinusoid."""
    return amplitude * np.sin(2 * np.pi * f_m * t)

def carrier_signal(t, f_c, amplitude=1):
    """Simulates a carrier sinusoid."""
    return amplitude * np.cos(2 * np.pi * f_c * t)

# Define parameters
f_m = 1000  # Baseband signal frequency
f_c = 10000  # Carrier frequency
amplitude = 1  # Signal amplitude
sample_rate = 100000  # Sampling rate
t = np.arange(0, 1, 1/sample_rate)  # Time samples

# Generate baseband and carrier signals
baseband = baseband_signal(t, f_m, amplitude)
carrier = carrier_signal(t, f_c, amplitude)

# Modulate baseband onto carrier (simple multiplication for this example)
passband = baseband * carrier

fft_baseband = np.fft.fftshift(np.fft.fft(baseband))
fft_carrier = np.fft.fftshift(np.fft.fft(carrier))
fft_passband = np.fft.fftshift(np.fft.fft(passband))

fft_freqs = np.fft.fftshift(np.fft.fftfreq(len(t), 1/sample_rate))

# Plot using fig, ax method
fig, axs = plt.subplots(3, 1, figsize=(10, 6))

# Plot baseband signal
axs[0].plot(t, baseband, color="blue")
axs[0].set_xlabel('Time (s)')
axs[0].set_ylabel('Baseband Signal')
axs[0].set_title(f"Baseband Signal frequency {f_m} Hz")
axs[0].grid(True)
axs[0].set_xlim(0, 3/f_m)

# Plot carrier signal
axs[1].plot(t, carrier, color='red')
axs[1].set_xlabel('Time (s)')
axs[1].set_ylabel('Carrier Signal')
axs[1].set_title(f"Carrier Signal frequency {f_c} Hz")
axs[1].grid(True)
axs[1].set_xlim(0, 3/f_m)

# Plot frequency domain representation
axs[2].plot(fft_freqs, np.abs(fft_baseband), color='blue', label="Baseband Signal")
axs[2].plot(fft_freqs, np.abs(fft_carrier), color='red', label="Carrier Signal")
axs[2].plot(fft_freqs, np.abs(fft_passband), color="green", label="Passband Signal")
axs[2].set_xlabel('Frequency (Hz)')
axs[2].set_ylabel('Magnitude')
#axs[2].legend()
axs[2].set_xlim(-f_c - 2*f_m, f_c + 2*f_m)  # Limit to show both sidebands
axs[2].set_xticks([-f_m-f_c, -f_c, -f_c+f_m, -f_m, 0, f_m, f_c-f_m, f_c, f_c+f_m])  # Setting the positions of the ticks
formatter = FuncFormatter(lambda x, pos: f'{x/1000:g}K')  # Formatting the tick labels to show as 1k, 2k, 3k, etc.
axs[2].xaxis.set_major_formatter(formatter)
#axs[2].set_xticklabels(np.arange(-f_c - 2*f_m, f_c + 2*f_m, 2000))  # Setting the labels of the ticks
axs[2].grid(True)

plt.tight_layout()
plt.show()
