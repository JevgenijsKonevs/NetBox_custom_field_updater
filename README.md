# SW_Checker
Python 3 based project to check the software version on different network equipments

Write an application that would collect information directly from the network devices, and update custom field in Netbox for each device.</br>
#### Task requirements:</br>
•	Use https://netboxdemo.com/</br>
•	Collect information for devices with Status = Active, Tenant = NOC in Netbox</br>
•	Information to collect: software version</br>
•	Custom field to update: "sw_version"</br>
Assume network device list would contain Cisco Catalyst IOS, Cisco Nexus OS, Cisco ASA OS, Aruba OS, PaloAlto PAN-OS (more device types covered more points).</br>
#### Code requirements:</br>
•	Python version 3</br>
•	Functional based style</br>
•	Should contain unit tests – pytest should be used</br>
•	Should pass pylint and black (optional)</br>

### Useful info :
#### Netbox :</br>
      • Netbox documentation https://netbox.readthedocs.io/en/stable/
      • What is a netbox and how to use netboxdemo https://packetpushers.net/netbox-demo-site-netboxdemo-com/
      • Netbox features https://youtu.be/X1BXS5N21TM
      • Netbox review https://youtu.be/-pdTU_9wCAg
#### Netbox API :</br>
      • Netbox API documentation https://netboxdemo.com/api/docs/
      • Probable API to use https://netboxdemo.com/api/dcim/devices/
      • API access token '72830d67beff4ae178b94d8f781842408df8069d'
      
####  Python Paramika module for SSH connection :</br>
      • https://medium.com/@keagileageek/paramiko-how-to-ssh-and-file-transfers-with-python-75766179de73
      • http://www.paramiko.org/
      • https://www.youtube.com/watch?v=kvPa85M9z2Q&ab_channel=TheIPSchool
####  Python for Telnet connection :</br>      
      • https://youtu.be/IhroIrV9_7w
      • https://docs.python.org/3.1/library/telnetlib.html
#### Pytest :</br>      
      • https://docs.pytest.org/en/stable/
