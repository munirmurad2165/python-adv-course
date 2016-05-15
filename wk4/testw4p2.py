
from getpass import getpass
import paramiko
import time
ip_addr='50.76.53.27'
username='pyclass'
password=getpass()
ssh_port=8022

remote_conn_pre=paramiko.SSHClient()
remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
remote_conn_pre.connect(ip_addr,username=username,password=password,port=ssh_port,look_for_keys=False,allow_agent=False)
remote_conn=remote_conn_pre.invoke_shell()

remote_conn.send("terminal length 0\n")
remote_conn.send("sh logging | inc Log Buffer\n")
time.sleep(2)
remote_conn.send("configure terminal\n")
remote_conn.send("logging buffer 68000\n")
remote_conn.send("exit\n")
remote_conn.send("sh logging | inc Log Buffer\n")
time.sleep(2)
while remote_conn.recv_ready():
    output=remote_conn.recv(500)
    print output
    #time.sleep(2)
