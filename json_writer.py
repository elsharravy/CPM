import json

class JsonWriter:
    def __init__(self, output_file):
        self.output_file = output_file

    def write_nodes(self, nodes):
        data = [node.to_dict() for node in nodes]
        with open(self.output_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)
