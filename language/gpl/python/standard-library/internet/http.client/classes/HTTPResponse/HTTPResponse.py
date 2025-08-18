# %%
from http.client import HTTPSConnection, HTTPResponse
import json

# Request Connection
conn = HTTPSConnection("httpbin.org")

# Configures the Request
conn.request("GET", "/get")

# Send request!
response: HTTPResponse = conn.getresponse()

# Read response
response_data: bytes = response.read()

# Parse response
json.loads(response_data)
