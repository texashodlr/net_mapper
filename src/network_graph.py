import networkx as nx
import plotly.graph_objects as go
from subnet_sweeper import subnet_sweep

node_list = subnet_sweep('subnet_range.csv')
gateway = '192.168.1.1'

# Creates a graph using NetworkX
G = nx.Graph()
# G.add_edge("a","b",weight=0.25)
for node in node_list:
    G.add_edge(node, gateway, weight = 0.25)

# Generates positions for the nodes
pos = nx.spring_layout(G)

# Create a plotly figure
fig = go.Figure()

# Add edges to the figure
for u, v, data in G.edges(data=True):
    x0, y0 = pos[u]
    x1, y1 = pos[v]
    fig.add_trace(go.Scatter(
        x=[x0, x1], 
        y=[y0, y1], 
        mode='lines', 
        line = dict(width=data['weight'] * 5, 
            color='gray'),
        hoverinfo='none'
    ))

# Labeling our detected nodes
node_x = []
node_y = []
node_labels = []

# Add nodes to the figure
for node in G.nodes():
    x, y = pos[node]
    node_x.append(x)
    node_y.append(y)
    node_labels.append(node)

fig.add_trace(go.Scatter(
    x=node_x, 
    y=node_y, 
    mode='markers+text', 
    marker=dict(size=10,
        color='blue',
        line=dict(width=2, color='black')
    ),
    text=node_labels,
    textposition='top center',
    textfont=dict(
        size=12,
        color='black'
    ),
    hoverinfo='text',
    hovertext=node_labels
))

fig.update_layout(
        title = 'Network Topology Visualizer',
        title_x = 0.5,
        showlegend = False,
        hovermode = 'closest',
        plot_bgcolor='white',
        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False)
        )

# Show the figure
fig.show()

