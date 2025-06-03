from signal_generator import generate_signal
from signal_processor import process_signal
from signal_plotter import plot_signal


def main():
    print("Generating signal...")
    generate_signal()

    print("Processing signal...")
    df, filtered, peaks = process_signal()

    print("Plotting results...")
    plot_signal(df, filtered, peaks)


if __name__ == "__main__":
    main()
