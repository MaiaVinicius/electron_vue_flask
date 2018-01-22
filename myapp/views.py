from flask import render_template, jsonify, request

from myapp import api
from myapp.api import db

app = api.app
from .models import Todo


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/example')
def example():
    message = "Hello Flask!"
    return render_template('example.html', message=message)


@app.route('/more')
def more():
    return render_template('more.html')


def initialize_database():
    app.logger.info('Database is not created, exec create_all() here.')
    db.create_all()
    data1 = Todo('todo1')
    data2 = Todo('todo2')
    db.session.add(data1)
    db.session.add(data2)
    db.session.commit()


@app.route('/sqlalchemy')
def sqlalchemy():
    todos = []
    try:
        todos = Todo.query.order_by(Todo.pub_date.desc()).all()
    except:
        initialize_database()
    return render_template('sqlalchemy.html', todos=todos)


@app.route('/sqlalchemy/get', methods=['GET'])
def sqlalchemy_get():
    todos = Todo.query.order_by(Todo.pub_date.desc()).all()
    return jsonify(todos=[todo.get_dict() for todo in todos])


@app.route('/sqlalchemy/new', methods=['POST'])
def sqlalchemy_new():
    if request.json:
        db.session.add(Todo(request.json['title']))
        db.session.commit()
    return jsonify(status='ok')  # Oops: always ok...


@app.route('/sqlalchemy/update', methods=['POST'])
def sqlalchemy_update():
    if request.json:
        todo = Todo.query.get(request.json['id'])
        todo.done = request.json['done']
        todo.title = request.json['title']
        db.session.commit()
    return jsonify(status='ok')  # Oops: always ok...


@app.route('/router')
def router():
    return render_template('router.html')


@app.route('/sfc')
def sfc():
    return render_template('sfc.html')


@app.route('/typescript')
def typescript():
    return render_template('typescript.html')


@app.route('/vuex')
def vuex():
    return render_template('vuex.html')


@app.route('/v0.10.3')
def v0_10_3():
    return render_template('vue.js_v0.10.3.html')

