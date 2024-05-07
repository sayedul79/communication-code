import numpy as np
import matplotlib.pyplot as plt

# Signal parameters
f1 = 50  # Frequency of the sinusoidal signal in Hz
f2=250
amplitude = 1   # Amplitude of the sinusoidal signal
period_original_signal=np.lcm(1,1)/np.gcd(f1,f2)
duration = 1    # Duration of the signal in seconds
sampling_rate = 1000  # Sampling rate in Hz

# Generate time array
t = np.linspace(0, duration, int(duration*sampling_rate))

# Generate the original sinusoidal signal
t_plot= np.linspace(0, 2*period_original_signal, 1000)
original_signal_plot=amplitude*np.sin(2 * np.pi * f1 * t_plot) + amplitude*np.sin(2 * np.pi * f2 * t_plot)
#original_signal_plot নিছি যাতে স্মুথলি সিগ্নাল্টা প্লট করা যায়
original_signal = amplitude*np.sin(2 * np.pi * f1 * t) + amplitude*np.sin(2 * np.pi * f2 * t)
#original_signal কে plt.plot দিয়ে স্মুথলি প্লট করা যায় না কারন পয়েন্ট পর্যাপ্ত না

# Calculate the Discrete Fourier Transform (DFT) of the original signal
original_fft = np.fft.fftshift(np.fft.fft(original_signal))
frequencies = np.fft.fftshift(np.fft.fftfreq(len(original_signal), 1 / sampling_rate))

# Plot the original signal in time domain
plt.figure(figsize=(10, 7))
plt.subplot(2, 2, 1)
plt.plot(t_plot, original_signal_plot)
plt.title('Original Signal (Time Domain)')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.xlim(0, 2*period_original_signal)

# Plot the magnitude spectrum of the original signal
plt.subplot(2, 2, 2)
plt.plot(frequencies, np.abs(original_fft))
plt.title('Magnitude Spectrum of Original Signal')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')

# Undersample the signal by reducing the sampling rate
undersampled_sampling_rate = 350  # Lower sampling rate
undersampled_t = np.linspace(0, duration, int(duration * undersampled_sampling_rate))
undersampled_signal = amplitude *np.sin(2 * np.pi * f1 * undersampled_t) + amplitude*np.sin(2 * np.pi * f2 * undersampled_t)

# Calculate the DFT of the undersampled signal
undersampled_fft = np.fft.fftshift(np.fft.fft(undersampled_signal))
undersampled_frequencies = np.fft.fftshift(np.fft.fftfreq(len(undersampled_signal), 1 / undersampled_sampling_rate))

# Plot the undersampled signal in time domain
plt.subplot(2, 2, 3)
plt.stem(undersampled_t, undersampled_signal, markerfmt='ro', linefmt='r-', basefmt='r-', label='Undersampled Signal')
plt.title('Undersampled Signal (Time Domain)')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.xlim(0, 7*period_original_signal)
# Plot the magnitude spectrum of the undersampled signal
plt.subplot(2, 2, 4)
plt.plot(undersampled_frequencies, np.abs(undersampled_fft), 'r')
plt.title('Magnitude Spectrum of Undersampled Signal')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')

plt.tight_layout()
plt.show()
