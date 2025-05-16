import json
import node_class
import strings

class Json_reader:
    @staticmethod
    def load(filePath):
        try:
            with open(filePath, "r") as file:
                data = json.load(file)

                nodes = {entry["name"]: node_class.node(entry[strings.JSON["duration_key_name"]], entry[strings.JSON["name_key_name"]]) for entry in data}

                for entry in data:
                    node = nodes[entry[strings.JSON["name_key_name"]]]

                    if entry[strings.JSON["precedent_key_name"]]:  
                        predecessors = entry[strings.JSON["precedent_key_name"]]

                        for pred_name in predecessors:
                            if pred_name in nodes:  
                                pred_node = nodes[pred_name]
                                node.previous.append(pred_node) 
                                pred_node.next.append(node) 
                            else:
                                print(f"Warning: Predecessor '{pred_name}' not found for node '{node.name}'")

                for node in nodes.values():
                    print(f"{node.name}: Previous -> {[p.name for p in node.previous]}, Next -> {[n.name for n in node.next]}")

                return list(nodes.values())

                
        
        except FileNotFoundError:
            print(f"Error: File '{filePath}' not found.")