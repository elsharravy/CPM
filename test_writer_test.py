from node_class import node
from json_writer import JsonWriter

# Przykładowe węzły (nodes)
node1 = node(5, "Start", pr=[], es=0, ef=5, ls=0, r=0, lf=5, ne=["TaskA"])
node2 = node(3, "TaskA", pr=["Start"], es=5, ef=8, ls=5, r=0, lf=8, ne=["End"])
node3 = node(2, "End", pr=["TaskA"], es=8, ef=10, ls=8, r=0, lf=10, ne=[])

# Lista węzłów
nodes = [node1, node2, node3]

# Inicjalizacja writer-a
writer = JsonWriter("test_output.json")

# Zapis danych do pliku JSON
writer.write_nodes(nodes)

print("Zapisano dane do pliku test_output.json")
