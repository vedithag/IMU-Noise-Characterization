# IMU-Noise-Characterization

This project involves the characterization of IMU (Inertial Measurement Unit) noise using Allan variance. The Allan variance is a statistical tool used to analyze and quantify the noise characteristics of accelerometer and gyroscope measurements. This repository contains the code, data, and analysis results from the study.

## Introduction
IMU noise characterization with Allan variance helps in understanding the noise characteristics such as random walk noise, bias instability, rate random walk, and white noise in IMU data. This understanding is crucial for designing precise motion sensing systems, enabling accurate measurements, and improving the overall performance of inertial sensors.

By collecting IMU measurements over a period and calculating the Allan variance, we can identify different types of noise present in the data. The Allan variance curve helps determine the optimal integration time for the IMU, balancing noise reduction and bias error increase.

## Analysis Plots
### Short Interval Analysis (10-15 minutes)
Pitch vs Time
Yaw vs Time
Roll vs Time
Magnetic Field vs Time (X, Y, Z)
Linear Acceleration vs Time (X, Y, Z)
Angular Velocity vs Time (X, Y, Z)
Mean and Standard Deviation

### Long Interval Analysis (5 hours)
Accelerometer Allan Deviation (X, Y, Z)
Gyro Allan Deviation (X, Y, Z)

### Error Analysis
Errors in the data can arise from various sources including setup and data collection errors, sensor noise, calibration errors, magnetic interference, and mounting and installation errors. Key observations include:

### Gaussian distribution of errors indicated by histogram plots.
Negative means in linear acceleration suggest sensor biases or external forces.
Angular velocity and magnetic field means indicate potential errors in orientation and sensor biases.

## Skills and Knowledge Demonstrated

- **Sensor Calibration**: Proficiency in hard and soft iron calibration techniques for magnetometers, understanding of how to eliminate magnetic distortions to ensure precise heading data.
- **Signal Processing**: Competence with low-pass and high-pass filtering for IMU data to manage noise and drift, enhancing data quality for subsequent calculations.
- **Data Fusion**: Knowledge of complementary filtering and sensor fusion with GPS, ensuring robust positional accuracy and orientation estimates over extended periods.
- **Dead Reckoning**: Expertise in using IMU data to estimate displacement and velocity via integration, along with techniques to minimize drift.
- **Error Correction and Bias Handling**: Applied methods to identify and remove stationary data biases and integrate GPS data to correct for accumulated IMU errors.
- **Technical Documentation and Analysis**: Produced detailed documentation, analyzing IMU and magnetometer data, presenting sensor fusion results, and using plots to visually represent calibration improvements and fusion accuracy.


## Conclusion
Both time series and histogram charts demonstrate that the errors have a Gaussian distribution. The Allan Deviation plot helps identify and quantify noise parameters, enabling the detection and simulation of noise measurements in IMU devices.
