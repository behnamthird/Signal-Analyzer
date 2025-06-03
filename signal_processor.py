import pandas as pd
import numpy as np
from scipy.signal import find_peaks


def moving_average(signal, window_size=50):
    """
    Apply a simple moving average filter to the signal.

    Parameters:
        signal (array): input signal values
        window_size (int): number of samples to average

    Returns:
        array: filtered signal
    """
    return np.convolve(signal, np.ones(window_size)/window_size, mode='same')


def detect_peaks(signal, height=0.5):
    """
    Detect peaks in the signal using scipy.

    Parameters:
        signal (array): filtered signal
        height (float): minimum peak height

    Returns:
        array of peak indices
    """
    peaks, _ = find_peaks(signal, height=height)
    return peaks


def process_signal(csv_path="data/signal_data.csv"):
    """
    Read signal from CSV, apply filter, detect peaks.

    Returns:
        original_df: raw signal
        filtered_signal: filtered values
        peaks: indices of peaks
    """
    df = pd.read_csv(csv_path)
    filtered = moving_average(df["value"])
    peaks = detect_peaks(filtered)
    return df, filtered, peaks


if __name__ == "__main__":
    df, filtered, peaks = process_signal()
    print(f"Detected {len(peaks)} peaks.")
