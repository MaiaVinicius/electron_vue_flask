import imp
import importlib

import os
from flask import Flask
import sys

cwd = os.getcwd()
sys.path.append(cwd)

if __name__ == '__main__':
    # routes_path = resource_path('routes/routes.py')
    # print(routes_path)
    # application = imp.load_source('app', routes_path)
    from myapp.routes.routes import Routes

    application = Routes()
    application.start()

    port = application.app.config['PORT']
    ip = application.app.config['IP']
    app_name = application.app.config['APP_NAME']
    host_name = application.app.config['HOST_NAME']

    server = Flask(__name__)
    server.wsgi_app = application.app

    server.run(host=ip, port=port)
