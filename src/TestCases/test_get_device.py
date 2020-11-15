import requests
import json
import re

# API url
api_url = 'https://netboxdemo.com/api/'
# Status = Active, Tenant = NOC url
param_url = api_url+"dcim/devices/?tenant=noc&status=active"
# Authorization header
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Token 72830d67beff4ae178b94d8f781842408df8069d'
}
# devices that were created and are currently active on netboxdemo
created_devices_names = ["test_device_50", "test_device_51", "test_device_52"]
created_devices_id = [44, 45, 46]
created_devices_ipv4 = ["192.168.10.1/24",
                        "192.168.10.2/24", "192.168.10.3/24"]
created_devices_dict = {44: "192.168.10.1",
                        45: "192.168.10.2", 46: "192.168.10.3"}


def test_status():
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
        assert response.status_code == 200
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
    get_device_info()


def test_headers():
    def get_device_info():
        # Creating empty arrays for ID and IP values from API
        id_number = []
        ip_number = []
        # Send GET request to API
        response = requests.get(param_url, headers=headers)
        assert headers['Content-Type'] == "application/json"
        if response.status_code != 200:
            raise Exception("Device info request went wrong! Try again :(")
        json_data = response.json()
        device_count = json_data['count']
        results = json_data['results']
        assert response.status_code == 200
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
    get_device_info()


def test_url():
    def get_device_info():
        # Creating empty arrays for ID and IP values from API
        id_number = []
        ip_number = []
        # Send GET request to API
        response = requests.get(param_url, headers=headers)
        assert param_url == 'https://netboxdemo.com/api/dcim/devices/?tenant=noc&status=active'
        if response.status_code != 200:
            raise Exception("Device info request went wrong! Try again :(")
        json_data = response.json()
        device_count = json_data['count']
        results = json_data['results']
        assert response.status_code == 200
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
    get_device_info()


def test_devices_ids():
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
        assert response.status_code == 200
        for each_device in range(0, device_count):
            # getting device data from response
            device_id = results[each_device]['id']
            assert device_id == created_devices_id[each_device]
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
    get_device_info()


def test_devices_names():
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
        assert response.status_code == 200
        for each_device in range(0, device_count):
            # getting device data from response
            device_id = results[each_device]['id']
            device_name = results[each_device]['name']
            assert device_name == created_devices_names[each_device]
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
    get_device_info()


def test_devices_ip():
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
        assert response.status_code == 200
        for each_device in range(0, device_count):
            # getting device data from response
            device_id = results[each_device]['id']
            device_name = results[each_device]['name']
            device_display_name = results[each_device]['device_type']['display_name']
            device_status = results[each_device]['status']['value']
            device_rack_name = results[each_device]['rack']['name']
            device_primary_ip = results[each_device]['primary_ip']['address']
            device_ipv4 = results[each_device]['primary_ip4']['address']
            assert device_ipv4 == created_devices_ipv4[each_device]
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
    get_device_info()


def test_devices_dict():
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
        assert response.status_code == 200
        for each_device in range(0, device_count):
            # getting device data from response
            device_id = results[each_device]['id']
            device_name = results[each_device]['name']
            device_display_name = results[each_device]['device_type']['display_name']
            device_status = results[each_device]['status']['value']
            device_rack_name = results[each_device]['rack']['name']
            device_primary_ip = results[each_device]['primary_ip']['address']
            device_ipv4 = results[each_device]['primary_ip4']['address']
            assert device_ipv4 == created_devices_ipv4[each_device]
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
        assert device_dict == created_devices_dict
        return device_dict
    get_device_info()
