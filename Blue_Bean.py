import bluetooth
import os
import time
import logging
import subprocess
import configparser





# Initialize logging
##logging.basicConfig(filename='/var/log/bluetooth_unlock.log', level=logging.DEBUG)

## put this file in usr/local/bin

TARGET_BLUETOOTH_ADDRESS = '74:42:1X:XX:XX:XX' # the devices bluethooth address you want to use to unlock the computer
PASSWORD = 'Password123'  # Your hardcoded password (use at your own risk)

# Check if the target Bluetooth device is connected
def is_device_connected():
    try:
        nearby_devices = bluetooth.discover_devices(duration=1)
        #logging.debug(f'Nearby devices: {nearby_devices}')
        return TARGET_BLUETOOTH_ADDRESS in nearby_devices
    except bluetooth.BluetoothError as e:
        logging.error(f'Bluetooth error: {e}')
        return False
    except Exception as e:
        logging.error(f'Unexpected error: {e}')
        return False

# Disconnect the Bluetooth device
def disconnect_bluetooth_device():
    try:
        os.system(f'bluetoothctl disconnect {TARGET_BLUETOOTH_ADDRESS}')
        logging.info('Bluetooth device disconnected')
    except Exception as e:
        logging.error(f'Error disconnecting Bluetooth device: {e}')

while True:
    if is_device_connected():
        try:
            logging.info('Device found, performing unlock actions')
            os.system(f'xdotool type {PASSWORD}')  # Type the password
            logging.info('Typing password')
            os.system('xdotool key Return')  # Press Enter
            logging.info('Pressing Enter to login')
            disconnect_bluetooth_device()  # Disconnect the Bluetooth device            
            time.sleep(1)

           

            
            logging.info('reloading services for next login')
        except Exception as e:
            logging.error(f'Error in main loop: {e}')
    else:
        logging.info('Device not found')
    #time.sleep(0.5)