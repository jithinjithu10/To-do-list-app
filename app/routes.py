from flask import render_template, request, redirect, url_for, flash
from . import create_app, db
from .models import Todo

app = create_app()

@app.route('/')
def index():
    todos = Todo.query.all()
    return render_template('index.html', todos=todos)

@app.route('/add', methods=['POST'])
def add_todo():
    task = request.form.get('task')
    if task:
        new_todo = Todo(task=task)
        db.session.add(new_todo)
        db.session.commit()
        flash('Task added successfully!', 'success')
    else:
        flash('Task cannot be empty!', 'error')
    return redirect(url_for('index'))

@app.route('/delete/<int:id>', methods=['POST'])
def delete_todo(id):
    todo = Todo.query.get(id)
    if todo:
        db.session.delete(todo)
        db.session.commit()
        flash('Task deleted successfully!', 'success')
    return redirect(url_for('index'))

