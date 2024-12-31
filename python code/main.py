import serial
import requests
url = "http://fi9.bot-hosting.net:20405/"

# Configure the serial connection
bluetooth = serial.Serial('COM4', 9600)  # Replace 'COM3' with your HC-05's COM port
print("Connected to Bluetooth module")

try:
    while True:
        # Read data sent from the Arduino
        if bluetooth.in_waiting > 0:
            received_data = bluetooth.readline().decode('utf-8').strip()
            if received_data.startswith('h') or received_data.startswith('s') or received_data.startswith('t'):
                print(received_data[1:] + " " + received_data[0])
                data = {
                    received_data[0]: received_data[1:]  # Replace with the actual data the server expects
                }

                # Send a POST request
                try:
                    response = requests.post(url, json=data)  # Use json=data if the server expects JSON
                    print("Status Code:", response.status_code)
                    print("Response Data:", response.json())  # Assuming the server responds with JSON
                except requests.exceptions.RequestException as e:
                    print("An error occurred:", e)

except KeyboardInterrupt:
    print("Program stopped")
finally:
    bluetooth.close()
