from netmiko import ConnectHandler

lullaby = {'device_type': 'cisco_xe', 'host': '192.168.119.129', 'username': 'adam', 'password': ''}

show = ['show ip int br', 'show ip protocols', 'show ip eigrp interfaces']
config = ['router eigrp 1', 'network 10.0.0.0']

with ConnectHandler(**lullaby) as net_connect:
    output = net_connect.send_config_set(config)
    output = net_connect.send_command(show)
    output += net_connect.save_config()

print()
print(output)
print()
