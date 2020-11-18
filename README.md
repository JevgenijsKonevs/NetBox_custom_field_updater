# SW_Checker

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
It is more convenietn to use PATCH request instead of PUT request, because PATCH request updates only necessary field.</br>



#### Netbox :</br>

      • Netbox documentation https://netbox.readthedocs.io/en/stable/
      • What is a netbox and how to use netboxdemo https://packetpushers.net/netbox-demo-site-netboxdemo-com/
      • Netbox features https://youtu.be/X1BXS5N21TM
      • Netbox review https://youtu.be/-pdTU_9wCAg
      • Netbox API https://netboxdemo.com/api/docs/ (naybe to use in order to filter the devices by status and model. Look for "Device" )

#### Python Paramika module for SSH connection :</br>

      • Netboxdemo login and password : netbox,netbox
#### Netbox API :</br>
      • Netbox API documentation https://netboxdemo.com/api/docs/
      • Probable API to use https://netboxdemo.com/api/dcim/devices/
      • API access token '72830d67beff4ae178b94d8f781842408df8069d'
      • Request Url with (Status = Active, Tenant = noc) https://netboxdemo.com/api/dcim/devices/?tenant=noc&status=active
  ![API](https://user-images.githubusercontent.com/55871427/98450154-fbbda500-2142-11eb-88f8-6b7438432217.JPG)

      
####  Python Paramika module for SSH connection :</br>
      • https://medium.com/@keagileageek/paramiko-how-to-ssh-and-file-transfers-with-python-75766179de73
      • http://www.paramiko.org/
      • https://www.youtube.com/watch?v=kvPa85M9z2Q&ab_channel=TheIPSchool

#### Python for Telnet connection :</br>

      • https://youtu.be/IhroIrV9_7w
      • https://docs.python.org/3.1/library/telnetlib.html

#### Pytest :</br>

      • https://docs.pytest.org/en/stable/

