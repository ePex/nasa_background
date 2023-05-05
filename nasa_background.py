import requests
import subprocess
import os
import logging
import platform

# Set up logging
logging.basicConfig(filename='nasa_background.log', level=logging.DEBUG)

# Make a GET request to the NASA APOD API
response = requests.get('https://api.nasa.gov/planetary/apod', params={'api_key': 'DEMO_KEY'})

# Parse the response JSON and get the URL of the image of the day
data = response.json()
image_url = data['url']

# Download the image data and save it to a file
response = requests.get(image_url)
with open('nasa_image.jpg', 'wb') as f:
    f.write(response.content)

# Set desktop background
try:
    if platform.system() == 'Darwin':  # macOS
        file_location = os.path.abspath("nasa_image.jpg")
        osascript = f'tell application "System Events" to set picture of every desktop to "{file_location}"'
        os.system(f"osascript -e '{osascript}'")
    elif platform.system() == 'Windows':  # Windows
        import ctypes
        SPI_SETDESKWALLPAPER = 20
        file_location = os.path.abspath("nasa_image.jpg")
        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, file_location, 0)
    else:
        logging.error('Unsupported operating system: %s' % platform.system())

    logging.info('Desktop background set successfully.')
except subprocess.CalledProcessError as e:
    logging.error('Error setting desktop background: %s' % e)
