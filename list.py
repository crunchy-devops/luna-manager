#! /usr/bin/env python
from lndynamic import LNDynamic

with open(r"../../system-dev.txt") as hpass:
    lines = hpass.readlines()


api = LNDynamic(lines[0].rstrip('\n'), lines[1].rstrip('\n'))
results = api.request('vm', 'list')
val = results.get('vms')
print(val)
print (type(val))
print (val[0])
d = val[0]
print(d['vm_id'])
print(d['name'])
print(d['plan_id'])
print(d['hostname'])
print(d['primaryip'])
print(d['privateip'])
print(d['ram'])
print(d['vcpu'])
print(d['storage'])
print(d['region'])
print(d['os_status'])


element = dict()
element['vm_id'] = d['vm_id']
vm_info= api.request('vm', 'info', element)
print(vm_info)
print(vm_info['info'])
val = vm_info['info']
#print (val['image'])
print(val['login_details'])
list_images = api.request('image', 'list')
#print(list_images)
print(d['region'])
create = dict()
create['hostname'] = 'test'
create['plan_id'] = d['plan_id']
create['region'] = d['region']
create['storage'] = d['storage']
for a in list_images['images']:
    #print(a)
    if a['region'] == d['region'] and a['name'] == val['image']:
        print(a['image_id'])
        create['image_id'] = a['image_id']
api.request("vm", "create", create)
