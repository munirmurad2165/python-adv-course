from snmp_helper import snmp_get_oid, snmp_extract

COMMUNITY_STRING='galileo'
#SNMP_PORT=8061
IP='50.76.53.27'
SYS_DESCRP='1.3.6.1.2.1.1.1.0'
SYS_NAME='1.3.6.1.2.1.1.5.0'



def main():

    pynet_rtr1=(IP,COMMUNITY_STRING,7961)
    pynet_rtr2=(IP,COMMUNITY_STRING,8061)

    for a_device in (pynet_rtr1,pynet_rtr2):
        for oid_data in (SYS_DESCRP,SYS_NAME):
            snmp_data=snmp_get_oid(a_device,oid=oid_data)
            output=snmp_extract(snmp_data)
            print '\n'
            print output

if __name__=="__main__":
    main()



