import numpy as np
import matplotlib.pyplot as plt

# Parameters
quantization_levels = 8  # Number of quantization levels
signal_range = 2  # Range of the signal (-signal_range to signal_range)
sampling_freq = 1000  # Sampling frequency in Hz
duration = 1  # Duration of the signal in seconds
sampling_period=1/sampling_freq

# Generate analog signal (e.g., a sine wave)
# t = np.linspace(0, duration, int(sampling_freq * duration), endpoint=False)
t = np.arange(0, duration, sampling_period)
analog_signal = np.sin(2 * np.pi * 5 * t)  # 5 Hz sine wave

# Sample the analog signal
sampled_signal = analog_signal # প্লট করতে গেলে হিজিবিজি হয়ে যায় তাই নিচের পদ্ধতি for sampling signal plot

sampling_indices = np.arange(0, len(analog_signal), 10)  # Sample every 10th point for simplicity
sampled_signal_plot = analog_signal[sampling_indices]
sampled_times = t[sampling_indices]

# Quantization
quantization_step = signal_range / quantization_levels  # Calculate quantization step size
quantized_signal = np.round(sampled_signal / quantization_step) * quantization_step

# Plotting
plt.figure(figsize=(10, 6))

# Analog Signal
plt.plot(t, analog_signal, label='Analog Signal', color='red', linewidth=2)

# Sampled Signal
#plt.stem(t, sampled_signal, label='Sampled Signal', markerfmt='ro', basefmt=" ", linefmt='r-') #হিজিবিজি ওয়ালা
plt.stem(sampled_times, sampled_signal_plot,
	markerfmt='ko', 
	basefmt=" ", 
	linefmt='k-', 
	label='Sampled Signal')
# plt.plot(t, sampled_signal, label='Sampled Signal') 
plt.title('Sampled Signal')
# Quantized Signal
#plt.stem(t, quantized_signal, label='Quantized Signal', markerfmt='go', basefmt=" ", linefmt='g-')
plt.plot(t, quantized_signal, label='Quantized Signal', color="blue", linewidth=2)
plt.title('Quantized Signal')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.legend()

#plot quantization labels line
for level in np.arange(-quantization_levels/2,quantization_levels/2+1,):
    plt.axhline(y=level * quantization_step, color='black', alpha=0.4)
plt.xlim(0,0.4)
plt.tight_layout()
plt.show()
