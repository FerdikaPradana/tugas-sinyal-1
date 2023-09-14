import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# Generate noisy signal
t = np.linspace(0, 1, 1000, endpoint=False)
noise = np.random.normal(0, 0.5, t.shape)
signal_clean = np.sin(2 * np.pi * 5 * t)
signal_noisy = signal_clean + noise

# Create a low-pass FIR filter
nyquist_freq = 0.5  # Nyquist frequency (half of the sampling rate)
cutoff_freq = 0.1   # Cutoff frequency (relative to Nyquist frequency)
num_taps = 51       # Number of filter taps (filter length)

# Design the filter kernel
filter_kernel = signal.firwin(num_taps, cutoff_freq, nyq=nyquist_freq)

# Apply the filter to the noisy signal
filtered_signal = signal.lfilter(filter_kernel, 1.0, signal_noisy)

# Plot the original signal, noisy signal, and filtered signal
plt.figure(figsize=(10, 6))
plt.plot(t, signal_clean, label='Original Signal', linewidth=2)
plt.plot(t, signal_noisy, label='Noisy Signal', alpha=0.7)
plt.plot(t, filtered_signal, label='Filtered Signal', linewidth=2)
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)
plt.show()
