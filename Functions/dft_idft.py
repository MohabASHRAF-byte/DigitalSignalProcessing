from math import sin, cos, pi, sqrt, atan2


class DFT:
    @staticmethod
    def compute_dft(signal, fs: int):
        _, input_signal = zip(*signal.data.items())
        N = len(input_signal)
        amplitudes, phases = [], []

        for k in range(fs):
            real, imag = 0, 0
            for j in range(N):
                termVal = 2 * pi * k * j / N
                real += input_signal[j] * cos(termVal)
                imag += -input_signal[j] * sin(termVal)

            amplitude = sqrt(real ** 2 + imag ** 2)
            phase = atan2(imag, real)
            amplitudes.append(amplitude)
            phases.append(phase)

        signal.dft_amplitudes = amplitudes
        signal.dft_phases = phases
        return amplitudes, phases

    @staticmethod
    def compute_idft(signal, fs):
        N = min(fs, len(signal.dft_amplitudes))
        reconstructed_signal = []

        for k in range(N):
            real = 0
            for n in range(N):
                amplitude, phase = signal.dft_amplitudes[n], signal.dft_phases[n]
                term_val = 2 * pi * k * n / N
                real += amplitude * cos(term_val + phase)
            reconstructed_signal.append(real / N)

        signal.data.clear()
        for i in range(len(reconstructed_signal)):
            signal.data[i] = reconstructed_signal[i]
        return reconstructed_signal
