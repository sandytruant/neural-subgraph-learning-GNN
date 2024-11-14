import networkx as nx
import pickle

def genQueryGraph():
    G = nx.Graph()
    G.add_node(1, type="add")
    G.add_node(2, type="sub")
    G.add_edge(1, 2)
    return G

def genTargetGraph():
    G = nx.Graph()
    G.add_node(1, type="add")
    G.add_node(2, type="sub")
    G.add_node(3, type="add")
    G.add_edge(1, 2)
    G.add_edge(1, 3)
    G.add_edge(2, 3)
    return G

def main():
    query = genQueryGraph()
    target = genTargetGraph()
    with open("query.pkl", "wb") as f:
        pickle.dump(query, f)
    with open("target.pkl", "wb") as f:
        pickle.dump(target, f)

if __name__ == "__main__":
    main()
