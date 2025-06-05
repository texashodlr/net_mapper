# Network Mapper
This repo is a python project that helps a user graphically map out endpoints in a network and produces the resulting map in a browser.

## Network Topology Visualizer Tool
The point of this tool is to scan a collection of subnet(s) then populate a 2D graph with the endpoints that were discovered.

Once the endpoints are discovered they are then connected with lines for relations (sending traffic)

1. Scan the inputed ranges (subnet_ranges.csv)
2. Populate a 2D graph with the discovered endpoints
3. Relate the discovered endpoints
