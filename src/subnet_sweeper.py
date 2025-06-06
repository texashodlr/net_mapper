import csv
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
    if len(ip_octets) != 4 or not all(ip_octets.isdigit() and 0 <= int(ip_octets) <= 255 for ip_octet in ip_octets):
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
