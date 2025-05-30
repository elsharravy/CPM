from flask import Flask, render_template, request, jsonify
from node_class import node
from json_writer import JsonWriter
from json_reader import Json_reader
from Compiler_class import Compiler

import json

app = Flask(__name__)
OUTPUT_PATH = 'test_output.json'
INPUT_PATH = OUTPUT_PATH

def generateLinks(nodes):
    links = []
    for i in range(len(nodes)):
       prev = nodes[i].get_pr()
       for j in range(len(prev)):
        prevNode = nodes[ prev[j] ]
        isCritical = False
        if prevNode.get_r()==0 and nodes[i].get_r() == 0:
            isCritical = True
        entry = dict( source= nodes[ prev[j] ].get_n(), target=nodes[i].get_n(), critical=isCritical )
        links.append( entry )
    return links

def clean_item(item):
    return {
        'n': item.get('name'),              # rename 'node_id' -> 'id'
        't': item.get('duration'),   # rename 'content' -> 'value', default to 'empty'
        'es': item.get('early_start'), 
        'ef': item.get('early_finish'),
        'ls': item.get('late_start'),
        'lf': item.get('late_finish'),
        'r': item.get('reserve'), 
        'pr': item.get('previous'),
        'ne': item.get('next')
    }

def load_existing_nodes():
    try:
        with open(OUTPUT_PATH, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return [node(**clean_item(item)) for item in data]
    except FileNotFoundError:
        return []

@app.route('/', methods=['GET'])
def index():
    nodes = load_existing_nodes()
    return render_template('json_writer_site.html', nodes=nodes)

@app.route('/add', methods=['POST'])
def add_node():
    def parse_list(field):
        val = request.form.get(field, '')
        return [v.strip() for v in val.split(',')] if val else []

    def parse_int(field):
        val = request.form.get(field)
        return int(val) if val else None

    n = request.form['n']
    t = parse_int('t')
    pr = parse_list('pr')
    es = parse_int('es')
    ef = parse_int('ef')
    ls = parse_int('ls')
    r = parse_int('r')
    lf = parse_int('lf')
    ne = parse_list('ne')

    new_node = node(t=t, n=n, pr=pr, es=es, ef=ef, ls=ls, r=r, lf=lf, ne=ne)

    nodes = load_existing_nodes()
    nodes.append(new_node)

    writer = JsonWriter(OUTPUT_PATH)
    writer.write_nodes(nodes)

    return render_template('json_writer_site.html', message=f'Node "{n}" added successfully!', nodes=nodes)

@app.route('/clean', methods=['GET'])
def clean():
    with open("test_output.json", "w") as file:
        file.write("[\n]")
    return render_template('json_writer_site.html', message=f'Nodes deleted')

@app.route("/gen")
def loadNodesFromJSONAndSendToWebsite():
    nodes = Json_reader.load( INPUT_PATH )
    for i in range(len(nodes)):
       prev = nodes[i].get_pr()
       for j in range(len(prev)):
          print(f"Prev[j] jest rowne: {prev[j].get_n()}")
          for k in range(len(nodes)):
             if prev[j].get_n() == nodes[k].get_n():
                prev[j]=k
                print(f"K jest rowne: {k}")
                break
    print("Compiler input-------------")
    for node in nodes:
        print(node)
    compiled_nodes = Compiler.Compile(nodes)
    print("Compiler output-------------")
    for node in compiled_nodes:
        print(node)
    '''
    links = [
        { "source": 'a', "target": 'b' },
        { "source": 'a', "target": 'c' },
        { "source": 'b', "target": 'd' },
        { "source": 'c', "target": 'd' }
    ];
    '''
    links = generateLinks(compiled_nodes)

    arrayOfGraphData = []
    arrayOfNodesData = []

    for i in range(len(compiled_nodes)):
        obj = dict( id=compiled_nodes[i].get_n(), left= compiled_nodes[i].get_es(), right=compiled_nodes[i].get_ef(), bottom=compiled_nodes[i].get_r(), top=compiled_nodes[i].get_n()  )
        arrayOfGraphData.append(obj)
    for i in range(len(compiled_nodes)):
        obj = dict( name=compiled_nodes[i].get_n(), early_start= compiled_nodes[i].get_es(), early_finish=compiled_nodes[i].get_ef(), reserve=compiled_nodes[i].get_r(), duration=compiled_nodes[i].get_t(), previous=compiled_nodes[i].get_pr(), next=compiled_nodes[i].get_ne(), late_start=compiled_nodes[i].get_ls(), late_finish=compiled_nodes[i].get_lf()  )
        arrayOfNodesData.append(obj)
    print(arrayOfGraphData)
    return jsonify({"nodes": arrayOfGraphData, "links": links, "compiled" : arrayOfNodesData})

if __name__ == '__main__':
    app.run(debug=True)
