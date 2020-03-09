from __future__ import print_function, unicode_literals
from netmiko import Netmiko
from teletokens import *



device = {
    'host': host,
    'username': hostusername,
    'password': hostpassword,
    'device_type': 'autodetect',
    'port': port
}

command = ['cd /telegrambot', f'git pull {gitrepo} master',
           'docker stop telebot-docker telebot-docker', 'docker rm telebot-docker', 'docker build -t telebot-docker .', 'docker run -it -P  --restart unless-stopped --name telebot-docker telebot-docker' ]

net_connect = Netmiko(**device)
for cmd in command:
    output = net_connect.send_command_timing(cmd, delay_factor=2)
    if output:
        print(output)
net_connect.disconnect()

