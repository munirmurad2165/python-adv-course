

import paramiko
import time
ip_addr='50.76.53.27'
username='pyclass'
password='88newclass'
ssh_port=8022

remote_conn_pre=paramiko.SSHClient()
remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
remote_conn_pre.connect(ip_addr,username=username,password=password,port=ssh_port,look_for_keys=False,allow_agent=False)
remote_conn=remote_conn_pre.invoke_shell()

remote_conn.send("terminal length 0\n")
remote_conn.send("sh version\n")
time.sleep(2)
while remote_conn.recv_ready():
    output=remote_conn.recv(500)
    print output
    #time.sleep(2)
