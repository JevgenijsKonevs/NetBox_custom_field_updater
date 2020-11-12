import requests
import json
import paramiko
import os


# API url
api_url = 'https://netboxdemo.com/api/'
# Tenant Group url
tenant_group_url = api_url+"tenancy/tenant-groups/"
# Tenant url
tenant_url = api_url+"tenancy/tenants/"
# Device url
device_url = 'https://netboxdemo.com/api/dcim/devices/'
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
        print("Tenant Group creation went wrong! Try again :(")
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
        print("Tenant creation went wrong! Try again :(")
        print(response.text)


def create_new_device():

    data = {
        "name": "test_device_55",
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
    response = requests.post(device_url, headers=headers, json=data)
    if response.status_code == 201:
        print("Device was sucessfully created!")
    else:
        print("New device creation went wrong! Try again :(")
        print(response.text)


def get_device_info():
    # Creating empty arrays for ID and IP values from API
    id_number = []
    ip_number = []
    # Send GET request to API
    response = requests.get(param_url, headers=headers)
    if response.status_code == 200:
        json_data = response.json()
        device_count = json_data['count']
        results = json_data['results']

        for each_device in range(0, device_count):
            # getting device data from response
            device_id = results[each_device]['id']
            device_name = results[each_device]['name']
            device_display_name = results[each_device]['device_type']['display_name']
            device_status = results[each_device]['status']['value']
            device_rack_name = results[each_device]['rack']['name']
            device_primary_ip = results[each_device]['primary_ip']['address']
            device_ipv4 = results[each_device]['primary_ip4']['address']
            #device_ipv6 = results[each_device]['primary_ip6']
            tenant = results[each_device]['tenant']['name']

            # Fulfilling the arrays with values
            id_number.append(device_id)
            # Deleting mask from IP address
            device_ipv4_nomask = "/".join(device_ipv4.split("/")[:-1])
            ip_number.append(device_ipv4_nomask)

            # Printing the device data
            print("Device ID: " + str(device_id))
            print("Device name: " + str(device_name))
            print("Device display name: " + str(device_display_name))
            print("Device status: " + str(device_status))
            print("Tenant: " + str(tenant))
            print("Rack: " + str(device_rack_name))
            print("Device primary IP: "+str(device_primary_ip))
            print("Device IPv4: " + str(device_ipv4))
            print("===========================================")
            #print("Device IPv4: " + str(device_ipv6))
    else:
        print("Device info request went wrong! Try again :(")

    # Creating the dictionary with key = ID and value = IP
    device_dict = dict(zip(id_number, ip_number))
    print(device_dict)
    return device_dict


def get_device_sw_version():
    device_dict = get_device_info()
    hostname_list = list(device_dict.values())
    hostname_count = len(hostname_list)

    hostname_test = ["195.144.107.198", "195.144.107.198",
                     "195.144.107.198", "195.144.107.198"]
    hostname_test_count = len(hostname_test)
    # Performing the connection to the devices
    for each_hostname in range(0, hostname_count):
        server_ip = hostname_list[each_hostname].format()
        # Checking if the equipment is reachable (with ping)
        rep = os.system('ping ' + server_ip)
        if rep == 0:
            print("Equipment is reachable! Performing the connection....")
            # Setup a connection
            ssh = paramiko.SSHClient()
            # Fixing the problem with the known_hosts. Automatically add it
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            # Replace 'username', 'password' with actual values, if needed
            ssh.connect(server_ip, port=22,
                        username='demo', password='password')
            # executing the command on the equipment to observer the software version
            # stdin, stdout, stderr = ssh.exec_command('show version')
            # store the output
            # output = stdout.readLines()
            print("Successfully Connected!")
        else:
            print("Equipment is unreachable! Can not setup the connection :(")


get_device_info()
get_device_sw_version()


def update_custom_field():
    response = requests.get(param_url, headers=headers)
    id = 34
    url_device = 'https://netboxdemo.com/api/dcim/devices/'+str(id)+'/'
    payload = {
        "custom_fields": "sw_version"
    }
    data = json.dumps(payload)

    r = requests.patch(url_device, headers=headers, data=data)
    print(r.status_code)


# uncomment if there is no NOC tenant and tenant group created on netboxdemo
# create_tenant()

# uncomment to create new device. Field "name" and "primary_ip4" should be edited before running
# create_new_device()

# getting device info, might be errors if no IP address assigned
get_device_info()

# function is not working on netboxdemo due to lack of admin access
# update_custom_field()
