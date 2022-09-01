from lndynamic import LNDynamic

with open(r"../../../system-dev.txt") as hpass:
    lines = hpass.readlines()

all_api = LNDynamic(lines[0].rstrip('\n'), lines[1].rstrip('\n'))

class api(object):
    def __init__(self, all_api):
        self.all_api = all_api

    def get_vm(self):
        all = self.all_api.request('vm', 'list')
        value = all.get('vms')
        self.number_vm = len(value)
        return value

    def vm_info(self, rank):
        info = []
        val = self.get_vm()
        info.append(val[rank]['vm_id'])
        info.append(val[rank]['name'])
        info.append(val[rank]['plan_id'])
        info.append(val[rank]['hostname'])
        info.append(val[rank]['primaryip'])
        info.append(val[rank]['privateip'])
        info.append(val[rank]['ram'])
        info.append(val[rank]['vcpu'])
        info.append(val[rank]['storage'])
        info.append(val[rank]['region'])
        info.append(val[rank]['os_status'])
        return info

    def vm_detail(self, rank):
        element = dict()
        val = self.get_vm()
        element['vm_id'] = val[rank]['vm_id']
        vm_info = self.all_api.request('vm', 'info', element)
        item =  vm_info['info']
        return item

    def get_image_id(self,rank):
        vm = self.vm_info(rank)
        region = vm[9]
        vm_detail = self.vm_detail(rank)
        image_name = vm_detail['image']
        list_images = self.all_api.request('image', 'list')
        for a in list_images['images']:
            if a['region'] == region and a['name'] == image_name :
                image_id = a['image_id']
                return image_id
        return None

    def create_vm(self, hostname, rank):
        vm = self.vm_info(rank)
        parameter = dict()
        parameter['hostname'] = hostname
        parameter['plan_id'] = vm[2]
        parameter['region'] = vm[9]
        parameter['storage'] = vm[8]
        parameter['image_id'] = self.get_image_id(rank)
        self.all_api.request("vm", "create", parameter)




if __name__ == '__main__':
    test_api = api(all_api)
    vms = test_api.get_vm()
    print(len(vms))
    for i in range(0,len(vms)):
        print(test_api.vm_info(i))
        print(test_api.vm_detail(i))
        #print(test_api.get_image_id(i))

    #test_api.create_vm("git-trainee-1",0)

