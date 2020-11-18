import api
import requests
import pytest
import sys
import os

sys.path.insert(0, '..//main/')
# Pass these variable in tests in order to test the exceptions
existing_tenant_group = "NOC"
existing_tenant_slug = "noc"
existing_tenant = "NOC"
existing_device_name = "test_device_50"
# Device role list that exists and configured on Netbox
device_role_list = ["Access Switch",
                    "Core Switch", "Firewall", "Fiber Patch Panel"]
# Pass these variables in tests in order to test the creation of device / tenant / tenant group
# Works only on netboxdemo.com
# In order to get function "create_new_device()" works on other NetBox, "site", "rack" "platform" should be edited
new_device_name = "test_device_55"
new_tenant_group = "NOC_2"
new_tenant_slug = "noc_2"
new_tenant = "NOC_2"


# create_tenant_group() tests

# Passing the existing tenant slug and tenant group on netboxdemo.com
# in order to test the exception
def test_tenant_group_exception_existing():
    with pytest.raises(Exception):
        api.create_tenant_group(existing_tenant_group, existing_tenant_slug)

# Passing the new tenant_group and tenant_slug in order to test the POST request status code
# 201 = successful


def test_tenant_group_status():
    expected_status_code = 201
    actual_status_code = api.create_tenant_group(
        new_tenant_group, new_tenant_slug)
    assert expected_status_code == actual_status_code


# create_tenant() tests

# Passing the existing tenant slug and tenant on netboxdemo.com
# in order to test the exception


def test_tenant_exception_existing():
    with pytest.raises(Exception):
        api.create_tenant(existing_tenant, existing_tenant_slug)

# Passing the new tenant and tenant_slug in order to test the POST request status code
# 201 = successful


def test_tenant_status():
    expected_status_code = 201
    actual_status_code = api.create_tenant(new_tenant, new_tenant_slug)
    assert expected_status_code == actual_status_code


# create_device() tests

# Creating new device in order to test the POST request status code
# 201 = successful


def test_created_device_status():
    expected_status_code = 201
    actual_status_code = api.create_new_device(
        new_device_name, device_role_list[0])
    assert expected_status_code == actual_status_code

# Passing the existing device name on netboxdemo.com
# in order to test the exception


def test_existing_device_exception():
    with pytest.raises(Exception):
        api.create_new_device(existing_device_name, device_role_list[1])


# get_device_info() test

# Passing the expected dictionary to the function in order to test the actual dictionary
# which will be made by function.
# expected_dict should be edited in format {id : primary_ip} in order to test for other devices


def test_get_device_dict():
    expected_dict = {44: "192.168.100.1",
                     38: "192.168.100.1", 39: "192.168.100.1"}
    actual_dict = api.get_device_info()
    assert expected_dict == actual_dict


# get_device_sw_version() test

# Passing the expected dictionary to the function in order to test the actual dictionary
# which will be made by function.
# expected_dict should be edited in format {id : software_version} in order to test for other devices


def test_output_dict():
    expected_dict = {
        44: "Version 12.4(6)T3", 38: "Version 12.4(6)T3", 39: "Version 12.4(6)T3"}
    actual_dict = api.get_device_sw_version()
    assert expected_dict == actual_dict


# update_device_sw_version() test

# updating the custom fields (sw_version) on NetBox in order to test the response status
# 200 = successful


def test_update_device_sw_status():
    expected_status_code = 200
    actual_status_code = api.update_custom_field()
    assert expected_status_code == actual_status_code
