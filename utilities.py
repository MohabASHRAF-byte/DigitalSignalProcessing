from Signal import Signal
def ReadSignal(file_path:str=None):
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
        signal_data:dict[int, float] ={} 
        for line in file:
            parts = line.strip().split()
            index = int(parts[0])
            value = float(parts[1])
            signal_data[index] = value
    signal = Signal(data=signal_data,offset=offest)
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
