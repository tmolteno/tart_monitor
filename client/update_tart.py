
import requests

# Make a GET request to a specified URL
response = requests.get('http://api.elec.ac.nz/tart_monitor')

# Print the response text
print(response.text)
