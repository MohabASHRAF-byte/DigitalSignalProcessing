from Signal import Signal
from typing import Dict


def ReadSignal(file_path: str = None, reversed: bool = False):
    """
    Open a file and read a single signal from it.
    """

    if not file_path:
        return None

    with open(file_path, 'r') as file:
        # Read the first three numbers
        temp = int(file.readline().strip())
        offest = int(file.readline().strip())
        num_points = int(file.readline().strip())
        # Read the points 
        signal_data: dict[float, float] = {}
        for line in file:
            parts = line.strip().split()
            if reversed:
                index = float(parts[1].replace('f', ''))
                value = float(parts[0].replace('f', ''))
            else:
                index = float(parts[0].replace('f', ''))
                value = float(parts[1].replace('f', ''))

            signal_data[index] = value
    signal = Signal(data=signal_data, offset=offest)
    return signal


def ReadSignalValues(file_path: str = None):
    """
    Open a file and read a single signal from it.
    """

    if not file_path:
        return None

    with open(file_path, 'r') as file:
        # Read the first three numbers
        temp = int(file.readline().strip())
        offest = int(file.readline().strip())
        num_points = int(file.readline().strip())
        # Read the points
        signal_data: dict[float, float] = {}
        i = 0
        for line in file:
            value = line.strip().split()[0]
            signal_data[i] = int(value)
            i += 1

    signal = Signal(data=signal_data, offset=offest)
    return signal


def ReadSignalInFrequencyDomain(file_path: str = None):
    """
    Open a file and read a single signal in frequency domain from it.
    """

    if not file_path:
        return None

    with open(file_path, 'r') as file:
        # Read the first three numbers
        temp = int(file.readline().strip())
        offest = int(file.readline().strip())
        num_points = int(file.readline().strip())
        # Read the points
        signal_data: Dict[float, float] = {}
        Amplitudes = []
        Phases = []
        for line in file:
            parts = line.strip().split()
            Amplitude = float(parts[0].replace('f', ''))
            Phase = float(parts[1].replace('f', ''))
            Amplitudes.append(Amplitude)
            Phases.append(Phase)

    signal = Signal({})
    signal.dft_amplitudes = Amplitudes
    signal.dft_phases = Phases
    return signal


def CompSignals(signal3, Expected, Message):
    Your_indices, Your_samples = signal3.get_signal_indexs(), signal3.get_signal_values()
    expected_indices, expected_samples = Expected.get_signal_indexs(), Expected.get_signal_values()
    if (len(expected_samples) != len(Your_samples)) and (len(expected_indices) != len(Your_indices)):
        return Message + " Test case failed, your signal have different length from the expected one"

    for i in range(len(Your_indices)):
        if (Your_indices[i] != expected_indices[i]):
            return Message + " Test case failed, your signal have different indicies from the expected one"
    for i in range(len(expected_samples)):
        if abs(Your_samples[i] - expected_samples[i]) < 0.01:
            continue
        else:
            return Message + " Test case failed, your signal have different values from the expected one"

    return Message + " Test case passed successfully"


def SignalCompareAmplitude(s1: Signal, s2: Signal):
    SignalInput = s1.dft_amplitudes
    SignalOutput = s2.dft_amplitudes
    if len(SignalInput) != len(SignalOutput):
        return False
    else:
        for i in range(len(SignalInput)):
            if abs(SignalInput[i] - SignalOutput[i]) > 0.001:
                return False
        return True


def SignalComparePhaseShift(s1: Signal, s2: Signal):
    SignalInput = s1.dft_phases
    SignalOutput = s2.dft_phases
    if len(SignalInput) != len(SignalOutput):
        return False
    else:
        for i in range(len(SignalInput)):
            A = round(SignalInput[i])
            B = round(SignalOutput[i])
            if abs(A - B) > 0.0001:
                return False
            elif A != B:
                return False
        return True


def CompSignalsBool(signal3, Expected):
    Your_indices, Your_samples = signal3.get_signal_indexs(), signal3.get_signal_values()
    expected_indices, expected_samples = Expected.get_signal_indexs(), Expected.get_signal_values()
    if (len(expected_samples) != len(Your_samples)) and (len(expected_indices) != len(Your_indices)):
        return False

    for i in range(len(Your_indices)):
        if Your_indices[i] != expected_indices[i]:
            return False
    for i in range(len(expected_samples)):
        if abs(Your_samples[i] - expected_samples[i]) < 0.01:
            continue
        else:
            return False

    return True


def CompSignalsQuantized(signal, path):
    Your_EncodedValues = signal.encoded_values
    Your_QuantizedValues = signal.quantized_values
    file_name = path
    expectedEncodedValues = []
    expectedQuantizedValues = []
    with open(file_name, 'r') as f:
        line = f.readline()
        line = f.readline()
        line = f.readline()
        line = f.readline()
        while line:
            # process line
            L = line.strip()
            if len(L.split(' ')) == 2:
                L = line.split(' ')
                V2 = str(L[0])
                V3 = float(L[1])
                expectedEncodedValues.append(V2)
                expectedQuantizedValues.append(V3)
                line = f.readline()
            else:
                break
    if ((len(Your_EncodedValues) != len(expectedEncodedValues)) or (
            len(Your_QuantizedValues) != len(expectedQuantizedValues))):
        print("QuantizationTest1 Test case failed, your signal have different length from the expected one")
        return False
    for i in range(len(Your_EncodedValues)):
        if (Your_EncodedValues[i] != expectedEncodedValues[i]):
            print(
                "QuantizationTest1 Test case failed, your EncodedValues have different EncodedValues from the expected one")
            return False
    for i in range(len(expectedQuantizedValues)):
        if abs(Your_QuantizedValues[i] - expectedQuantizedValues[i]) < 0.01:
            continue
        else:
            print(
                "QuantizationTest1 Test case failed, your QuantizedValues have different values from the expected one")
            return False
    print("QuantizationTest1 Test case passed successfully")
    return True


def CompSignalsQuantized2(signal, path):
    Your_IntervalIndices = signal.interval_indices
    Your_EncodedValues = signal.encoded_values
    Your_QuantizedValues = signal.quantized_values
    Your_SampledError = signal.errors
    file_name = path
    expectedIntervalIndices = []
    expectedEncodedValues = []
    expectedQuantizedValues = []
    expectedSampledError = []
    with open(file_name, 'r') as f:
        line = f.readline()
        line = f.readline()
        line = f.readline()
        line = f.readline()
        while line:
            # process line
            L = line.strip()
            if len(L.split(' ')) == 4:
                L = line.split(' ')
                V1 = int(L[0])
                V2 = str(L[1])
                V3 = float(L[2])
                V4 = float(L[3])
                expectedIntervalIndices.append(V1)
                expectedEncodedValues.append(V2)
                expectedQuantizedValues.append(V3)
                expectedSampledError.append(V4)
                line = f.readline()
            else:
                break
    if (len(Your_IntervalIndices) != len(expectedIntervalIndices)
            or len(Your_EncodedValues) != len(expectedEncodedValues)
            or len(Your_QuantizedValues) != len(expectedQuantizedValues)
            or len(Your_SampledError) != len(expectedSampledError)):
        print("QuantizationTest2 Test case failed, your signal have different length from the expected one")
        return False

    for i in range(len(Your_IntervalIndices)):
        if (Your_IntervalIndices[i] != expectedIntervalIndices[i]):
            print("QuantizationTest2 Test case failed, your signal have different indicies from the expected one")
            return False
    for i in range(len(Your_EncodedValues)):
        if (Your_EncodedValues[i] != expectedEncodedValues[i]):
            print(
                "QuantizationTest2 Test case failed, your EncodedValues have different EncodedValues from the expected one")
            return False

    for i in range(len(expectedQuantizedValues)):
        if abs(Your_QuantizedValues[i] - expectedQuantizedValues[i]) < 0.01:
            continue
        else:
            print(
                "QuantizationTest2 Test case failed, your QuantizedValues have different values from the expected one")
            return False
    for i in range(len(expectedSampledError)):
        if abs(Your_SampledError[i] - expectedSampledError[i]) < 0.01:
            continue
        else:
            print(
                "QuantizationTest2 Test case failed, your SampledError have different values from the expected one")
            return False
    print("QuantizationTest2 Test case passed successfully")
    return True
