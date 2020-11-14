import requests
import json
import re

# API url
api_url = 'https://netboxdemo.com/api/'
# Tenant Group url
tenant_group_url = api_url+"tenancy/tenant-groups/"

headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Token 72830d67beff4ae178b94d8f781842408df8069d'
}
tenant_group_name_list = ["NOC", "NOC_2", "123", "zsa1212"]


def test_tenant_url():
    def create_tenant_group():
        # Create Tenant Group NOC

        data_tenant_group = {
            "name": None,
            "slug": None,
            "parent": None,
            "description": "NOC"
        }
        response = requests.post(tenant_group_url, headers=headers,
                                 json=data_tenant_group)
        print("Creating new Tenant Group....")
        assert tenant_group_url == 'https://netboxdemo.com/api/tenancy/tenant-groups/'
        if response.status_code == 201:
            print("Tenant Group was sucessfully created!")
        else:
            print("Tenant Group creation went wrong! Try again :(")
            print(response.text)
    create_tenant_group()


def test_headers():
    def create_tenant_group():
        # Create Tenant Group NOC

        data_tenant_group = {
            "name": None,
            "slug": None,
            "parent": None,
            "description": "NOC"
        }
        response = requests.post(tenant_group_url, headers=headers,
                                 json=data_tenant_group)
        print("Creating new Tenant Group....")
        assert response.headers["Content-Type"] == "application/json"
        if response.status_code == 201:
            print("Tenant Group was sucessfully created!")
        else:
            print("Tenant Group creation went wrong! Try again :(")
            print(response.text)
    create_tenant_group()


def test_create_first_tenant():
    def create_tenant_group():
        data_tenant_group = {
            "name": tenant_group_name_list[0],
            "slug": tenant_group_name_list[0].lower(),
            "parent": None,
            "description": "NOC"
        }
        response = requests.post(tenant_group_url, headers=headers,
                                 json=data_tenant_group)
        print("Creating new Tenant Group....")
        assert response.status_code == 201
        if response.status_code == 201:
            print("Tenant Group was sucessfully created!")
        else:
            print("Tenant Group creation went wrong! Try again :(")
            print(response.text)
    create_tenant_group()


def test_create_second_tenant():
    def create_tenant_group():
        data_tenant_group = {
            "name": tenant_group_name_list[1],
            "slug": tenant_group_name_list[1].lower(),
            "parent": None,
            "description": "NOC"
        }
        response = requests.post(tenant_group_url, headers=headers,
                                 json=data_tenant_group)
        print("Creating new Tenant Group....")
        assert response.status_code == 201
        if response.status_code == 201:
            print("Tenant Group was sucessfully created!")
        else:
            print("Tenant Group creation went wrong! Try again :(")
            print(response.text)
    create_tenant_group()


def test_create_third_tenant():
    def create_tenant_group():
        data_tenant_group = {
            "name": tenant_group_name_list[2],
            "slug": tenant_group_name_list[2].lower(),
            "parent": None,
            "description": "NOC"
        }
        response = requests.post(tenant_group_url, headers=headers,
                                 json=data_tenant_group)
        print("Creating new Tenant Group....")
        assert response.status_code == 201
        if response.status_code == 201:
            print("Tenant Group was sucessfully created!")
        else:
            print("Tenant Group creation went wrong! Try again :(")
            print(response.text)
    create_tenant_group()


def test_create_fourth_tenant():
    def create_tenant_group():
        data_tenant_group = {
            "name": tenant_group_name_list[3],
            "slug": tenant_group_name_list[3].lower(),
            "parent": None,
            "description": "NOC"
        }
        response = requests.post(tenant_group_url, headers=headers,
                                 json=data_tenant_group)
        print("Creating new Tenant Group....")
        assert response.status_code == 201
        if response.status_code == 201:
            print("Tenant Group was sucessfully created!")
        else:
            print("Tenant Group creation went wrong! Try again :(")
            print(response.text)
    create_tenant_group()
