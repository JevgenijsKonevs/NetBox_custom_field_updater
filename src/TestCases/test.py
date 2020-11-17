import requests
import json
import paramiko
import pytest
import re
import sys
import os

sys.path.insert(0, '..//main/')
import api

existing_tenant_group = "NOC"
existing_tenant_slug = "noc"
existing_tenant = "NOC"
existing_device_name = "test_device_50"
device_role_list = ["Access Switch", "Core Switch", "Firewall", "Fiber Patch Panel"]
new_device_name = "test_device_55"
new_tenant_group = "NOC_2"
new_tenant_slug = "noc_2"
new_tenant = "NOC_2"


# create_tenant_group() tests
def test_tenant_group_exception_existing():
    with pytest.raises(Exception):
        api.create_tenant_group(existing_tenant_group, existing_tenant_slug)


def test_tenant_group_status():
    expected_status_code = 201
    actual_status_code = api.create_tenant_group(new_tenant_group, new_tenant_slug)
    assert expected_status_code == actual_status_code


# create_tenant() tests
def test_tenant_exception_existing():
    with pytest.raises(Exception):
        api.create_tenant(existing_tenant, existing_tenant_slug)


def test_tenant_status():
    expected_status_code = 201
    actual_status_code = api.create_tenant(new_tenant, new_tenant_slug)
    assert expected_status_code == actual_status_code


# create_device() tests
def test_created_device_status():
    expected_status_code = 201
    actual_status_code = api.create_new_device(new_device_name, device_role_list[0])
    assert expected_status_code == actual_status_code


def test_existing_device_exception():
    with pytest.raises(Exception):
        api.create_new_device(existing_device_name, device_role_list[1])


# get_device_info() tests
def test_get_device_dict():
    expected_dict = {44: "192.168.100.1", 38: "192.168.100.1", 39: "192.168.100.1"}
    actual_dict = api.get_device_info()
    assert expected_dict == actual_dict


# get_device_sw_version tests
def test_output_dict():
    expected_dict = {44: "Version 12.4(6)T3", 38: "Version 12.4(6)T3", 39: "Version 12.4(6)T3"}
    actual_dict = api.get_device_sw_version()
    assert expected_dict == actual_dict


# update_device_sw_version() tests
def test_update_device_sw_status():
    expected_status_code = 204
    actual_status_code = api.update_custom_field()
    assert expected_status_code == actual_status_code


def test_update_device_exception():
    with pytest.raises(Exception):
        api.update_custom_field()
