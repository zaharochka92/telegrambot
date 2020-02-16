import netmiko
from pprint import pprint

# выполнение одной комманды из списка commands=[,,,,]
def send_show_command(dev,commands):
    with  netmiko.ConnectHandler(**dev,default_enter="\n\r") as ssh:
#          print ('prompt:',ssh.find_prompt())
          result=ssh.send_command(commands)
    return result

command = '/interface print brief'
show_command=send_show_command({'device_type':'cisco_ios','username':'admin+ct80h','password':'zakharov1992','verbose':True,'ip':'192.168.42.100'},command)
print(show_command)