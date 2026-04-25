# %%

from urllib.parse import urlparse


url = "https://httpbin.org/get"

parsed_url = urlparse(url)

parsed_url.scheme  # https
parsed_url.netloc  # httpbin.org
parsed_url.path  # /get
