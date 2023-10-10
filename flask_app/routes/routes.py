from flask import render_template, request
from flask_app import app
from flask_app.models.models import SingleLinkedList



init_list = SingleLinkedList()
init_list.push("1", "linear-gradient(212.42deg, #f40c12 2%, #f39c12 98%)")
init_list.push("2", "linear-gradient(212.42deg, #f40c12 2%, #f39c12 98%)")
init_list.push("3", "linear-gradient(212.42deg, #f40c12 2%, #f39c12 98%)")


@app.route('/')
def index():
    print("Accessing the index route.")
    return render_template('index.html', list_data=list(init_list), length=init_list.length)

@app.route('/update_nodes', methods=['POST'])
def update_nodes():
    current_method = request.form.get('current_method')
    value = request.form.get('value')
    color = request.form.get('color')
    index_value = request.form.get('index_value')

    # Check if index_value is not empty before converting to int
    if index_value:
        index_value = int(index_value)
    else:
        index_value = None  

    if current_method == 'push':
        init_list.push(value, color)
    elif current_method == 'pop':
        init_list.pop()
    elif current_method == 'shift':
        init_list.shift()
    elif current_method == 'unshift':
        init_list.unshift(value, color)
    elif current_method == 'set':
        init_list.set(value, color, index_value)
    elif current_method == 'insert':
        init_list.insert(value, color, index_value)
    elif current_method == 'remove':
        init_list.remove(index_value)
    elif current_method == 'reverse':
        init_list.reverse()

    return render_template('index.html', list_data=init_list, length=init_list.length)