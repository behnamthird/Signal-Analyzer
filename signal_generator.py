import numpy as np
import pandas as pd


def generate_signal(duration=5, sample_rate=1000, noise_level=0.3):
    """
    Generate a noisy sine wave signal and save it as CSV.

    Parameters:
        duration (int): total duration in seconds
        sample_rate (int): number of samples per second
        noise_level (float): standard deviation of Gaussian noise

    Returns:
        DataFrame with time and signal value
    """
    t = np.linspace(0, duration, duration * sample_rate)
    frequency = 2  # 2 Hz sine wave
    signal = np.sin(2 * np.pi * frequency * t)
    noise = np.random.normal(0, noise_level, size=t.shape)
    noisy_signal = signal + noise

    df = pd.DataFrame({"time": t, "value": noisy_signal})
    df.to_csv("data/signal_data.csv", index=False)
    return df


if __name__ == "__main__":
    generate_signal()
