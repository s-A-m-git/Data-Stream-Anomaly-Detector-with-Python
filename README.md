# Data-Stream-Anomaly-Detector-with-Python
This project implements a simple anomaly detection system that monitors a simulated data stream. The system calculates the mean and standard deviation of incoming data points to identify values that are significantly different from the norm. 

## Key Components

### 1. **Class Definition**

- **`DataStreamAnomalyDetector`**: This class contains the main logic for detecting anomalies in the data stream.

### 2. **Initialization**

- **`__init__(self, threshold=2.0)`**: 
  - Initializes the anomaly detector with a specified threshold, which determines how far a data point can stray from the mean before it's considered an anomaly.
  - Sets up empty lists for data points and initializes the mean and standard deviation to zero.

### 3. **Updating Statistics**

- **`update_statistics(self, new_value)`**: 
  - Takes in a new data point and updates the running statistics (mean and standard deviation).
  - If it's the first data point, it sets the mean directly. For subsequent points, it calculates a new mean and updates the standard deviation using a formula that incorporates the new value.

### 4. **Anomaly Detection**

- **`detect_anomaly(self, value)`**:
  - Compares the new data point against the calculated mean and standard deviation.
  - Determines if the value is an anomaly by checking if it falls outside a defined range (mean ± threshold * standard deviation). 

### 5. **Simulating Data Stream**

- **`simulate_data_stream(self)`**:
  - Generates random data points with a seasonal pattern and some noise to simulate real-world conditions.
  - Each generated value is processed to update statistics and check for anomalies.
  - Outputs the current status of each data point, whether it is normal or an anomaly, along with its value, the updated mean, and standard deviation in a formatted table.

### 6. **Output Format**

The output is printed in a table format:

```
Status            | Value | Mean  | Standard Deviation
------------------------------------------------------
Normal            | 52.23 | 51.12 |  3.45             |       
Anomaly detected! | 68.45 | 51.12 |  3.45             | 
```

This format clearly shows the status of each data point as it is processed.

## How to Run the Project

To run this project, make sure you have Python installed on your system. Simply execute the script, and it will start simulating the data stream. You can stop it anytime by pressing `Ctrl + C`.

---
