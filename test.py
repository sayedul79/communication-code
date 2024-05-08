




# import numpy as np
# import matplotlib.pyplot as plt

# # Define original signal parameters (sine wave)
# fs_original = 1000  # Original sampling frequency (Hz)
# t = np.arange(0, 1, 1/fs_original)  # Time vector
# f1 = 50  # Signal frequency (Hz)
# f2 = 250  # Higher frequency component (Hz) - This component will be affected by undersampling

# # Generate the signal with two frequencies
# signal = np.sin(2 * np.pi * f1 * t) + np.sin(2 * np.pi * f2 * t)

# # Function for calculating the Discrete Fourier Transform (DFT)
# def DFT(x, n=None):
#     N = len(x)
#     k = np.arange(N)
#     return np.fft.fft(x, n) / N

# # Calculate original signal's DFT
# original_fft = DFT(signal)

# # Original frequency axis (shifted for visualization)
# f_original = np.fft.fftshift(np.fft.fftfreq(len(signal), 1/fs_original))

# # Define an undersampling rate (lower than Nyquist for f2)
# undersample_rate = 300

# # Calculate DFT for undersampled signal (zero-pad for same FFT size)
# undersampled_signal = signal[::int(fs_original/undersample_rate)]  # Downsample by selecting every nth sample
# undersampled_fft = DFT(undersampled_signal, n=len(signal))  # Zero-pad for same FFT size

# # Undersampled frequency axis (shifted)
# f_undersampled = np.fft.fftshift(np.fft.fftfreq(len(undersampled_fft), 1/undersample_rate))

# # Plot results (original vs undersampled)
# plt.figure(figsize=(12, 6))

# plt.subplot(2, 1, 1)
# plt.plot(f_original, np.abs(original_fft))
# plt.xlabel('Frequency (Hz)')
# plt.ylabel('Magnitude')
# plt.title('Original Signal Spectrum (f1, f2)')
# plt.xlim(-fs_original/2, fs_original/2)
# plt.grid(True)

# plt.subplot(2, 1, 2)
# plt.plot(f_undersampled, np.abs(undersampled_fft))
# plt.xlabel('Frequency (Hz)')
# plt.ylabel('Magnitude')
# plt.title('Undersampled Spectrum (Aliasing of f2)')
# plt.xlim(-undersample_rate/2, undersample_rate/2)
# plt.grid(True)

# plt.tight_layout()
# plt.show()
 

# import numpy as np
# import matplotlib.pyplot as plt

# # Define signal parameters
# f0 = 100  # Hz, center frequency of the bandwidth signal
# B = 200  # Hz, bandwidth of the signal
# fs = 1000  # Hz, sampling frequency

# # Create time vector
# t = np.linspace(0, 1, fs)  # One second duration

# # Generate ideal bandwidth signal (rectangular in frequency domain)
# bandwidth_signal = np.sinc(2*B*t)  # sinc function for bandlimited signal

# # Calculate the signal's spectrum (Fourier Transform)
# fft_bandwidth_signal = np.fft.fftshift(np.fft.fft(bandwidth_signal))
# freqs = np.fft.fftshift(np.fft.fftfreq(len(bandwidth_signal), d=1/fs))  # Corresponding frequencies

# # Plot the time domain signal and its frequency spectrum
# plt.figure(figsize=(10, 6))

# plt.subplot(2, 1, 1)
# plt.plot(t, bandwidth_signal)
# plt.xlabel('Time (s)')
# plt.ylabel('Signal')
# plt.title('Bandwidth Signal (Time Domain)')
# plt.grid(True)

# plt.subplot(2, 1, 2)
# plt.plot(freqs, np.abs(fft_bandwidth_signal))
# plt.xlabel('Frequency (Hz)')
# ylabel = 'Magnitude (FFT)'
# plt.title(ylabel)
# #plt.xlim(-fs/2, fs/2)  # Adjust x-axis for entire spectrum
# plt.grid(True)

# plt.tight_layout()
# plt.show()

# import numpy as np
# import matplotlib.pyplot as plt

# # Define signal parameters
# f0 = 100  # Hz, center frequency of the bandwidth signal
# B = 200  # Hz, bandwidth of the signal
# fs = 1000  # Hz, sampling frequency

# # Create time vector
# t = np.linspace(0, 1, fs)  # One second duration

# # Generate ideal bandwidth signal (rectangular in frequency domain)
# bandwidth_signal = np.sinc(2*B*t)  # sinc function for bandlimited signal

# # Calculate the signal's spectrum (Fourier Transform)
# fft_bandwidth_signal = np.fft.fftshift(np.fft.fft(bandwidth_signal))
# freqs = np.fft.fftshift(np.fft.fftfreq(len(bandwidth_signal), d=1/fs))  # Corresponding frequencies

# # Undersampling: Select only a portion of the data for a lower effective sampling rate
# decimation_factor = 2  # How much to reduce the sampling rate
# sampled_bandwidth_signal = bandwidth_signal[::decimation_factor]
# effective_fs = fs / decimation_factor  # Effective sampling rate after decimation

# # Calculate the undersampled signal's spectrum
# fft_sampled_bandwidth_signal = np.fft.fftshift(np.fft.fft(sampled_bandwidth_signal))
# freqs_sampled = np.fft.fftshift(np.fft.fftfreq(len(sampled_bandwidth_signal), d=1/effective_fs))  # Frequencies for undersampled data

# # Plot the results
# plt.figure(figsize=(10, 8))

# # Original spectrum
# plt.subplot(2, 1, 1)
# plt.plot(freqs, np.abs(fft_bandwidth_signal))
# plt.xlabel('Frequency (Hz)')
# plt.ylabel('Magnitude (FFT)')
# plt.title('Original Signal Spectrum')
# plt.grid(True)

# # Undersampled spectrum
# plt.subplot(2, 1, 2)
# plt.plot(freqs_sampled, np.abs(fft_sampled_bandwidth_signal))
# plt.xlabel('Frequency (Hz)')
# plt.ylabel('Magnitude (FFT)')
# plt.title('Undersampled Signal Spectrum (Decimation Factor: {})'.format(decimation_factor))
# plt.grid(True)

# # Adjust x-axis limits for the undersampled spectrum plot
# plt.xlim(-effective_fs / 2, effective_fs / 2)

# plt.tight_layout()
# plt.show()


#sampling effect at frequency domain
# import numpy as np
# import matplotlib.pyplot as plt

# # Define signal parameters
# f0 = 50  # Hz, frequency of the original signal
# fs = 500  # Hz, sampling frequency
# duration = 1  # Duration of the signal in seconds

# # Time vector
# t = np.linspace(0, duration, int(fs * duration), endpoint=False)  # Time vector

# # Create impulse train representing the sampling process
# impulse_train = np.zeros_like(t)
# impulse_train[::int(fs/f0)] = 1  # Impulse train with frequency equal to the original signal

# # Calculate the FFT of the impulse train
# fft_impulse_train = np.fft.fftshift(np.fft.fft(impulse_train))
# freqs = np.fft.fftshift(np.fft.fftfreq(len(impulse_train), d=1/fs))  # Corresponding frequencies

# # Generate a multi-tone signal (for example, a sum of two sine waves)
# f1 = 50  # Hz, frequency of the first tone
# f2 = 200  # Hz, frequency of the second tone
# multi_tone_signal = np.sin(2 * np.pi * f1 * t) + np.sin(2 * np.pi * f2 * t)

# # Calculate the FFT of the multi-tone signal
# fft_multi_tone_signal = np.fft.fftshift(np.fft.fft(multi_tone_signal))

# # Multiply the spectrum of the multi-tone signal with the spectrum of the impulse train
# combined_spectrum = fft_multi_tone_signal * fft_impulse_train

# # Plot the results
# plt.figure(figsize=(10, 6))

# # Plot the frequency spectrum of the multi-tone signal
# plt.subplot(3, 1, 1)
# plt.plot(freqs, np.abs(fft_multi_tone_signal))
# plt.xlabel('Frequency (Hz)')
# plt.ylabel('Magnitude')
# plt.title('Frequency Spectrum of Multi-tone Signal')
# plt.grid(True)

# # Plot the frequency spectrum of the impulse train
# plt.subplot(3, 1, 2)
# plt.plot(freqs, np.abs(fft_impulse_train))
# plt.xlabel('Frequency (Hz)')
# plt.ylabel('Magnitude')
# plt.title('Frequency Spectrum of Impulse Train')
# plt.grid(True)

# # Plot the combined spectrum (multi-tone signal * impulse train)
# plt.subplot(3, 1, 3)
# plt.plot(freqs, np.abs(combined_spectrum))
# plt.xlabel('Frequency (Hz)')
# plt.ylabel('Magnitude')
# plt.title('Combined Spectrum (Multi-tone Signal * Impulse Train)')
# plt.grid(True)

# plt.tight_layout()
# plt.show()


