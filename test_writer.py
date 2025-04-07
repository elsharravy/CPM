from functions import create_node
from json_writer import JsonWriter

# Tworzymy 2 węzły "na sucho"
node1 = create_node("A", 4, [])
node2 = create_node("B", 3, ["A"])

# Zapis do JSON
writer = JsonWriter("dry_input.json")
writer.write_nodes([node1, node2])
