# Network Mapper
This repo holds a python project that maps out endpoints in a network plotting them /somehow/

## Network Topology Visualizer Tool
The point of this tool is to scan a subnet(s) then populate a 2D graph with the endpoints that were discovered.

Once the endpoints are discovered they are then connected with lines for relations (sending traffic)

1. Scan the inputed ranges (subnet_ranges.csv)
2. Populate a 2D graph with the discovered endpoints
3. Relate the discovered endpoints
