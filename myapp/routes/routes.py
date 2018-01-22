from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy

from myapp.models.Todo import Todo
from myapp.helpers.resource_path import resource_path


class Routes():
    app = False

    def start(self):

        class CustomFlask(Flask):
            jinja_options = Flask.jinja_options.copy()
            jinja_options.update(dict(
                block_start_string='{%',
                block_end_string='%}',
                variable_start_string='((',
                variable_end_string='))',
                comment_start_string='{#',
                comment_end_string='#}',
            ))

        template_folder = resource_path('templates/')

        self.app = CustomFlask(__name__, template_folder=template_folder)
        self.app.config.from_pyfile(resource_path('../app.cfg', 'app.cfg'))

        db = SQLAlchemy(self.app)

        @self.app.route('/')
        def index():
            return render_template('index.html')

        @self.app.route('/example')
        def example():
            message = "Hello Flask!"
            return render_template('example.html', message=message)

        @self.app.route('/more')
        def more():
            return render_template('more.html')

        def initialize_database():
            self.app.logger.info('Database is not created, exec create_all() here.')
            db.create_all()
            data1 = Todo('todo1')
            data2 = Todo('todo2')
            db.session.add(data1)
            db.session.add(data2)
            db.session.commit()

        @self.app.route('/sqlalchemy')
        def sqlalchemy():
            todos = []
            try:
                todos = Todo.query.order_by(Todo.pub_date.desc()).all()
            except:
                initialize_database()
            return render_template('sqlalchemy.html', todos=todos)

        @self.app.route('/sqlalchemy/get', methods=['GET'])
        def sqlalchemy_get():
            todos = Todo.query.order_by(Todo.pub_date.desc()).all()
            return jsonify(todos=[todo.get_dict() for todo in todos])

        @self.app.route('/sqlalchemy/new', methods=['POST'])
        def sqlalchemy_new():
            if request.json:
                db.session.add(Todo(request.json['title']))
                db.session.commit()
            return jsonify(status='ok')  # Oops: always ok...

        @self.app.route('/sqlalchemy/update', methods=['POST'])
        def sqlalchemy_update():
            if request.json:
                todo = Todo.query.get(request.json['id'])
                todo.done = request.json['done']
                todo.title = request.json['title']
                db.session.commit()
            return jsonify(status='ok')  # Oops: always ok...

        @self.app.route('/router')
        def router():
            return render_template('router.html')

        @self.app.route('/sfc')
        def sfc():
            return render_template('sfc.html')

        @self.app.route('/typescript')
        def typescript():
            return render_template('typescript.html')

        @self.app.route('/vuex')
        def vuex():
            return render_template('vuex.html')

        @self.app.route('/v0.10.3')
        def v0_10_3():
            return render_template('vue.js_v0.10.3.html')
