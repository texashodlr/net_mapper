import csv
import random
from ping3 import ping, verbose_ping

"""
subnet_sweeper.py 'sweeps' subnets pinging all IPs in a subnet and return list of
hosts or IPs that responded to the ping. This file also contains a generator function
which spawns a selection of hosts randomly within a subnet, for graph testing.
"""

def subnet_sweep(range_file = "subnet_range.csv"):
    """
    This function ingests a subnet file with ranges in the form of:
        X.X.X.X,ZZ where X are IPs (192.X etc) and ZZ is the subnet mask,
        Ex: 192.168.1.0,24 Will scan the entire 192.168.1.0/24 subnet from .1 to .255
    The function then returns a list of all endpoints of this form:
        ['192.168.1.1', '192.168.1.3'....] --> All elements are a string.
    """
    endpoints = []
    with open(range_file, 'r') as f:
        reader = csv.reader(f)
        subnet_range = [row for row in reader]    

    for i in range(len(subnet_range)):
        current_subnet = subnet_range[i][0]
        current_subnet_size = subnet_range[i][1]
        for j in range(2**(32-int(current_subnet_size))):
            if j > 1 and j < 255:
                temp_sub = current_subnet[:-1]
                IP = temp_sub + str(j)
                response = ping(IP,timeout=.25)
                # print(f"Response: {response}\n")
                if response is not None and response is not False:
                    print(f"Endpoint detected at: {IP}\n")
                    endpoints.append(IP)
    return endpoints

def subnet_discovery(self_ip = "127.0.0.1"):
    """
    This function is structured similarly to subnet_sweep but is intended 
    to be used for scanning the subnet where the current host is on.
        Ex: Host IP is 172.65.10.6, this function will then scan the entire
            172.65.10.0/24 subnet then return an endpoints list of strings
            like it does in subnet_sweep
    """
    endpoints = []
    ip_octets = self_ip.split('.')
    if len(ip_octets) != 4 or not all(ip_octet.isdigit() and 0 <= int(ip_octet) <= 255 for ip_octet in ip_octets):
        raise ValueError(f"Invalid IPv4 address: {ip_string}")
    starting_ip = '.'.join(ip_octets[:3])+'.'
    print(f"Starting IP: {starting_ip}\n")
    for i in range(255):
        if i > 1 and i < 255:
            IP = starting_ip + str(i)
            response = ping(IP,timeout=.25)
            # print(f"Response: {response}\n")
            if response is not None and response is not False:
                print(f"Endpoint detected at: {IP}\n")
                endpoints.append(IP)
    return endpoints

def subnet_generate(count = 0):
    """
    This function is used for testing of network_graph.
    It takes a count of how many random 'network clusters' to create
    and then spawns clusters on a single subnet.
    It is set to 20 hosts for spawning.
    """
    random_subnets = [None]*10
    random_gateways= [None]*10
    for i in range(count):
        # Generate a randomized subnet
        octets = [str(random.randint(0,254)) for _ in range (3)]
        subnet = '.'.join(octets)+'.'
        # Generate gateway
        gateway = subnet+'1'
        # Generate 10 hosts
        subnet_range = [None]*20
        for j in range(20):
            last_octet = str(random.randint(0,254))
            subnet_range[j] = subnet + last_octet
        random_subnets[i] = subnet_range
        random_gateways[i] = gateway
    random_subnets_gateways = [random_subnets, random_gateways]
    return random_subnets_gateways