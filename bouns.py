import numpy as np
import matplotlib.pyplot as plt
from Signal import Signal

# Generate a sine wave signal
x_vals = np.linspace(0, 2 * np.pi, 100)  # 100 samples over one period
sine_wave_data = {i: np.sin(2 * np.pi * 5 * x) for i, x in enumerate(x_vals)}

sine_signal = Signal(sine_wave_data)

noise_data = {i: np.random.normal(0, 0.5) for i in range(100)}
# Generate noise around 0.5
noise_signal = Signal(noise_data)

# Combine the sine wave with noise
combined_signal = sine_signal + noise_signal

# Compute autocorrelations
sine_autocorr = sine_signal.auto_correlate()
combined_autocorr = combined_signal.auto_correlate()

# Plot results
fig, axs = plt.subplots(4, 1, figsize=(10, 16))

# Plot sine wave
axs[0].plot(sine_signal.get_signal_indexs(), sine_signal.get_signal_values(), label="Sine Wave")
axs[0].set_title("Sine Wave")
axs[0].grid(True)
axs[0].legend()

# Plot noise
axs[1].plot(noise_signal.get_signal_indexs(), noise_signal.get_signal_values(), label="Noise", color='orange')
axs[1].set_title("Additive White Gaussian Noise (AWGN)")
axs[1].grid(True)
axs[1].legend()

# Plot combined signal
axs[2].plot(combined_signal.get_signal_indexs(), combined_signal.get_signal_values(), label="Sine + Noise", color='green')
axs[2].set_title("Noisy Signal")
axs[2].grid(True)
axs[2].legend()

# Plot autocorrelation
axs[3].plot(sine_autocorr.get_signal_indexs(), sine_autocorr.get_signal_values(), label="Sine Autocorrelation", color='blue')
axs[3].plot(combined_autocorr.get_signal_indexs(), combined_autocorr.get_signal_values(), label="Noisy Autocorrelation", color='red')
axs[3].set_title("Autocorrelation")
axs[3].grid(True)
axs[3].legend()

plt.tight_layout()
plt.show()
