import numpy as np
import matplotlib.pyplot as plt

# Define a pure sine wave with specific frequency
def sine_wave(t, f):
  return np.sin(2 * np.pi * f * t)

# Sample rate and time duration
sample_rate = 1000  # Hz
duration = 1  # seconds
t = np.linspace(0, duration, int(sample_rate * duration))

# Define a specific frequency
f0 = 200  # Hz

# Generate the sine wave
signal = sine_wave(t, f0)

# Define windows (replace with desired functions)
def hann_window(size):
  return np.hanning(size)

def hamming_window(size):
  return np.hamming(size)

def blackman_window(size):
  return np.blackman(size)

# Window functions to compare
windows = [hann_window, hamming_window, blackman_window]
non_windowed_fft = np.abs(np.fft.fft(signal))

# Plot results for each window
fig, axes = plt.subplots(len(windows), 1, figsize=(10, 6))

for i, window_func in enumerate(windows):
  # Apply window and calculate FFT
  window = window_func(len(signal))
  windowed_signal = signal * window
  # Take the Fast Fourier Transform (FFT)
  windowed_fft = np.fft.fft(windowed_signal)
  # Frequency bins (half the size due to real signal)
  freqs = np.linspace(0, sample_rate / 2, len(windowed_fft) // 2)
  windowed_fft_abs = np.abs(windowed_fft)[:len(freqs)]  # Absolute values for magnitude
  # Plot for comparison without windowing (increased leakage)
  axes[i].plot(freqs, non_windowed_fft[:len(freqs)], linestyle="--", linewidth="1", label='Without Window')
  # Plot for current window
  axes[i].plot(freqs, windowed_fft_abs, label="With windowing")
  axes[i].set_title(f"FFT (Window: {window_func.__name__})")
  axes[i].set_xlabel('Frequency (Hz)')
  axes[i].set_ylabel('Magnitude')
  axes[i].grid(True)
  axes[i].legend()

# Fine-tune layout
plt.tight_layout()
plt.show()
