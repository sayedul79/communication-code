import numpy as np
import matplotlib.pyplot as plt

# Parameters
carrier_frequency = 50  # Frequency of the carrier signal in Hz
message_frequency = 5  # Frequency of the message signal in Hz
mesage_amplitude=2
carrier_amplitude=4
modulation_index = mesage_amplitude/carrier_amplitude  # Modulation index

# Time array
t = np.linspace(0, 2, 1000)  # 2 seconds duration

# Carrier signal
carrier_signal = np.sin(2 * np.pi * carrier_frequency * t)

# Message signal
message_signal = np.sin(2 * np.pi * message_frequency * t)

# AM modulation
am_signal = carrier_amplitude*(1 + modulation_index * message_signal) * carrier_signal

# Create figure and axis objects
fig, axs = plt.subplots(3, 1, figsize=(10, 6))

# Plot carrier signal
axs[0].plot(t, carrier_signal, 'b')
axs[0].set_title('Carrier Signal')
axs[0].set_xlabel('Time')
axs[0].set_ylabel('Amplitude')

# Plot message signal
axs[1].plot(t, message_signal, 'g')
axs[1].set_title('Message Signal')
axs[1].set_xlabel('Time')
axs[1].set_ylabel('Amplitude')

# Plot AM signal
axs[2].plot(t, am_signal, 'r')
axs[2].set_title('AM Signal')
axs[2].set_xlabel('Time')
axs[2].set_ylabel('Amplitude')

# Adjust layout
# Set x-axis limits
for ax in axs:
    ax.set_xlim(0, 3/message_frequency)  # Set x-axis limits from 0 to 2

plt.tight_layout()

# Show plot
plt.show()
