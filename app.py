from flask import Flask, render_template, request, jsonify, redirect, url_for
import json
import os

app = Flask(__name__)

# In-memory storage for todos (in production, use a database)
todos = []
todo_id_counter = 1

# Load todos from file if exists
TODO_FILE = 'todos.json'

def load_todos():
    global todos, todo_id_counter
    if os.path.exists(TODO_FILE):
        try:
            with open(TODO_FILE, 'r') as f:
                data = json.load(f)
                todos = data.get('todos', [])
                todo_id_counter = data.get('counter', 1)
        except:
            todos = []
            todo_id_counter = 1

def save_todos():
    with open(TODO_FILE, 'w') as f:
        json.dump({'todos': todos, 'counter': todo_id_counter}, f)

# Load todos on startup
load_todos()

@app.route('/')
def index():
    """Render the main page with all todos"""
    return render_template('index.html', todos=todos)

@app.route('/api/todos', methods=['GET'])
def get_todos():
    """Get all todos as JSON"""
    return jsonify(todos)

@app.route('/api/todos', methods=['POST'])
def add_todo():
    """Add a new todo"""
    global todo_id_counter
    data = request.get_json()
    
    if not data or 'title' not in data:
        return jsonify({'error': 'Title is required'}), 400
    
    new_todo = {
        'id': todo_id_counter,
        'title': data['title'],
        'completed': False
    }
    
    todos.append(new_todo)
    todo_id_counter += 1
    save_todos()
    
    return jsonify(new_todo), 201

@app.route('/api/todos/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    """Update a todo (mark as completed/incomplete or change title)"""
    data = request.get_json()
    
    for todo in todos:
        if todo['id'] == todo_id:
            if 'completed' in data:
                todo['completed'] = data['completed']
            if 'title' in data:
                todo['title'] = data['title']
            save_todos()
            return jsonify(todo)
    
    return jsonify({'error': 'Todo not found'}), 404

@app.route('/api/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    """Delete a todo"""
    global todos
    
    for i, todo in enumerate(todos):
        if todo['id'] == todo_id:
            deleted_todo = todos.pop(i)
            save_todos()
            return jsonify(deleted_todo)
    
    return jsonify({'error': 'Todo not found'}), 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)