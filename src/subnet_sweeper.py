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
