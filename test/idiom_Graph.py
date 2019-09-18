# -*- coding: utf-8 -*-
def get_idiom_data():
    good_data, bad_data = [], []
    idioms = []
    for line in open('idiom', encoding='utf-8').readlines():
        # print(line.split('：'))
        idiom, match = line.split('：')
        idioms.append(idiom)
        good_match, bad_match = match.split('大吉与')

        good_match_dict = {animal: 10 - 2 * v for v, animal in enumerate(good_match.strip().split('、'))}
        bad_match_dict = {animal: 10 - 2 * v for v, animal in enumerate(bad_match.strip().split('、'))}

        # print(idiom, good_match_dict, bad_match_dict)
        for animal, weight in good_match_dict.items():
            good_data.append((idiom, animal, weight))

        for animal, weight in bad_match_dict.items():
            bad_data.append((idiom, animal, weight))

    return idioms, good_data, bad_data

#生成D3js

idioms, gd, bd = get_idiom_data()

for tt in bd:
    print("{source: '%s', target: '%s', type: 'resolved'}," % (tt[0], tt[1]))

# import networkx as nx
# import matplotlib.pyplot as plt
#
# # G = nx.Graph()#创建空的网络图
#
#
# # G = nx.DiGraph()
# # G = nx.MultiGraph()
# G = nx.MultiDiGraph()
# idioms, gd, bd = get_idiom_data()
#
# G.add_nodes_from(idioms)
#
# print(gd)
# # G.add_edges_from([(li[0], li[1], {'weight': li[2]*100}) for li in gd])
# G.add_weighted_edges_from(gd)
# pos = nx.spring_layout(G)  # positions for all nodes
#
# #画图显示
# # nx.draw(G)
# nx.draw_shell(G, node_color = 'b',
#       with_labels = True, font_size =18, node_size =50, font_weight='bold')
# # labels
# nx.draw_networkx_labels(G, pos, font_size=20, font_family='sans-serif')
#
#
# plt.show()


# import matplotlib.pyplot as plt
# import networkx as nx
#
# idioms, gd, bd = get_idiom_data()
# # G = nx.Graph()
#
# G = nx.MultiGraph()
# # G.add_edge('a', 'b', weight=0.6)
# # G.add_edge('a', 'c', weight=0.2)
# # G.add_edge('c', 'd', weight=0.1)
# # G.add_edge('c', 'e', weight=0.7)
# # G.add_edge('c', 'f', weight=0.9)
# # G.add_edge('a', 'd', weight=0.3)
# G.add_weighted_edges_from(gd)
#
# elarge = [(u, v) for (u, v, d) in G.edges(data=True) if d['weight'] > 0.5]
# esmall = [(u, v) for (u, v, d) in G.edges(data=True) if d['weight'] <= 0.5]
#
# pos = nx.spring_layout(G)  # positions for all nodes
#
# # nodes
# nx.draw_networkx_nodes(G, pos, node_size=700)
#
# # edges
# nx.draw_networkx_edges(G, pos, edgelist=elarge, width=6)
# nx.draw_networkx_edges(G, pos, edgelist=esmall,  width=6, alpha=0.5, edge_color='b', style='dashed')
#
# # labels
# nx.draw_networkx_labels(G, pos, font_size=40, font_family='sans-serif')
#
# plt.axis('off')
# plt.show()

