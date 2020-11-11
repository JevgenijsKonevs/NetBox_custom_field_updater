import requests
import json
# API url
api_url = 'https://netboxdemo.com/api/'
# Tenant Group url
tenant_group_url = api_url+"tenancy/tenant-groups/"
# Tenant url
tenant_url = api_url+"tenancy/tenants/"
# Status = Active, Tenant = NOC url
param_url = api_url+"dcim/devices/?tenant=noc&status=active"
# Authorization header
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Token 72830d67beff4ae178b94d8f781842408df8069d'
}


def create_tenant():
    # Create Tenant Group NOC

    data_tenant_group = {
        "name": "NOC",
        "slug": "noc",
        "parent": None,
        "description": "NOC"
    }
    response = requests.post(tenant_group_url, headers=headers,
                             json=data_tenant_group)
    print("Creating new Tenant Group....")
    if response.status_code == 201:
        print("Tenant Group was sucessfully created!")
    else:
        print("Something went wrong! Try again :(")
        print(response.text)

    # Create Tenant NOC
    data_tenant = {
        "name": "NOC",
        "slug": "noc",
        "group": {"name": "NOC"},
        "description": "NOC",
        "comments": "",
        "tags": [
            "noc"
        ],
        "custom_fields": {
        }
    }
 # Send POST request to API
    print("Creating new Tenant....")
    response = requests.post(tenant_url, headers=headers, json=data_tenant)
    if response.status_code == 201:
        print("Tenant was sucessfully created!")
    else:
        print("Something went wrong! Try again :(")
        print(response.text)


def create_new_device():
    data = {
        "name": "test_device_51",
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
        print(response.text)


def get_device_info():
    # Send GET request to API
    response = requests.get(param_url, headers=headers)
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
        print(response.text)


def get_device_sw_version():
    pass


def update_custom_field():
    id = 34
    url_device = 'https://netboxdemo.com/api/dcim/devices/'+str(id)+'/'
    payload = {
        "custom_fields": "sw_version"
    }
    data = json.dumps(payload)

    r = requests.patch(url_device, headers=headers, data=data)
    print(r.status_code)


create_tenant()
create_new_device()
get_device_info()
update_custom_field()
