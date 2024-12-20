import math

from Signal import Signal

def get_filters(filter_type, fs, stop_band_attenuation, f1, f2, transition_band):
    delta_f = transition_band / fs
    [N, windowFunction] = get_n_and_window(stop_band_attenuation, delta_f)
    end_pos = int((N - 1) / 2)
    if filter_type == "Low pass":
        f1 = (f1 + (transition_band / 2)) / fs
        filter_dict = get_low_high_pass_filter(windowFunction, end_pos, f1)
        return filter_dict
    elif filter_type == "High pass":
        f1 = (f1 - (transition_band / 2)) / fs
        filter_dict = get_low_high_pass_filter(windowFunction, end_pos, f1, "high")
        return filter_dict
    elif filter_type == "Band Pass":
        f1 = (f1 - (transition_band / 2)) / fs
        f2 = (f2 + (transition_band / 2)) / fs
        filter_dict = get_pass_stop_filter(windowFunction, end_pos, f1, f2)
        return filter_dict
    elif filter_type == "Band Stop":
        f1 = (f1 + (transition_band / 2)) / fs
        f2 = (f2 - (transition_band / 2)) / fs
        filter_dict = get_pass_stop_filter(windowFunction, end_pos, f1, f2, "stop")
        return filter_dict

def get_n_and_window(stop_band_attenuation, delta_f):
    if stop_band_attenuation <= 21:
        N = ceil_n(0.9 / delta_f)
        return [N, lambda n: 1]
    elif stop_band_attenuation <= 44:
        N = ceil_n(3.1 / delta_f)
        return [N, lambda n: 0.5 + 0.5 * math.cos((2 * math.pi * n) / N)]
    elif stop_band_attenuation <= 53:
        N = ceil_n(3.3 / delta_f)
        return [N, lambda n: 0.54 + 0.46 * math.cos((2 * math.pi * n) / N)]
    else:
        N = ceil_n(5.5 / delta_f)
        return [N, lambda n: 0.42 + 0.5 * math.cos((2 * math.pi * n) / (N - 1)) + 0.08 * math.cos((4 * math.pi * n) / (N - 1))]

def ceil_n(N):
    ceil_num = math.ceil(N)
    return ceil_num if ceil_num % 2 != 0 else ceil_num + 1

def get_low_high_pass_filter(window_function, end_pos, fc, filter_type = "low"):
    values = []
    for n in range(0, end_pos + 1):
        w = window_function(n)
        if n == 0:
            if filter_type == "low": values.append(2 * fc)
            else: values.append(1 - (2 * fc))
        else:
            wc = 2 * math.pi * fc * n
            ho = math.sin(wc) / (math.pi * n)
            if filter_type == "high": ho = -1 * ho
            values.append(ho * w)

    symmetric_dict = dict()
    for i, value in enumerate(values):
        symmetric_dict[-i] = value
        if i != 0:
            symmetric_dict[i] = value
    return Signal(symmetric_dict)

def get_pass_stop_filter(window_function, end_pos, f1, f2, filter_type = "pass"):
    values = []
    for n in range(0, end_pos + 1):
        w = window_function(n)
        if n == 0:
            if filter_type == "pass": values.append(2 * (f2 - f1))
            else: values.append(1 - (2 * (f2 - f1)))
        else:
            wc1 = 2 * math.pi * f1 * n
            first_term = math.sin(wc1) / (math.pi * n)
            wc2 = 2 * math.pi * f2 * n
            second_term = math.sin(wc2) / (math.pi * n)

            if filter_type == "pass": ho = second_term - first_term
            else: ho = first_term - second_term

            values.append(ho * w)

    symmetric_dict = dict()
    for i, value in enumerate(values):
        symmetric_dict[-i] = value
        if i != 0:
            symmetric_dict[i] = value
    return Signal(symmetric_dict)
