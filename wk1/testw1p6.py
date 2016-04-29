import yaml
import json

my_list=range(10)
my_list.append('whatever')
my_list.append('ice-cream')
my_list.append({})
my_list[-1]['ip_address']='10.10.10.1'
my_list[-1]['vendor']='cisco'
my_list[-1]['host_name']='rt1'

with open("testw1p6.yml","w") as f:
    f.write(yaml.dump(my_list,default_flow_style=False))

with open("testw1p6.json","w") as f:
    json.dump(my_list,f)



