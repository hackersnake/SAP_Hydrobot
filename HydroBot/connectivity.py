import time
import requests
import json
import picamera
from io import BytesIO

# Replace with your server IP and port
SERVER_URL = 'http://your-server-ip:5000/update_data'
ROBOT_IP = 'your-robot-ip'

# Function to simulate GPS location data
def get_gps_location():
    # Replace with actual GPS data retrieval logic
    return {
        'latitude': 12.9716,
        'longitude': 77.5946
    }

# Function to simulate accelerometer data
def get_accelerometer_data():
    # Replace with actual accelerometer data retrieval logic
    return {
        'x': 0.0,
        'y': 0.0,
        'z': 0.0
    }

# Function to simulate battery health data
def get_battery_health():
    # Replace with actual battery health data retrieval logic
    return 100  # 100% battery health

# Function to simulate safety status data
def get_safety_status():
    # Replace with actual safety status data retrieval logic
    return 'Safe'

# Function to capture image from the camera
def capture_image():
    with picamera.PiCamera() as camera:
        stream = BytesIO()
        camera.capture(stream, format='jpeg')
        stream.seek(0)
        return stream.read()

# Main loop to send data to the server
while True:
    data = {
        'robot_ip': ROBOT_IP,
        'location': get_gps_location(),
        'accelerometer': get_accelerometer_data(),
        'battery': get_battery_health(),
        'safety': get_safety_status(),
        'time': time.strftime('%Y-%m-%d %H:%M:%S')
    }
    
    # Send sensor data
    try:
        response = requests.post(SERVER_URL, json=data)
        print('Data sent:', response.status_code)
    except requests.exceptions.RequestException as e:
        print('Error sending data:', e)

    # Send camera feed
    try:
        image = capture_image()
        response = requests.post(SERVER_URL + '/camera', files={'image': image})
        print('Camera feed sent:', response.status_code)
    except requests.exceptions.RequestException as e:
        print('Error sending camera feed:', e)

    # Wait for 3 seconds before sending the next set of data
    time.sleep(3)
