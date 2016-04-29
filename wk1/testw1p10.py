from ciscoconfparse import CiscoConfParse
import re


def main():

    cisco_cfg=CiscoConfParse("cisco_ipsec.txt")

    crypto_map=cisco_cfg.find_objects_wo_child(parentspec=r'crypto map CRYPTO', childspec=r'AES')

    for child in crypto_map:
        #print child.text
        for ch in child.children:
            if 'transform-set' in ch.text:
                match=re.search(r'set transform-set (.*)',ch.text)
                result=match.group(1)
                print "{0}>>> {1}".format(child.text,result)

if __name__ == "__main__":
    main()


