import numpy as np
import matplotlib.pyplot as plt

# Parameters
sampling_freq = 1000  # Sampling frequency (Hz)
message_freq=5
carrier_freq = 20     # Carrier frequency (Hz)
phase_sensitivity_factor = 10  # Phase Sensitivity factor
duration = 10/message_freq          # Duration of the signal (seconds)
t = np.linspace(0, duration, int(sampling_freq * duration))

# Modulating signal (sine wave)
modulating_signal = np.sin(2 * np.pi * message_freq * t)  # 5 Hz sine wave

# Carrier signal (sine wave)
carrier_signal = np.sin(2 * np.pi * carrier_freq * t)

# Phase modulation
phase_modulated_signal = np.sin(2 * np.pi * carrier_freq * t + phase_sensitivity_factor * modulating_signal)

# Plot signals
fig, axs = plt.subplots(3, 1, figsize=(10, 6))

axs[0].plot(t, carrier_signal)
axs[0].set_title('Carrier Signal')
axs[0].set_xlabel('Time')
axs[0].set_ylabel('Amplitude')

axs[1].plot(t, modulating_signal, color="blue")
axs[1].set_title('Modulating Signal')
axs[1].set_xlabel('Time')
axs[1].set_ylabel('Amplitude')

axs[2].plot(t, phase_modulated_signal, color="Green")
axs[2].set_title('Phase Modulated Signal')
axs[2].set_xlabel('Time')
axs[2].set_ylabel('Amplitude')

for ax in axs:
    ax.set_xlim(4/message_freq, 8/message_freq)  # Set x-axis limits from 0 to 4*message signal period
plt.tight_layout()
plt.show()
