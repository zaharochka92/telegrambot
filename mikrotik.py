import netmiko
from pprint import pprint

# выполнение одной комманды из списка commands=[,,,,] это модифицированный чужой код
def mikrotik_cmd(ip):
    dev={'device_type':'cisco_ios','username':'admin+ct80h','password':'zakharov1992','verbose':True,'ip':ip}
    commands = '/system resource print'
    with  netmiko.ConnectHandler(**dev,default_enter="\n\r") as ssh:

          result=ssh.send_command(commands)
    result1=''
    result = result.split('\n')

    for line in result:
        result1+=' '.join(line.split())
        result1+='\n'
    return result1

