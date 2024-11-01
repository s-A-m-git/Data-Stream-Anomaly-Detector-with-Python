import random
import time

class DataStreamAnomalyDetector:
    """
    A class to detect anomalies in a simulated data stream based on mean and standard deviation.
    """
    
    def __init__(self, threshold=2.0):
        """
        Initialize the anomaly detector with a specified threshold.

        :param threshold: The number of standard deviations to consider for anomaly detection.
        """
        self.data_points = []
        self.mean = 0.0
        self.std_dev = 0.0
        self.threshold = threshold
    
    def update_statistics(self, new_value):
        """
        Update the mean and standard deviation with the new value.

        :param new_value: The new data point to add to the statistics.
        """
        # Ensure the new_value is a valid number
        if not isinstance(new_value, (int, float)):
            print("Error: Data point is not a valid number.")
            return

        self.data_points.append(new_value)
        n = len(self.data_points)

        # Calculate mean and standard deviation
        if n == 1:
            self.mean = new_value
            self.std_dev = 0.0
        else:
            old_mean = self.mean
            self.mean += (new_value - old_mean) / n
            self.std_dev = ((n - 2) * self.std_dev**2 + (new_value - old_mean) * (new_value - self.mean)) / (n - 1)
            self.std_dev = self.std_dev**0.5  # Compute standard deviation

    def detect_anomaly(self, value):
        """
        Detect anomalies based on the statistical threshold.

        :param value: The new data point to check for anomalies.
        :return: True if an anomaly is detected, otherwise False.
        """
        if len(self.data_points) < 2:  # Not enough data to make a decision
            return False

        upper_bound = self.mean + self.threshold * self.std_dev
        lower_bound = self.mean - self.threshold * self.std_dev
        return value > upper_bound or value < lower_bound

    def simulate_data_stream(self):
        """
        Simulate a data stream with seasonal patterns and noise.
        """
        # Print table headers
        print(f"{'Status':<17} | {'Value':<5} | {'Mean':<5} | {'Standard Deviation':<18}")
        print("-" * 55)  # Print a separator line

        while True:
            # Simulate seasonal data pattern
            season_value = 50 + 10 * random.choice([-1, 0, 1])  # Random seasonal variation
            noise = random.gauss(0, 5)  # Random noise
            new_value = season_value + noise
            
            # Update statistics and detect anomalies
            self.update_statistics(new_value)
            is_anomaly = self.detect_anomaly(new_value)

            # Prepare output format
            status = "Anomaly detected!" if is_anomaly else "Normal"
            print(f"{status:<17} | {new_value:<.2f} | {self.mean:<.2f} | {self.std_dev:<18.2f} |")
            
            time.sleep(0.1)  # Simulate a delay in data streaming

if __name__ == "__main__":
    detector = DataStreamAnomalyDetector(threshold=2.0)
    detector.simulate_data_stream()