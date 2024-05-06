import numpy as np
import matplotlib.pyplot as plt

# Parameters
message_frequency=5
sampling_rate = 500  # Hz
duration = 2/message_frequency  # seconds
t = np.arange(0, duration, 0.001) # for message signal plot
t_stair=np.arange(0, len(t), 1/sampling_rate) # for staircase plot
# Generate an analog input signal (sine wave)
message_signal = 5*np.sin(2 * np.pi * message_frequency * t) #for message signal plot
input_signal = 5*np.sin(2 * np.pi * message_frequency * t_stair)# for staircase signal generation

# Delta modulation parameters
step_size = 0.3  # Adjust as needed

# Perform delta modulation
output_signal = np.zeros_like(input_signal)
output_signal[0]=-0.5 #initial value
ouput_binary_signal=np.zeros_like(input_signal)
for i in range(1, len(input_signal)):
    if input_signal[i] >= output_signal[i-1]:
        d = 1
        output_signal[i] = output_signal[i-1] + step_size
    else:
        d = 0
        output_signal[i] = output_signal[i-1] - step_size
    ouput_binary_signal[i]=d
# Plot input and output signals
fig, ax=plt.subplots(1, 1, figsize=(10,6))
# ax[0].plot(t, message_signal, label='Analog Input Signal')
# ax[0].step(t_stair, output_signal, label='Staircase Signal', where='post')
# ax[0].step(t_stair, ouput_binary_signal, label='Delta Modulated Output Signal', where="post")
# ax[0].set_xlim(0, 1/message_frequency)
# ax[0].set_xlabel('Time (s)')
# ax[0].set_ylabel('Amplitude')
# ax[0].set_title('Delta Modulation')
# ax[0].legend()
# ax[0].grid(True)

# ax[1].step(t_stair, ouput_binary_signal, where="post")
# ax[1].set_xlim(0, 1/message_frequency)
# ax[1].set_title('Delta Modulated Signal')
# ax[1].set_xlabel('Time (s)')
# ax[1].set_ylabel('Digital Value')

ax.plot(t, message_signal, label='Analog Input Signal')
ax.step(t_stair, output_signal, color="darkorange", label='Staircase Signal', where='post')
ax.step(t_stair, ouput_binary_signal, color="green", label='Delta Modulated Output Signal', where="post")
ax.set_xlim(0, 1/message_frequency)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Amplitude')
ax.set_title('Delta Modulation')
ax.legend()
ax.grid(True)
plt.tight_layout()
plt.grid(True)

plt.show()
