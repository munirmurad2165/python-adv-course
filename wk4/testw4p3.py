
from getpass import getpass
import pexpect
import time
import sys

ip_addr='50.76.53.27'
username='pyclass'
password='88newclass'
ssh_port=8022

remote_conn=pexpect.spawn( 'ssh -l {} {} -p {}'.format(username,ip_addr,ssh_port ))
remote_conn.timeout=6
remote_conn.logfile=sys.stdout
remote_conn.expect('ssword:')
remote_conn.sendline(password)
#remote_conn.expect('#')
#print remote_conn.before
#print remote_conn.after

remote_conn.sendline('sh version')
remote_conn.expect('#')
print remote_conn.before
print remote_conn.after

