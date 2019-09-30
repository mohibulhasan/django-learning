from django import forms
#from django import paramiko

import sys


def sshrouter(val):
    # do something
    
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    hostname = input("Enter host IP address: ")
    username = input("Enter SSH Username: ")
    password = input("Enter SSH Password: ") 
    port = 22

    ssh.connect(hostname, port, username, password, look_for_keys=False)
    stdin,stdout,stderr = ssh.exec_command('show users')
    output = stdout.readlines()
    print ('\n'.join(output))
    print (val)
    # return something
    return val

if __name__ == '__main__':
    try:
        arg = sys.argv[1]
    except IndexError:
        arg = None

    return_val = sshrouter(arg)


#ssh = paramiko.SSHClient()
#ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

#hostname = input("Enter host IP address: ")
#username = input("Enter SSH Username: ")
#password = input("Enter SSH Password: ")
#port = 22

#ssh.connect(hostname, port, username, password, look_for_keys=False)
#stdin,stdout,stderr = ssh.exec_command('show users')
#output = stdout.readlines()
#print ('\n'.join(output))
