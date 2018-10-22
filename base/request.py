import requests
# Base URL being accessed
url = 'http://httpbin.org/post'

# Dictionary of query parameters (if any)
parms = {
   'name1' : 'value1',
   'name2' : 'value2'
}

# Extra headers
headers = {
    'User-agent' : 'none/ofyourbusiness',
    'Spam' : 'Eggs'
}
resp = requests.post(url, data=parms, headers=headers)

# Decoded text returned by the request
text = resp.text
print(text)

import requests
url = 'http://httpbin.org/post'
files = {'file': ('data.csv', open('data.csv', 'rb'))}
r = requests.post(url, files=files)