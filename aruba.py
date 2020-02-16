import argparse
import ArubaCloud
from ArubaCloud.PyArubaAPI import CloudInterface
from ArubaCloud.objects.VmTypes import Smart, Pro

ci = CloudInterface(dc=7)
ci.login(username="AWI-256466", password="jqoYS212-j", load=True)

ci.create_snapshot(dc=7, server_id=26293)
# print(ci.get_vm())
# print(ci.get_virtual_datacenter())

# ci.get_servers()
#

#
# for vm in ci.vmlist:
#     print("VM Name: {}".format(vm.vm_name))
#     print("VM Type: {}".format(type(vm)))
#
#     if isinstance(vm, Smart):
#         print("VM IP: {}".format(vm.ip_addr))
#     elif isinstance(vm, Pro):
#         for ip in vm.ip_addr:
#             print("VM IP: {}".format(ip.ip_addr))
#     print("############################")