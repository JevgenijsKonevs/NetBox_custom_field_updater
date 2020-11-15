import requests
import json
import paramiko
import os
import re
import pytest
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
test_server_ip_list = ['192.168.100.1', '192.168.100.1',
                       '192.168.100.1', '192.168.100.1', '192.168.100.1']
sw_version_test_valid_list = ["Version 12.4(6)T3", "Version 12.4(6)T3",
                              "Version 12.4(6)T3", "Version 12.4(6)T3", "Version 12.4(6)T3"]
sw_version_test_invalid_list = ["V 123", "Versija", "Version", "v202", "v105"]
sw_output_test_dict = {44: "Version 12.4(6)T3", 45: "Version 12.4(6)T3",
                       46: "Version 12.4(6)T3", 63: "Version 12.4(6)T3", 64: "Version 12.4(6)T3"}
invalid_server_dict = {"id1": "10.10.10.1"}
username = "evgeny"
password = "cisco"


def test_ping_valid_device():
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
            assert rep != 0
            if rep != 0:
                raise Exception(
                    "Equipment is unreachable! Can not setup the connection :(")
            print("Equipment is reachable! Performing the connection....")
            try:
                # Setup a connection
                ssh = paramiko.SSHClient()
                # Fixing the problem with the known_hosts. Automatically add it
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                # Replace 'username', 'password' with actual values, if needed
                ssh.connect(server_ip, port=22,
                            username=username, password=password, allow_agent=False)
            except paramiko.ssh_exception.NoValidConnectionsError as error:
                print("Failed to connect to host '%s' with error: %s" % (error))
            # Executing the command on the equipment to observer the software version
            stdin, stdout, stderr = ssh.exec_command('show version')
            print("Successfully Connected!")
            # Close ssh session
            ssh.close()
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
        # Update device_dict values with sw_version. Example {1:"Version 1.0",2:"Version 2.0"}
        sw_output_dict = dict(zip(device_dict, sw_version))
        # Returning the new dictionary
        return sw_output_dict


def test_invalid_server_ip():
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
            with pytest.raises(Exception):
                if rep != 0:
                    raise Exception(
                        "Equipment is unreachable! Can not setup the connection :(")
            print("Equipment is reachable! Performing the connection....")
            try:
                # Setup a connection
                ssh = paramiko.SSHClient()
                # Fixing the problem with the known_hosts. Automatically add it
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                # Replace 'username', 'password' with actual values, if needed
                ssh.connect(server_ip, port=22,
                            username=username, password=password, allow_agent=False)
            except paramiko.ssh_exception.NoValidConnectionsError as error:
                print("Failed to connect to host '%s' with error: %s" % (error))
            # Executing the command on the equipment to observer the software version
            stdin, stdout, stderr = ssh.exec_command('show version')
            print("Successfully Connected!")
            # Close ssh session
            ssh.close()
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
        # Update device_dict values with sw_version. Example {1:"Version 1.0",2:"Version 2.0"}
        sw_output_dict = dict(zip(device_dict, sw_version))
        # Returning the new dictionary
        return sw_output_dict


def test_sw_valid_version():
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
            with pytest.raises(Exception):
                if rep != 0:
                    raise Exception(
                        "Equipment is unreachable! Can not setup the connection :(")
            print("Equipment is reachable! Performing the connection....")
            try:
                # Setup a connection
                ssh = paramiko.SSHClient()
                # Fixing the problem with the known_hosts. Automatically add it
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                # Replace 'username', 'password' with actual values, if needed
                ssh.connect(server_ip, port=22,
                            username=username, password=password, allow_agent=False)
            except paramiko.ssh_exception.NoValidConnectionsError as error:
                print("Failed to connect to host '%s' with error: %s" % (error))
            # Executing the command on the equipment to observer the software version
            stdin, stdout, stderr = ssh.exec_command('show version')
            print("Successfully Connected!")
            # Close ssh session
            ssh.close()
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
            assert sw_version_test_valid_list[each_hostname] == sw_version[each_hostname]
        # Update device_dict values with sw_version. Example {1:"Version 1.0",2:"Version 2.0"}
        sw_output_dict = dict(zip(device_dict, sw_version))
        # Returning the new dictionary
        return sw_output_dict


def test_sw_invalid_version():
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
            with pytest.raises(Exception):
                if rep != 0:
                    raise Exception(
                        "Equipment is unreachable! Can not setup the connection :(")
            print("Equipment is reachable! Performing the connection....")
            try:
                # Setup a connection
                ssh = paramiko.SSHClient()
                # Fixing the problem with the known_hosts. Automatically add it
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                # Replace 'username', 'password' with actual values, if needed
                ssh.connect(server_ip, port=22,
                            username=username, password=password, allow_agent=False)
            except paramiko.ssh_exception.NoValidConnectionsError as error:
                print("Failed to connect to host '%s' with error: %s" % (error))
            # Executing the command on the equipment to observer the software version
            stdin, stdout, stderr = ssh.exec_command('show version')
            print("Successfully Connected!")
            # Close ssh session
            ssh.close()
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
            assert sw_version_test_invalid_list[each_hostname] != sw_version[each_hostname]
        # Update device_dict values with sw_version. Example {1:"Version 1.0",2:"Version 2.0"}
        sw_output_dict = dict(zip(device_dict, sw_version))
        # Returning the new dictionary
        return sw_output_dict


def test_sw_output_dict():
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
            try:
                # Setup a connection
                ssh = paramiko.SSHClient()
                # Fixing the problem with the known_hosts. Automatically add it
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                # Replace 'username', 'password' with actual values, if needed
                ssh.connect(server_ip, port=22,
                            username=username, password=password, allow_agent=False)
            except paramiko.ssh_exception.NoValidConnectionsError as error:
                print("Failed to connect to host '%s' with error: %s" % (error))
            # Executing the command on the equipment to observer the software version
            stdin, stdout, stderr = ssh.exec_command('show version')
            print("Successfully Connected!")
            # Close ssh session
            ssh.close()
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
        # Update device_dict values with sw_version. Example {1:"Version 1.0",2:"Version 2.0"}
        sw_output_dict = dict(zip(device_dict, sw_version))
        assert sw_output_test_dict == sw_output_dict
        # Returning the new dictionary
        return sw_output_dict
