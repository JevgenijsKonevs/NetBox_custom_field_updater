import paramiko

ssh = paramiko.SSHClient()
# setup a connection
# replace 'hostname', 'username', 'password' with actual values
ssh.connect('192.168.101.10', port=22, username='evgeny', password='cisco')
# fix the problem with the known_hosts. Automatically add it
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# executing the command on the equipment to observer the software version
stdin, stdout, stderr = ssh.exec_command('show version')
# store the output
output = stdout.readLines()
print(output)
