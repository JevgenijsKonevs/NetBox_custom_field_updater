import requests
import json
import re

# API url
api_url = 'https://netboxdemo.com/api/'
# Tenant Group url
tenant_url = api_url+"tenancy/tenants/"

headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Token 72830d67beff4ae178b94d8f781842408df8069d'
}
tenant_name_list = ["NOC", "network", "123", "zsa1212"]
tenant_group = "NOC"


def test_tenant_headers():
    def create_tenant():
        # Create Tenant NOC
        data_tenant = {
            "name": tenant_name_list[0],
            "slug": tenant_name_list[0].lower(),
            "group": {"name": tenant_group},
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
        assert response.headers["Content-Type"] == "application/json"
        if response.status_code != 201:
            raise Exception(
                "Tenant creation went wrong! Try again :(\n"+response.text)
        print("Tenant was sucessfully created!")
    create_tenant()


def test_tenant_creation_one():
    def create_tenant():
        data_tenant = {
            "name": tenant_name_list[0],
            "slug": tenant_name_list[0].lower(),
            "group": {"name": tenant_group},
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
        assert response.status_code == 201
        if response.status_code != 201:
            raise Exception(
                "Tenant creation went wrong! Try again :(\n"+response.text)
        print("Tenant was sucessfully created!")
    create_tenant()


def test_tenant_creation_two():
    def create_tenant():
        data_tenant = {
            "name": tenant_name_list[1],
            "slug": tenant_name_list[1].lower(),
            "group": {"name": tenant_group},
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
        assert response.status_code == 201
        if response.status_code != 201:
            raise Exception(
                "Tenant creation went wrong! Try again :(\n"+response.text)
        print("Tenant was sucessfully created!")
    create_tenant()


def test_tenant_creation_three():
    def create_tenant():
        data_tenant = {
            "name": tenant_name_list[2],
            "slug": tenant_name_list[2].lower(),
            "group": {"name": tenant_group},
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
        assert response.status_code == 201
        if response.status_code != 201:
            raise Exception(
                "Tenant creation went wrong! Try again :(\n"+response.text)
        print("Tenant was sucessfully created!")
    create_tenant()


def test_tenant_creation_four():
    def create_tenant():
        data_tenant = {
            "name": tenant_name_list[3],
            "slug": tenant_name_list[3].lower(),
            "group": {"name": tenant_group},
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
        assert response.status_code == 201
        if response.status_code != 201:
            raise Exception(
                "Tenant creation went wrong! Try again :(\n"+response.text)
        print("Tenant was sucessfully created!")
    create_tenant()
