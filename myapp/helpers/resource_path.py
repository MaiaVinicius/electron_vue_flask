import sys

import os


def resource_path(relative_path, relative_path_bundled=False):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    bundled = False
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
        bundled = True
    except Exception:
        base_path = os.path.abspath(".")

        # a poor aproach but it is working
        if not 'electron_vue_flask/myapp' in base_path:
            base_path = base_path + '/myapp'

        base_path = base_path + '/client/'

    if bundled and relative_path_bundled:
        relative_path = relative_path_bundled

    return os.path.join(base_path, relative_path)
