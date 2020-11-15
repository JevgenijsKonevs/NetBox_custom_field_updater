import requests
import json
import paramiko
import os
import re
# API url
api_url = 'https://netboxdemo.com/api/'
device_url = 'https://netboxdemo.com/api/dcim/devices/'
# Status = Active, Tenant = NOC url
param_url = api_url+"dcim/devices/?tenant=noc&status=active"
# Authorization header
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Token 72830d67beff4ae178b94d8f781842408df8069d'
}
test_server_ip_list = []
sw_version_test_list = []
sw_output_test_dict = []


def test_ping():
    def get_device_info():
        # Creating empty arrays for ID and IP values from API
        id_number = []
        ip_number = []
        # Send GET request to API
        response = requests.get(param_url, headers=headers)
        if response.status_code != 200:
            raise Exception("Device info request went wrong! Try again :(")
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

        # Creating the dictionary with key = ID and value = IP
        device_dict = dict(zip(id_number, ip_number))

        return device_dict

    def get_device_sw_version():
        sw_version = []
        output = ""
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
            if rep != 0:
                raise Exception(
                    "Equipment is unreachable! Can not setup the connection :(")
            print("Equipment is reachable! Performing the connection....")
            # Setup a connection
            ssh = paramiko.SSHClient()
            # Fixing the problem with the known_hosts. Automatically add it
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            # Replace 'username', 'password' with actual values, if needed
            ssh.connect(server_ip, port=22,
                        username='demo', password='password', allow_agent=False)
            # Executing the command on the equipment to observer the software version
            stdin, stdout, stderr = ssh.exec_command('show version')
            print("Successfully Connected!")
            # Get and store the output
            for line in stdout:
                output = output+line
            # Get the first string of the output
            first_output_string = output.split('\n')[0]
            # Locate and store the string value with version
            software_version_value = ''.join(re.findall(
                '\,\s*(Version.*)\,', first_output_string))
            # Append the string value to sw_version list
            sw_version.append(software_version_value)
        # Update device_dict values with sw_version. Example {"id1":"Version 1.0","id2":"Version 2.0"}
        sw_output_dict = dict(zip(device_dict, sw_version))
        # Returning the new dictionary
        return sw_output_dict
