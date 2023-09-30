import requests

response = requests.get('http://nr.device.util.s3.amazonaws.com')
print(response.text)