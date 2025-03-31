import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

G.add_node('Storage 1')
G.add_node('Storage 2')
G.add_node('Storage 3')
G.add_node('Shop 1')
G.add_node('Shop 2')

G.add_edge('Storage 1', 'Shop 1', weight=10)
G.add_edge('Storage 1', 'Shop 2', weight=26)
G.add_edge('Storage 2', 'Shop 2', weight=29)
G.add_edge('Storage 3', 'Shop 2', weight=20)
G.add_edge('Storage 3', 'Shop 1', weight=17)
G.add_edge('Storage 2', 'Storage 1', weight=36)
G.add_edge('Storage 3', 'Storage 1', weight=13)

shortest_path = nx.shortest_path(G, source='Storage 1', target="Shop 2", weight="weight")
path_len = nx.shortest_path_length(G, source='Storage 1', target="Shop 2", weight="weight")

print(f'Shortest path from storage 1 to shop: {shortest_path}')
print(f'Count of navigate: {path_len} units')

pos = nx.spring_layout(G)
labels = nx.get_edge_attributes(G, 'weight')

plt.figure(figsize=(8, 6))
nx.draw(G, pos, with_labels=True, node_size=3000, node_color="pink", font_size=10, font_weight="bold")
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.title("Граф доставки товаров")
plt.show()