import csv
import random
from ping3 import ping, verbose_ping


def subnet_sweep(range_file = "subnet_range.csv"):
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