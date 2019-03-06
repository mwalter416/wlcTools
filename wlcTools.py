from netmiko import ConnectHandler

class wlc:
    def __init__(self, ip, username, password):
        self.netmiko_wlc = {
                       'device_type': 'cisco_wlc',
                       'ip': ip,
                       'username': username,
                       'password': password
                      }
        self.net_connect = ConnectHandler(**self.netmiko_wlc)

    def getCmdOutput(self, cmd):
        return self.net_connect.send_command(cmd)

    def getApJoinStats(self):
        return self.net_connect.send_command('show ap join stats summary all')

    def disconnect(self):
        self.net_connect.disconnect()
