import time
import pygal
import json
import snmp_helper
import email_helper
from pprint import pprint


IP='50.76.53.27'
pynet_rtr1=(IP,7961)
pynet_rtr2=(IP,8061)
username='pysnmp'
auth_key='galileo1'          
encrypt_key='galileo1'

snmp_user=(username,auth_key,encrypt_key)
snmp_oids=(
('ifDescr_fa4', '1.3.6.1.2.1.2.2.1.2.5'),
('ifInOctets_fa4', '1.3.6.1.2.1.2.2.1.10.5'),
('ifInUcastPkts_fa4', '1.3.6.1.2.1.2.2.1.11.5'),
('ifOutOctets_fa4', '1.3.6.1.2.1.2.2.1.16.5'),
('ifOutUcastPkts_fa4', '1.3.6.1.2.1.2.2.1.17.5')
)

a_list=[]
minit=range(1,6,1)
in_octets=[]
out_octets=[]
in_pkts=[]
out_pkts=[]

for t in minit:
    time.sleep(t)
    
    for desc,a_oid in snmp_oids:
        snmp_data=snmp_helper.snmp_get_oid_v3(pynet_rtr1,snmp_user,oid=a_oid)
        snmp_extracts=snmp_helper.snmp_extract(snmp_data)
        tup=(desc,a_oid,snmp_extracts)
        a_list.append(tup)
        if desc== snmp_oids[1][0]:
            in_octets.append(int(snmp_extracts))
            #print in_octets
        elif desc==snmp_oids[2][0]:
            out_octets.append(int(snmp_extracts))
        elif desc==snmp_oids[3][0]:
            in_pkts.append(int(snmp_extracts))
        elif desc==snmp_oids[4][0]:
            out_pkts.append(int(snmp_extracts))     

    '''    
    with open ("testw3p2.json", "ab")as f:
        json.dump(a_list,in_octets,out_octets,in_pkts,out_pkts,f)
        json.dump("\n\n",f)
        

    with open ("testw3p2.json","rb") as f1:
        for line in f1:
            pprint(line)

    '''

print "Input_Octets: ", in_octets
print "Output Octets: ", out_octets
print "Input Pkts: ",in_pkts
print "Output Pkts: ",out_pkts


# Create a Chart of type Line
line_chart = pygal.Line()

# Title
line_chart.title = 'Input/Output Packets and Bytes'

# X-axis labels (samples were every five minutes)
line_chart.x_labels = ['1', '2', '3', '4', '5']
#line_chart.x_labels = ['5', '10', '15', '20', '25', '30','35','40','45','50','55','60']
# Add each one of the above lists into the graph as a line with corresponding label
line_chart.add('InPackets', in_pkts)
line_chart.add('OutPackets',out_pkts)
line_chart.add('InBytes', in_octets)
line_chart.add('OutBytes', out_octets)

# Create an output image file from this
line_chart.render_to_file('testw3p2.svg')





def send_mail(recipient, subject, message, sender):
    '''
    Simple function to help simplify sending SMTP email

    Assumes a mailserver is available on localhost
    '''

    import smtplib
    from email.mime.text import MIMEText

    message = MIMEText(message)
    message['Subject'] = subject
    message['From'] = sender
    message['To'] = recipient

    # Create SMTP connection object to localhost
    smtp_conn = smtplib.SMTP('localhost')

    # Send the email
    smtp_conn.sendmail(sender, recipient, message.as_string())

    # Close SMTP connection

    smtp_conn.quit()

    return True





recipient = 'nazfroz@gmail.com;murad2165@gmail.com'
subject = 'Test message'
message ='''
Hi Upoma,

I Love You!!
Happy Future Mothers Day!

This is a fictional test message.


Regards,

Murad

'''

sender = 'mmurad@twb-tech.com'
email_helper.send_mail(recipient, subject, message, sender)







