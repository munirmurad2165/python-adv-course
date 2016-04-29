from ciscoconfparse import CiscoConfParse


def main():

    cisco_cfg=CiscoConfParse("cisco_ipsec.txt")

    crypto_map=cisco_cfg.find_objects_w_child(parentspec=r'crypto map CRYPTO', childspec=r'pfs group2')

    print "Crypto Map Using PFS Group2: "

    for child in crypto_map:
        print "{0}".format(child.text)
    #for ch in child.children:
     #   print ch.itext
if __name__=="__main__":
    main()


