from flask import Flask, render_template, request
from node_class import node
from json_writer import JsonWriter
import json

app = Flask(__name__)
OUTPUT_PATH = 'test_output.json'

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


if __name__ == '__main__':
    app.run(debug=True)
