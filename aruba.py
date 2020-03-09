import argparse
import ArubaCloud
from ArubaCloud.PyArubaAPI import CloudInterface
from ArubaCloud.objects.VmTypes import Smart, Pro
from teletokens import *

def arubainfo(username, password):
    try:
        ci = CloudInterface(dc=7)
        ci.login(username=username, password=password, load=True)
        json_data=ci.get_virtual_datacenter()
        # print(json.dumps(json_data,indent=2))
        pprint.pprint(json_data)

        for vm in ci.vmlist:
            print("VM Name: {}".format(vm.vm_name))
            print("VM Type: {}".format(type(vm)))

            print("VM IP: {}".format(vm.ip_addr))
            print("############################")
    except:
        return 'some_error'
