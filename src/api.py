import requests
import json
import paramiko
import os
import re

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
    sw_version = []
    # Accessing the variable from get_device_info
    device_dict = get_device_info()
    # Getting the list of IP addresses
    hostname_list = list(device_dict.values())
    # Counting the length of this list
    hostname_count = len(hostname_list)
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
            # Executing the command on the equipment to observer the software version
            stdin, stdout, stderr = ssh.exec_command('show version')
            # Store the output
            output = stdout.readLines()
            print("Successfully Connected!")
            # Get the first string of the output
            first_output_string = output.split('\n')[0]
            # Locate and store the string value with version
            software_version_value = ''.join(re.findall(
                '\,\s*(Version.*)\,', first_output_string))
            # Append the string value to sw_version list
            sw_version.append(software_version_value)
        else:
            print("Equipment is unreachable! Can not setup the connection :(")
    # Update device_dict values with sw_version. Example {"id1":"Version 1.0","id2":"Version 2.0"}
    sw_output_dict = dict(zip(device_dict, sw_version))
    # Returning the new dictionary
    return sw_output_dict


def update_custom_field():
    sw_output_dict = get_device_sw_version()
    id_list = list(sw_output_dict.keys())
    version_list = list(sw_output_dict.values())
    payload = {
        "custom_fields": {}
    }
    for each_id in range(0, len(id_list)):
        new_device_url = device_url + str(id_list[each_id])+'/'
        for each_version in range(0, len(version_list)):
            payload = {
                "custom_fields": {"sw_version": str(version_list[each_version])}
            }
            data = json.dumps(payload)
            response = requests.patch(
                new_device_url, headers=headers, data=data)
            if response.status_code == 204:
                print("The software version was successfully added to NetBox!")
            else:
                print("Something went wrong! Can not add software version!")
                print(response.text)


# Uncomment if there is no NOC tenant and tenant group created on netboxdemo
# create_tenant()

# Uncomment to create new device. Field "name" and "primary_ip4" should be edited before running
# create_new_device()

# Getting device info, might be errors if no IP address assigned
get_device_info()
# SSH connection to the equipment
get_device_sw_version()
# Updating the custom field on NetBox
# update_custom_field()
