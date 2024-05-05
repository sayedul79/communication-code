import numpy as np
import matplotlib.pyplot as plt

# Parameters
carrier_frequency = 100  # Frequency of the carrier signal in Hz
message_frequency = 10  # Frequency of the message signal in Hz
modulation_index = 5  # Modulation index

# Time array
t = np.linspace(0, 10/message_frequency, 10*1000)  # seconds duration

# Carrier signal
carrier_signal = np.sin(2 * np.pi * carrier_frequency * t)

# Message signal
message_signal = np.sin(2 * np.pi * message_frequency * t)

# FM modulation
fm_signal = np.sin(2 * np.pi * (carrier_frequency + modulation_index * message_signal) * t)

# Create figure and axis objects
fig, axs = plt.subplots(3, 1, figsize=(10, 6))

# Plot carrier signal
axs[0].plot(t, carrier_signal)
axs[0].set_title('Carrier Signal')
axs[0].set_xlabel('Time')
axs[0].set_ylabel('Amplitude')

# Plot message signal
axs[1].plot(t, message_signal, 'b')
axs[1].set_title('Message Signal')
axs[1].set_xlabel('Time')
axs[1].set_ylabel('Amplitude')

# Plot FM signal
axs[2].plot(t, fm_signal, 'g')
axs[2].set_title('FM Signal')
axs[2].set_xlabel('Time')
axs[2].set_ylabel('Amplitude')

# Adjust layout
for ax in axs:
    ax.set_xlim(2/message_frequency, 8/message_frequency)  # Set x-axis limits from 0 to 2
plt.tight_layout()

# Show plot
plt.show()
