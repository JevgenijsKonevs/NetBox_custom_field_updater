import requests
import json
import re
import pytest
# API url
api_url = 'https://netboxdemo.com/api/'
# Device url
device_url = api_url + "dcim/devices/"
# Status = Active, Tenant = NOC url
param_url = api_url+"dcim/devices/?tenant=noc&status=active"
# Authorization header
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Token 72830d67beff4ae178b94d8f781842408df8069d'
}
device_name_list = ["device1", "test_device", "CISCO c7200", "PALO ALTO"]
device_role_name_list = ["Core Switch", "Access Switch", "Firewall", "Server"]
device_site_name_list = ["A-main_rack", "B-main_rack", "DS9", "NCC-1701-D"]
device_rack_name_list = ["Rack1", "Rack2", "CORE_RACK", "Rack3"]
device_wrong_ipv4_value_list = ["192.168.100.1/",
                                "10.1.20..1", "172.39.4."]


def test_headers():
    def create_new_device():
        data = {
            "name": device_name_list[2],
            "device_type": 4,
            "device_role": {"name": device_role_name_list[2]},
            "tenant": {"name": "NOC"},
            "platform": 2,
            "serial": "",
            "asset_tag": None,
            "site": {"name": device_site_name_list[2]},
            "rack": {"name": device_rack_name_list[2]},
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
        assert response.headers["Content-Type"] == "application/json"
        if response.status_code != 201:
            raise Exception(
                "New device creation went wrong! Try again :(\n"+response.text)
        print("Device was sucessfully created!")
    create_new_device()


def test_fault_new_device_one():
    def create_new_device():

        data = {
            "name": device_name_list[0],
            "device_type": 4,
            "device_role": {"name": device_role_name_list[0]},
            "tenant": {"name": "NOC"},
            "platform": 2,
            "serial": "",
            "asset_tag": None,
            "site": {"name": device_site_name_list[0]},
            "rack": {"name": device_rack_name_list[0]},
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
        with pytest.raises(Exception):
            if response.status_code != 201:
                raise Exception(
                    "New device creation went wrong! Try again :(\n"+response.text)
        print("Device was sucessfully created!")
    create_new_device()


def test_fault_new_device_two():
    def create_new_device():

        data = {
            "name": device_name_list[3],
            "device_type": 4,
            "device_role": {"name": device_role_name_list[2]},
            "tenant": {"name": "NOC"},
            "platform": 2,
            "serial": "",
            "asset_tag": None,
            "site": {"name": device_site_name_list[1]},
            "rack": {"name": device_rack_name_list[2]},
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
        with pytest.raises(Exception):
            if response.status_code != 201:
                raise Exception(
                    "New device creation went wrong! Try again :(\n"+response.text)
        print("Device was sucessfully created!")
    create_new_device()


def test_new_device():
    def create_new_device():

        data = {
            "name": device_name_list[0],
            "device_type": 4,
            "device_role": {"name": device_role_name_list[0]},
            "tenant": {"name": "NOC"},
            "platform": 2,
            "serial": "",
            "asset_tag": None,
            "site": {"name": device_site_name_list[2]},
            "rack": {"name": device_rack_name_list[2]},
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
        assert response.status_code == 201
        if response.status_code != 201:
            raise Exception(
                "New device creation went wrong! Try again :(\n"+response.text)
        print("Device was sucessfully created!")
    create_new_device()


def test_new_device_wrong_ip():
    def create_new_device():

        data = {
            "name": device_name_list[0],
            "device_type": 4,
            "device_role": {"name": device_role_name_list[0]},
            "tenant": {"name": "NOC"},
            "platform": 2,
            "serial": "",
            "asset_tag": None,
            "site": {"name": device_site_name_list[2]},
            "rack": {"name": device_rack_name_list[2]},
            "position": None,
            "face": "front",
            "parent_device": {
                "name": ""
            },
            "status": "active",
            "primary_ip4": device_wrong_ipv4_value_list[2],
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
        with pytest.raises(Exception):
            if response.status_code != 201:
                raise Exception(
                    "New device creation went wrong! Try again :(\n"+response.text)
        print("Device was sucessfully created!")
    create_new_device()


def test_new_device_wrong_ip():
    def create_new_device():

        data = {
            "name": device_name_list[0],
            "device_type": 4,
            "device_role": {"name": device_role_name_list[0]},
            "tenant": {"name": "NOC"},
            "platform": 2,
            "serial": "",
            "asset_tag": None,
            "site": {"name": device_site_name_list[2]},
            "rack": {"name": device_rack_name_list[2]},
            "position": None,
            "face": "front",
            "parent_device": {
                "name": ""
            },
            "status": "active",
            "primary_ip4": device_wrong_ipv4_value_list[0],
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
        with pytest.raises(Exception):
            if response.status_code != 201:
                raise Exception(
                    "New device creation went wrong! Try again :(\n"+response.text)
        print("Device was sucessfully created!")
    create_new_device()


def test_new_device_wrong_ip2():
    def create_new_device():

        data = {
            "name": device_name_list[1],
            "device_type": 4,
            "device_role": {"name": device_role_name_list[1]},
            "tenant": {"name": "NOC"},
            "platform": 2,
            "serial": "",
            "asset_tag": None,
            "site": {"name": device_site_name_list[2]},
            "rack": {"name": device_rack_name_list[2]},
            "position": None,
            "face": "front",
            "parent_device": {
                "name": ""
            },
            "status": "active",
            "primary_ip4": device_wrong_ipv4_value_list[1],
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
        with pytest.raises(Exception):
            if response.status_code != 201:
                raise Exception(
                    "New device creation went wrong! Try again :(\n"+response.text)
        print("Device was sucessfully created!")
    create_new_device()


def test_new_device_wrong_ip3():
    def create_new_device():

        data = {
            "name": device_name_list[2],
            "device_type": 4,
            "device_role": {"name": device_role_name_list[2]},
            "tenant": {"name": "NOC"},
            "platform": 2,
            "serial": "",
            "asset_tag": None,
            "site": {"name": device_site_name_list[2]},
            "rack": {"name": device_rack_name_list[2]},
            "position": None,
            "face": "front",
            "parent_device": {
                "name": ""
            },
            "status": "active",
            "primary_ip4": device_wrong_ipv4_value_list[2],
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
        with pytest.raises(Exception):
            if response.status_code != 201:
                raise Exception(
                    "New device creation went wrong! Try again :(\n"+response.text)

        print("Device was sucessfully created!")

    create_new_device()
