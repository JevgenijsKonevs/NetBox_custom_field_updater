import getpass
import telnetlib

HOST = "hostname"
user = input("Enter your username: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

tn.write("enable"+b"\n")
tn.write(password+b"\n")
tn.write("show version"+b"\n")

print(tn.read_all().decode('ascii'))

qweqweqweqw