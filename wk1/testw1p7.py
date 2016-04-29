import yaml
import json
from pprint import pprint
#import testw1p6.yml
#import testw1p6.json

'''
my_list=range(10)
my_list.append('whatever')
my_list.append('ice-cream')
my_list.append({})
my_list[-1]['ip_address']='10.10.10.1'
my_list[-1]['vendor']='cisco'
my_list[-1]['host_name']='rt1'
'''

with open("testw1p6.yml","r") as f:
    new_list=yaml.load(f)

print "\n Yaml File: \n"
pprint(new_list)

print "\n\n\n"

with open("testw1p6.json","r") as f:
    new_list2=json.load(f)

print "\n Json File: \n"
pprint(new_list2)


