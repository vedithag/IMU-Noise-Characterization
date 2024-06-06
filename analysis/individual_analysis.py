import pandas as pd
from bagpy import bagreader
import matplotlib.pyplot as plt
import numpy as np

# Read in to csv file
bag = bagreader('/home/veditha/lab3/src/imu_driver/data/individual_data.bag')
imu_data = bag.message_by_topic(topic='/imu')
imu_data_csv = pd.read_csv(imu_data)
imu_df = pd.DataFrame(imu_data_csv, columns=['Time', 'magnetic_field.x', 'magnetic_field.y', 'magnetic_field.z', 'linear_acceleration.x', 'linear_acceleration.y', 'linear_acceleration.z', 'angular_velocity.x', 'angular_velocity.y', 'angular_velocity.z', 'orientation.x', 'orientation.y', 'orientation.z', 'orientation.w']).astype(float)

yaw_values = np.arctan2(2*(imu_df['orientation.y']*imu_df['orientation.z']+imu_df['orientation.w']*imu_df['orientation.x']), imu_df['orientation.w']*imu_df['orientation.w']-imu_df['orientation.x']*imu_df['orientation.x']-imu_df['orientation.y']*imu_df['orientation.y']+imu_df['orientation.z']*imu_df['orientation.z'])
pitch_values = np.arcsin(-2*(imu_df['orientation.x']*imu_df['orientation.z']-imu_df['orientation.w']*imu_df['orientation.y']))
roll_values = np.arctan2(2*(imu_df['orientation.x']*imu_df['orientation.y']+imu_df['orientation.w']*imu_df['orientation.z']), imu_df['orientation.w']*imu_df['orientation.w']+imu_df['orientation.x']*imu_df['orientation.x']-imu_df['orientation.y']*imu_df['orientation.y']-imu_df['orientation.z']*imu_df['orientation.z'])

def plot_data_by_time(y_data, title, ylabel):
    plt.close()
    plt.plot(imu_df['Time'], y_data)
    plt.grid()
    plt.title(title)
    plt.xlabel('Time (s)')
    plt.ylabel(ylabel)
    plt.show()

# Plotting magnetic field data
plot_data_by_time(imu_df['magnetic_field.x'], 'Magnetic Field-X vs Time', 'Magnetic Field-X (tesla)')
plot_data_by_time(imu_df['magnetic_field.y'], 'Magnetic Field-Y vs Time', 'Magnetic Field-Y (tesla)')
plot_data_by_time(imu_df['magnetic_field.z'], 'Magnetic Field-Z vs Time', 'Magnetic Field-Z (tesla)')

# Plotting linear acceleration data
plot_data_by_time(imu_df['linear_acceleration.x'], 'Linear Acceleration-X vs Time', 'Linear Acceleration-X (m/s^2)')
plot_data_by_time(imu_df['linear_acceleration.y'], 'Linear Acceleration-Y vs Time', 'Linear Acceleration-Y (m/s^2)')
plot_data_by_time(imu_df['linear_acceleration.z'], 'Linear Acceleration-Z vs Time', 'Linear Acceleration-Z (m/s^2)')

# Plotting angular velocity data
plot_data_by_time(imu_df['angular_velocity.x'], 'Angular Velocity-X vs Time', 'Angular Velocity-X (rad/s)')
plot_data_by_time(imu_df['angular_velocity.y'], 'Angular Velocity-Y vs Time', 'Angular Velocity-Y (rad/s)')
plot_data_by_time(imu_df['angular_velocity.z'], 'Angular Velocity-Z vs Time', 'Angular Velocity-Z (rad/s)')

# Plotting orientation data
plot_data_by_time(imu_df['orientation.x'], 'Orientation-X vs Time', 'Orientation-X')
plot_data_by_time(imu_df['orientation.y'], 'Orientation-Y vs Time', 'Orientation-Y')
plot_data_by_time(imu_df['orientation.z'], 'Orientation-Z vs Time', 'Orientation-Z')
plot_data_by_time(imu_df['orientation.w'], 'Orientation-W vs Time', 'Orientation-W')

# Plotting roll, pitch, and yaw data
plot_data_by_time(roll_values, 'Roll vs Time', 'Roll (deg)')
plot_data_by_time(pitch_values, 'Pitch vs Time', 'Pitch (deg)')
plot_data_by_time(yaw_values, 'Yaw vs Time', 'Yaw (deg)')

def calculate_mean_and_stddev(data):
    mean_value = np.mean(data)
    std_deviation = np.sqrt(np.sum(np.square(data - mean_value)) / len(data))
    return mean_value, std_deviation

# Calculating mean and standard deviation for various sensor data
mean_stddev_values = np.zeros((16, 2))
mean_stddev_values[3, :] = calculate_mean_and_stddev(imu_df['linear_acceleration.x'])
mean_stddev_values[4, :] = calculate_mean_and_stddev(imu_df['linear_acceleration.y'])
mean_stddev_values[5, :] = calculate_mean_and_stddev(imu_df['linear_acceleration.z'])
mean_stddev_values[6, :] = calculate_mean_and_stddev(imu_df['angular_velocity.x'])
mean_stddev_values[7, :] = calculate_mean_and_stddev(imu_df['angular_velocity.y'])
mean_stddev_values[8, :] = calculate_mean_and_stddev(imu_df['angular_velocity.z'])
mean_stddev_values[0, :] = calculate_mean_and_stddev(imu_df['magnetic_field.x'])
mean_stddev_values[1, :] = calculate_mean_and_stddev(imu_df['magnetic_field.y'])
mean_stddev_values[2, :] = calculate_mean_and_stddev(imu_df['magnetic_field.z'])
mean_stddev_values[9, :] = calculate_mean_and_stddev(imu_df['orientation.x'])
mean_stddev_values[10, :] = calculate_mean_and_stddev(imu_df['orientation.y'])
mean_stddev_values[11, :] = calculate_mean_and_stddev(imu_df['orientation.z'])
mean_stddev_values[12, :] = calculate_mean_and_stddev(imu_df['orientation.w'])
mean_stddev_values[13, :] = calculate_mean_and_stddev(roll_values)
mean_stddev_values[14, :] = calculate_mean_and_stddev(pitch_values)
mean_stddev_values[15, :] = calculate_mean_and_stddev(yaw_values)

print(mean_stddev_values)

