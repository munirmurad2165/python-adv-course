import time
import sys
from  telnetlib import Telnet

def telnet_conn(ip_addr, TELNET_PORT,TELNET_TIMEOUT):
    return Telnet(ip_addr, TELNET_PORT, TELNET_TIMEOUT)

def login(remote_conn,username,password,TELNET_TIMEOUT):
    output=remote_conn.read_until('sername:', TELNET_TIMEOUT)
    remote_conn.write(username +'\n')
    output+=remote_conn.read_until('assword:', TELNET_TIMEOUT)
    remote_conn.write(password+'\n')
    time.sleep(1)
    output+=remote_conn.read_very_eager()
    return output

def send_command(remote_conn,cmd):
    cmd=cmd.rstrip()
    remote_conn.write(cmd + '\n')
    time.sleep(1)
    return remote_conn.read_very_eager()

def main():
    
    ip_addr='50.76.53.27'
    TELNET_PORT=23
    TELNET_TIMEOUT=6
    username='pyclass'
    password='88newclass'
    
    remote_conn=telnet_conn(ip_addr, TELNET_PORT, TELNET_TIMEOUT)

    output=login(remote_conn,username,password,TELNET_TIMEOUT)
    output+=send_command(remote_conn,'terminal length 0')
    output+=send_command(remote_conn,'sh ip int brief')
    print output 
    remote_conn.close()

if __name__=='__main__':
    main()
