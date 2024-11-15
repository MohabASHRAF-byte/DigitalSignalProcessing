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