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
# print data from json
results = response.json()
device_count = results["count"]
device_name = results['results'][0]['name']
device_display_name = results['results'][0]['device_type']['display_name']
device_status = results['results'][0]['status']['value']
device_rack_name = results['results'][0]['rack']['name']
device_primary_ip = results['results'][0]['primary_ip']
device_ipv4 = results['results'][0]['primary_ip4']
device_ipv6 = results['results'][0]['primary_ip6']
tenant = results['results'][0]['tenant']['name']
print("Count: " + str(device_count))
print("Device name: " + str(device_name))
print("Device display name: " + str(device_display_name))
print("Device status: " + str(device_status))
print("Tenant: " + str(tenant))
print("Rack: " + str(device_rack_name))
print("Device primary IP: "+str(device_primary_ip))
print("Device IPv4: " + str(device_ipv4))
print("Device IPv4: " + str(device_ipv6))
