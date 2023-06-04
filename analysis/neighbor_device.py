import re
import ipaddress
import netmiko
import time
import threading
from PIL import Image
import networkx as nx
import matplotlib.pyplot as plt
from www.codes.my_projects.db_functions.db_rd_hostname_nei_dev import db_rd_host
from www.codes.my_projects.db_functions.db_rd_hostname_nei_dev import db_rd_nei

threads = []

def draw_nei():
    ip_host = db_rd_host()[0]
    hostname_h = db_rd_host()[1]
    domain_name = db_rd_host()[2]
    ip_nei = db_rd_nei()[0]
    hostname_n = db_rd_nei()[2]
    interface_n = db_rd_nei()[1]
    len_ip_nei = len(ip_nei)

    g_edges = []
    g_nodes = []
    for h_h in hostname_h:
        if (str(h_h) == 'None') or (str(h_h) == 'none') or (str(h_h) == '') or (str(h_h) == ' '):
            continue
        else:
            g_nodes.append(str(h_h))

    for num_i in range(0,len_ip_nei):
        ip = ip_nei[num_i]
        in_1 = ip_host.index(ip)
        h_local = hostname_h[in_1]
        h_nei = hostname_n[num_i]
        h_nei = h_nei.replace(".mon.com", "")
        l_n = interface_n[num_i]
        g_edges.append((h_nei, h_local))

    g = nx.MultiGraph(g_edges)
    g.edges(data=True)
    nx.degree(g)
    pos = nx.random_layout(g)
    #nx.draw(g, node_size=600, arrows=True, edge_color='r', node_color='g', with_labels=True, connectionstyle='arc3, rad = 0.1')
    #nx.draw_networkx_nodes(g, pos, node_color='r', node_size=500, alpha=1, label=1)
    #nx.draw_networkx_edges(g, pos, node_size=500, alpha = 1, edge_color='r', arrows=True)
    #nx.draw_networkx_edge_labels(g, pos, edge_labels=nx.get_edge_attributes(g, 'label'))
    nx.draw_networkx(g, pos,node_size=400, arrows=True, edge_color='r', node_color='g', with_labels=True, connectionstyle='arc3, rad = 0.1')

    ax = plt.gca()
    for e in g.edges:
        ax.annotate("", xy=pos[e[0]], xycoords='data', xytext=pos[e[1]], textcoords='data', arrowprops=dict(arrowstyle="->", color="0.5", shrinkA=5, shrinkB=5, patchA=None, patchB=None, connectionstyle="arc3,rad=0.1",),)
    plt.axis('off')
    plt.show()
    plt.show(block=False)
    plt.savefig("/var/www/grh.png", format="PNG")
    #im = Image.open('/var/www/grh.png')