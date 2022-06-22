import networkx as nx

N = int(input())
G = nx.DiGraph()
G.add_node("s")
G.add_node("t")
AB = []
for i in range(N):
    AB.append(tuple(map(int, input().split())))
    G.add_node(f"r{i}")
    G.add_edge("s", f"r{i}", capacity=1)
CD = []
for i in range(N):
    G.add_node(f"b{i}")
    G.add_edge(f"b{i}", "t", capacity=1)
    CD.append(tuple(map(int, input().split())))


for i, (a, b) in enumerate(AB):
    for j, (c, d) in enumerate(CD):
        if a < c and b < d:
            G.add_edge(f"r{i}", f"b{j}", capacity=1)

result = nx.maximum_flow_value(G, "s", "t")

print(result)

"""
マッチングの問題っぽいがその手の知識はない

青の内側に赤があるイメージ


N<=100で小さい
N**4

貪欲になるべく大きい赤を青に埋めていく、的な？
類題見た気がするなあ

AC

解説後
やっぱり2部最大マッチングだし覚え解くべき問題

"""
