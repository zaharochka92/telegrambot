import netmiko
#from returns.result import Result, safe
#import routeros_api
# выполнение одной комманды из списка commands=[,,,,] это модифицированный чужой код

def mikrotik_cmd(dev):
    try:
        commands = '/system resource print'
        with  netmiko.ConnectHandler(**dev,default_enter="\n\r") as ssh:

              result=ssh.send_command(commands)
        result1=''
        result = result.split('\n')

        for line in result:
            result1+=' '.join(line.split())
            result1+='\n'
        return result1
    except Exception as e:
        return  f'Some error:{e}'

#i try api func later
# connection = routeros_api.RouterOsApiPool(ip, username='', password='', use_ssl=False)
# api = connection.get_api()
# list = api.get_resource('/interface wireless disable wlan2 ')
# print(list)
#
# connection.disconnect()