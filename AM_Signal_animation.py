import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.ticker import FuncFormatter

# Define functions for baseband and carrier signals
def baseband_signal(t, f_m, amplitude=1):
    """Simulates a baseband sinusoid."""
    return amplitude * np.sin(2 * np.pi * f_m * t)

def carrier_signal(t, f_c, amplitude=1):
    """Simulates a carrier sinusoid."""
    return amplitude * np.cos(2 * np.pi * f_c * t) if amplitude!=0 else  np.cos(2 * np.pi * f_c * t)

# Define parameters
f_m = 1000  # Baseband signal frequency
f_c = 10000  # Carrier frequency
baseband_amplitude = 4
sample_rate = 100000  # Sampling rate
t = np.arange(0, 1, 1/sample_rate)  # Time samples

fig, axs = plt.subplots(2, 2, figsize=(10, 8))

def update(frame):
    axs[0,0].cla()
    axs[0,1].cla()
    axs[1,0].cla()
    axs[1,1].cla()
    
    carrier_amplitude = frame 
    
    if carrier_amplitude!=0:
        modulation_index = baseband_amplitude/carrier_amplitude
    else:
        modulation_index = "None"
    
    # Generate baseband and carrier signals
    modulating_signal = baseband_signal(t, f_m, baseband_amplitude)
    carrier = carrier_signal(t, f_c, carrier_amplitude)
    
    # Modulate baseband onto carrier (simple multiplication for this example)
    if carrier_amplitude!=0:
        amplitude_modulation = carrier + (modulation_index/baseband_amplitude)*modulating_signal*carrier
    else:
        amplitude_modulation = modulating_signal*carrier

    fft_modulating_signal = np.fft.fftshift(np.fft.fft(modulating_signal))
    fft_amplitude_modulation = np.fft.fftshift(np.fft.fft(amplitude_modulation))

    fft_freqs = np.fft.fftshift(np.fft.fftfreq(len(t), 1/sample_rate))

    # Plot modulating signal
    axs[0,0].plot(t, modulating_signal, color="blue")
    axs[0,0].set_xlabel('Time (s)')
    axs[0,0].set_ylabel('Modulating Signal')
    axs[0,0].set_title(f"Modulating Signal frequency {f_m} Hz")
    axs[0,0].grid(True)
    axs[0,0].set_xlim(0, 3/f_m)

    # Plot carrier signal
    axs[0,1].plot(t, carrier, color='red')
    axs[0,1].set_xlabel('Time (s)')
    axs[0,1].set_ylabel('Carrier Signal')
    #axs[0,1].set_title(f"Carrier Signal amplitude {carrier_amplitude}")
    axs[0,1].set_title(f"Carrier Signal amplitude {carrier_amplitude:.2f}")
    axs[0,1].grid(True)
    axs[0,1].set_xlim(0, 3/f_m)

    # Plot Modulating signal
    axs[1,0].plot(t, amplitude_modulation, color='green')
    axs[1,0].plot(t, carrier_amplitude+modulating_signal, linestyle="--", color='blue')
    axs[1,0].plot(t, -carrier_amplitude-modulating_signal, linestyle="--", color='blue')
    axs[1,0].set_xlabel('Time (s)')
    axs[1,0].set_ylabel('Amplitude Modulation Signal')
    title = f"AM Modulation (DSB-WC) Index={modulation_index:.2f}" if carrier_amplitude!=0 else "AM Modulation (DSB-SC)"
    axs[1,0].set_title(title)
    axs[1,0].grid(True)
    axs[1,0].set_xlim(0, 3/f_m)

    # Plot frequency domain representation
    axs[1,1].plot(fft_freqs, np.abs(fft_modulating_signal), color='blue', label="Modulating Signal")
    axs[1,1].plot(fft_freqs, np.abs(fft_amplitude_modulation), color="green", label="AM Signal")
    axs[1,1].set_xlabel('Frequency (KHz)')
    axs[1,1].set_ylabel('Magnitude')
    axs[1,1].legend()
    axs[1,1].set_xlim(-f_c - 2*f_m, f_c + 2*f_m)  # Limit to show both sidebands
    axs[1,1].set_xticks([-f_m-f_c, -f_c, -f_c+f_m, -f_m, 0, f_m, f_c-f_m, f_c, f_c+f_m])  # Setting the positions of the ticks
    formatter = FuncFormatter(lambda x, pos: f'{x/1000:g}')  # Formatting the tick labels to show as 1k, 2k, 3k, etc.
    axs[1,1].xaxis.set_major_formatter(formatter)
    axs[1,1].grid(True)

    plt.tight_layout()

ani = FuncAnimation(fig, update, frames=np.arange(10, -0.5, -0.5), interval=200)

# Export the animation as a video file
#ani.save('am_animation.mp4', writer='ffmpeg')

plt.show()