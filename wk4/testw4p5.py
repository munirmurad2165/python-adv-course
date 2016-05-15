import time
from netmiko import ConnectHandler
from getpass import getpass

password=getpass()

pynet1={
    'device_type':'cisco_ios',
    'ip':'50.76.53.27', 
    'username':'pyclass',
    'password':password,   
    'port':22
    }

pynet2={
    'device_type':'cisco_ios',
    'ip':'50.76.53.27',
    'username':'pyclass',
    'password':password,
    'port':8022
    }
juniper_srx={
    'device_type':'juniper',
    'ip':'50.76.53.27',
    'username':'pyclass',
    'password':password,
    'secret':'',
    'port':9822
    }

pynet_rtr1=ConnectHandler(**pynet1)
pynet_rtr2=ConnectHandler(**pynet2)
srx=ConnectHandler(**juniper_srx)

print pynet_rtr1.find_prompt()
print pynet_rtr2.find_prompt()
print srx.find_prompt()

pynet_rtr1.config_mode()
print pynet_rtr1.check_config_mode()
print pynet_rtr1.find_prompt()
pynet_rtr1.send_command("end")
print pynet_rtr1.send_command("sh version")
list_of_command=['logging buffer 9800','logging buffer 1000']
print pynet_rtr1.send_config_set(list_of_command)
time.sleep(2)
print pynet_rtr1.find_prompt()
print pynet_rtr1.send_command("sh logging | inc Log Buffer")
print pynet_rtr1.send_config_from_file(config_file='test.txt')
