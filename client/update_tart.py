import os
import requests
import time

# Make a GET request to a specified URL

tart_name=os.environ['TART_API']

while True:
    try:
        print(f"Starting ping")
        response = requests.get('http://api.elec.ac.nz/tart_monitor')

        # Print the response text
        print(response.text)
    except Exception as e:
        print(e)
    finally:
        print("sleeping")
        time.sleep(60)
