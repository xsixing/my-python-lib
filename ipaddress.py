# -*- encoding: utf-8 -*-
__author__ = 'sx'

def inet_aton(ipaddress):
    ips = ipaddress.split('.')
    return ((int(ips[0])) << 24) + ((int(ips[1])) << 16) + ((int(ips[2])) << 8) + (int(ips[3]))

def inet_ntoa(ipaddress):
    return "{0}.{1}.{2}.{3}".format((ipaddress >> 24) & 0xFF, (ipaddress >> 16) & 0xFF, (ipaddress >> 8) & 0xFF, ipaddress & 0xff)

class NetworkAddress(object):
    def __init__(self, network_addr):
        slash_index = network_addr.find("/")
        if slash_index != -1:
            self.mask = int(network_addr[slash_index+1:])

            self.mask_int = ~((1 << (32 - self.mask + 1)) - 1)
            self.network_address = inet_aton(network_addr[0:slash_index]) & self.mask_int
        else:
            self.mask_int = 32
            self.network_address = inet_aton(network_addr) & self.mask_int

    def __str__(self):
        return "network address:{0}, netmask:{1}".format(inet_ntoa(self.network_address), self.mask)

    def __contains__(self, ip):
        ip2net = inet_aton(ip) & self.mask_int
        return ip2net == self.network_address

if __name__ == '__main__':
    net = NetworkAddress("192.168.1.129/26")
    print("192.168.1.34" in net)
