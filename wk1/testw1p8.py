from ciscoconfparse import CiscoConfParse

cisco_cfg=CiscoConfParse("cisco_ipsec.txt")

crypto_map=cisco_cfg.find_objects(r'crypto map CRYPTO')

for child in crypto_map:
    print child.text
    for ch in child.children:
        print ch.text


