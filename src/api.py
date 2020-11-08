import requests
import json
# API url with parameters tenant = noc and status = active
api_url = 'https://netboxdemo.com/api/dcim/devices/?tenant=noc&status=active'
# Access token + content type
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Token 72830d67beff4ae178b94d8f781842408df8069d'
}
# Send GET request to API
response = requests.get(api_url, headers=headers)


def get_device_info():
    json_data = response.json()
    results = json_data['results']

    for device in results:

        # getting device data from response
        device_name = device['name']
        device_display_name = device['device_type']['display_name']
        device_status = device['status']['value']
        device_rack_name = device['rack']['name']
        device_primary_ip = device['primary_ip']['address']
        device_ipv4 = device['primary_ip4']['address']
        device_ipv6 = device['primary_ip6']
        tenant = device['tenant']['name']

        # printing the device data
        print("Device name: " + str(device_name))
        print("Device display name: " + str(device_display_name))
        print("Device status: " + str(device_status))
        print("Tenant: " + str(tenant))
        print("Rack: " + str(device_rack_name))
        print("Device primary IP: "+str(device_primary_ip))
        print("Device IPv4: " + str(device_ipv4))
        print("Device IPv4: " + str(device_ipv6))


get_device_info()
