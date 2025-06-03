import matplotlib.pyplot as plt


def plot_signal(df, filtered, peaks):
    """
    Plot original and filtered signals along with detected peaks.

    Parameters:
        df (DataFrame): original signal with 'time' and 'value'
        filtered (array): filtered signal values
        peaks (array): indices of detected peaks
    """
    time = df["time"]
    original = df["value"]

    plt.figure(figsize=(12, 6))

    # Original signal
    plt.plot(time, original, label="Original Signal", alpha=0.5)

    # Filtered signal
    plt.plot(time, filtered, label="Filtered Signal", linewidth=2)

    # Peaks
    plt.plot(time[peaks], filtered[peaks], "ro", label="Peaks")

    plt.title("Signal Analysis")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
