import time
import sys
from  telnetlib import Telnet



TELNET_PORT=23
TELNET_TIMEOUT=6


class TelnetConnect(object):
    def __init__(self,ip_addr,username,password):
        self.ip_addr=ip_addr
        self.username=username
        self.password=password
        try: 
            self.remote_conn= Telnet(self.ip_addr, TELNET_PORT, TELNET_TIMEOUT)
        except soket.timeout:
            sys.exit("Timeout Connection")

    def login(self,sleep_time=1):
        output=self.remote_conn.read_until('sername:',TELNET_TIMEOUT)
        self.remote_conn.write(self.username +'\n')
        output+=self.remote_conn.read_until('assword:', TELNET_TIMEOUT)
        self.remote_conn.write(self.password+'\n')
        time.sleep(sleep_time)
        output+=self.remote_conn.read_very_eager()
        return output

    def send_command(self,cmd,sleep_time=1):
        cmd=cmd.rstrip()
        self.remote_conn.write(cmd + '\n')
        time.sleep(sleep_time)
        return self.remote_conn.read_very_eager()
    
    def close_conn(self):
        self.remote_conn.close()

def main():
    
        ip_addr='50.76.53.27'
        username='pyclass'
        password='88newclass'
    
        my_conn=TelnetConnect(ip_addr,username,password)
        output=my_conn.login()
        output+=my_conn.send_command('terminal length 0')
        output+=my_conn.send_command('sh ip int brief')
        print output 
        my_conn.close_conn()

if __name__=='__main__':
    main()
