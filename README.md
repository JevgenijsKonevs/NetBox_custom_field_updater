
Python 3 based project to check the software version on different network equipments

Write an application that would collect information directly from the network devices, and update custom field in Netbox for each device.</br>

#### Task requirements:</br>

• Use https://netboxdemo.com/</br>
• Collect information for devices with Status = Active, Tenant = NOC in Netbox</br>
• Information to collect: software version</br>
• Custom field to update: "sw_version"</br>
Assume network device list would contain Cisco Catalyst IOS, Cisco Nexus OS, Cisco ASA OS, Aruba OS, PaloAlto PAN-OS (more device types covered more points).</br>

#### Code requirements:</br>


• Python version 3</br>
• Functional based style</br>
• Should contain unit tests – pytest should be used</br>
• Should pass pylint and black (optional)</br>


### Description :
The script was tested on https://netboxdemo.com as well as on manual NetBox setup, using Oracle VirtualBox with Ubuntu.</br> In order to test the code for device SSH connection, GNS3 software was used, where the test lab was set up, using different types of equipment and GNS3 LoopBack</br>
Simple example : </br>
![Capture1](https://user-images.githubusercontent.com/55871427/99528968-bbaebb80-29a7-11eb-8d2f-cf3cd78c20ed.JPG)</br>

For tenant and tenant group creation as well as create new device, get information regarding other devices and updating the custom field,</br> NetBox API was used, especially, POST / GET / PATCH requests. </br>
It is more conveniet to use PATCH request instead of PUT request, because PATCH request updates only necessary field.</br>
 
In order to get the script working properly you should have complete manual setup of NetBox and then change funtion "create_new_device()" "data" fields 
or you can use https://netboxdemo.com , where all racks, sites, device roles and types are already setup. </br>
It is important to mention that everything that you will create on https://netboxdemo.com will be cleared at 8:00 am UTC</br>

In addition, in order to run the pytests properly, you should change the input data as well such as "existing_tenant_group", "existing_tenant_slug", "existing_tenant", "existing_device_name", "device_role_list", "expected_dict"</br>

### Used sources :</br>
#### Netbox :</br>
• Netbox documentation https://netbox.readthedocs.io/en/stable/</br>
• What is a netbox and how to use netboxdemo https://packetpushers.net/netbox-demo-site-netboxdemo-com/</br>
• Netbox features https://youtu.be/X1BXS5N21TM</br>
• Netbox setup https://computingforgeeks.com/how-to-install-netbox-on-ubuntu-18-04-lts/</br>
      
####  Python Paramika module for SSH connection :</br>
• https://medium.com/@keagileageek/paramiko-how-to-ssh-and-file-transfers-with-python-75766179de73</br>
• http://www.paramiko.org/</br>
#### GNS3:</br>
• Connect GNS3 to the Internet https://docs.gns3.com/docs/using-gns3/advanced/connect-gns3-internet</br>
#### Pytest :</br>
• https://docs.pytest.org/en/stable/</br>

