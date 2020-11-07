import requests
import json
# Access token
token = '72830d67beff4ae178b94d8f781842408df8069d'
# API url with parameters tenant = noc and status = active
url = 'https://netboxdemo.com/api/dcim/devices/?tenant=noc&status=active'
# authorization
head = {'Authorization': 'token {}'.format(token)}
# get request
response = requests.get(url, headers=head)
# print response status (if 200 then request is sucessful)
print(response)
# print data in json format
print(response.json())
