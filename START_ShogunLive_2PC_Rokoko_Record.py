from vicon_core_api import *
shogun_client = Client('localhost')
print(shogun_client.connected)

import shogun_live_api
capture = shogun_live_api.CaptureServices(shogun_client)

suc, FILENAME = capture.capture_name()
print(suc)
print(FILENAME)
capture.start_capture()

import requests

IP_ADDRESS = '192.168.10.8' # Replace with actual ip address
PORT = '14053' # Replace with actual port
API_KEY = '1234' # Replace with actual api key

request = requests.post(f"http://{IP_ADDRESS}:{PORT}/v1/{API_KEY}/recording/start",
  json = {
    'filename': FILENAME
  }
)
print(request.json())

import requests

IP_ADDRESS = '192.168.10.9' # Replace with actual ip address
PORT = '7777' # Replace with actual port
API_KEY = 'eujd' # Replace with actual api key

request = requests.post(f"http://{IP_ADDRESS}:{PORT}/v1/{API_KEY}/recording/start",
  json = {
    'filename': FILENAME
  }
)
print(request.json())