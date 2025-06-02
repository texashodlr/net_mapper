import csv
from ping3 import ping, verbose_ping

# 192.168.1.0,24
# 192.168.2.0,24

range_file = "subnet_range.csv"
endpoints = []
with open(range_file, 'r') as f:
    reader = csv.reader(f)
    subnet_range = [row for row in reader]    

for i in range(len(subnet_range)):
    current_subnet = subnet_range[i][0]
    current_subnet_size = subnet_range[i][1]
    # print(f"Subnet: {current_subnet} | Size: {current_subnet_size}\n")
    for i in range(2**(32-int(current_subnet_size))):
        if i > 1 and i < 255:
            temp_sub = current_subnet[:-1]
            IP = temp_sub + str(i)
            # print(f"IP: {IP}\n")
            # print(f"Pinging {IP}: {ping(IP)}\n")
            response = ping(IP,timeout=2)
            # print(f"Response: {response}\n")
            if response is not None:
                print(f"Endpoint detected at: {IP}\n")
                endpoints.append(IP)

print(f"Detected endpoints are:\n\n{endpoints}")
