import requests
import json
# API url with parameters tenant = noc and status = active
api_url = 'https://netboxdemo.com/api/dcim/devices/?tenant=noc&status=active'
# API url for all devices
url = 'https://netboxdemo.com/api/dcim/devices/'
# Access token + content type
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Token 72830d67beff4ae178b94d8f781842408df8069d'
}


def create_new_device():
    data = {
        "name": "test_device_6",
        "device_type": 4,
        "device_role": {"name": "Core Switch"},
        "tenant": {"name": "NOC"},
        "platform": 2,
        "serial": "",
        "asset_tag": None,
        "site": {"name": "DS9"},
        "rack": {"name": "CORE_RACK"},
        "position": None,
        "face": "front",
        "parent_device": {
            "name": ""
        },
        "status": "active",
        "primary_ip4": None,
        "primary_ip6": None,
        "cluster": None,
        "virtual_chassis": None,
        "vc_position": None,
        "vc_priority": None,
        "comments": "",
        "local_context_data": "",
        "tags": [
            "string"
        ],
        "custom_fields": {

        }
    }
    # Send POST request to API
    print("Creating new device....")
    response = requests.post(api_url, headers=headers, json=data)
    print(response.status_code)
    if response.status_code == 201:
        print("Device was sucessfully created!")
    else:
        print("Something went wrong! Try again :(")


def get_device_info():
    # Send GET request to API
    response = requests.get(api_url, headers=headers)
    if response.status_code == 200:
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
    else:
        print("Something went wrong! Try again :(")


create_new_device()
get_device_info()
