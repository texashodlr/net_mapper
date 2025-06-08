# Network Mapper
This repo is a python project that helps a user graphically map out endpoints in a network and produces the resulting map in a browser.

## Network Topology Visualizer Tool
The point of this tool is to scan a collection of subnet(s) then populate a 2D graph with the endpoints that were discovered.

Once the endpoints are discovered they are then connected with lines for relations, displaying which hosts are inside a specific subnet.

1. network_graph.py asks the user two questions:
1.1. How many randomly generated subnets they want.
1.2. What their current IP is.
1.3. I've also included a line that enables users to
	scan inputed ranges (subnet_ranges.csv) in the form
	of X.X.X.X,prefixlength in the csv
1.4. Then subnet_sweeper.py is called
2. Subnet sweeper accepts the current IP and scans the subnet its on starting at .1 to .255
2.1. Subnet sweeper uses the ping command from the ping3 library to ping every single IP and adds active ones to the list
2.2. It also takes the number of RNG subnets and generates them returning a list as well
2.3. Subnet sweeper returns a list of [subnets, gateways] both real and RNG'd depending on user input.
3. Once subnet sweeper returns then graph_create (inside network_graph.py) accepts the list of subnets
	and gateways and begins plotting them associating hosts within a subnet range with their gateway
	before eventually plotting them in the browser. The user will see their detected endpoints connected
	to their local gateway. 
4. Running the program is simply: `cd src && python network_graph.py`
