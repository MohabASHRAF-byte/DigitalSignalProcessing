from math import sin, pi, cos, sqrt, atan2
import math
from Tests.Task5.code import Task5Test
from Signal import Signal

#
# def dft(input_signal, fs: int):
#     """
#     Perform Discrete Fourier Transform on the input signal.
#     :param fs: sampling frequency
#     :return: List of [Amplitude, Phase] for each frequency component
#     """
#     N = len(input_signal)
#     amplitudes, phases = [], []
#
#     for k in range(N):
#         real, imag = 0, 0
#         for j in range(N):
#             termVal = 2 * pi * k * j / N
#             real += input_signal[j] * cos(termVal)
#             imag += -input_signal[j] * sin(termVal)
#
#         amplitude = sqrt(real ** 2 + imag ** 2)  # Amplitude
#         phase = atan2(imag, real)  # Phase
#         amplitudes.append([amplitude, phase])
#
#     print("\nDFT Results (Amplitude and Phase):")
#     for i, (amp, phase) in enumerate(amplitudes):
#         print(f"Frequency {i}: Amplitude = {amp:.10f}, Phase = {phase:.10f} radians")
#
#     return amplitudes  # Return amplitudes and phases as a list of [Amplitude, Phase]
#
#
# def idft(dft_output):
#     """
#     Perform Inverse Discrete Fourier Transform to reconstruct the signal.
#     :param dft_output: List of [Amplitude, Phase] for each frequency component
#     :return: List of reconstructed real values (time domain signal)
#     """
#     N = len(dft_output)  # Length of the signal
#     reconstructed_signal = []
#
#     for k in range(N):  # For each signal point
#         real = 0
#         for n in range(N):
#             amplitude, phase = dft_output[n]  # Extract amplitude and phase
#             term_val = 2 * pi * k * n / N  # IDFT formula
#             real += amplitude * cos(term_val + phase)  # Reconstruct real part
#         reconstructed_signal.append(real / N)  # Normalize the result
#
#     print("\nReconstructed Signal (IDFT):")
#     for i, value in enumerate(reconstructed_signal):
#         print(f"Index {i}: Value = {value:.10f}")
#
#     return reconstructed_signal  # Return reconstructed real values
#

# Input signal for DFT
# input_signal = [1, 3, 5, 7, 9, 11, 13, 15]
#
# # Perform DFT on the input signal
# dft_result = dft(input_signal)
#
# # Perform IDFT on the DFT output to reconstruct the signal
# reconstructed_signal = idft(dft_result)
# s1 = Signal({
#     0: 1,
#     1: 3,
#     2: 5,
#     3: 7,
#     4: 9,
#     5: 11,
#     6: 13,
#     7: 15
# })
# s1.dft2(10)
ob = Task5Test()
ob.RunAllTests()