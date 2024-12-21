"""
This class provides the functionality to apply a filter to a signal
in the frequency domain by performing a convolution.
"""
import numpy as np
from Signal import Signal


class Filter:
    @staticmethod
    def apply(s1: Signal, s2: Signal) -> Signal:
        """
        Applies a filter in the frequency domain by performing a convolution
        between two signals.
        """
        combined_length = len(s1.data) + len(s2.data) - 1
        st = min(min(s2.data.keys()), min(s1.data.keys()))
        ed = st + combined_length

        val1 = s1.get_signal_values()
        val2 = s2.get_signal_values()

        x_padded = np.pad(val1, (0, combined_length - len(val1)))
        z_padded = np.pad(val2, (0, combined_length - len(val2)))

        data1 = {i: x_padded[i] for i in range(st, ed)}
        data2 = {i: z_padded[i] for i in range(st, ed)}

        s1_padded_signal = Signal(data1)
        s2_padded_signal = Signal(data2)

        self_amp, self_phase = s1_padded_signal.dft(combined_length)
        s2_amp, s2_phase = s2_padded_signal.dft(combined_length)

        convolved_amplitudes = \
            [self_amp[i] * s2_amp[i] for i in range(combined_length)]
        convolved_phases = \
            [(self_phase[i] + s2_phase[i]) for i in range(combined_length)]

        s1.dft_amplitudes = convolved_amplitudes
        s1.dft_phases = convolved_phases

        reconstructed_signal = s1.idft(combined_length)

        data = {i: reconstructed_signal[i - st] for i in range(st, ed)}

        return Signal(data)
