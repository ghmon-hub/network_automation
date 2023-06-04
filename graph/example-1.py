import networkx as nx
import matplotlib.pyplot as plt

g = nx.Graph()
g.add_nodes_from([1,2,3,4,5,6])
g.add_edge(1, 2, label='a')
g.add_edge(1, 3, label='a')
g.add_edge(2, 4, label='a')
g.add_edge(1, 6, label='a')
g.add_edge(3, 5, label='a')
g.add_edge(2, 1, label='a')
g.edges(data=True)
pos = nx.spring_layout(g)
#nx.draw(g,with_labels=True)
nx.draw_networkx(g, pos, node_size=600, edge_size=3000, edge_color='r', node_color='g')
nx.draw_networkx_edge_labels(g,pos,edge_labels=nx.get_edge_attributes(g,'label'))
plt.show()
