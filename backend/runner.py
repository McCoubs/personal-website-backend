import sys
import os
sys.path.append('../')
import backend as app_root
from backend.app import create_app

APP_ROOT_FOLDER = os.path.abspath(os.path.dirname(app_root.__file__))

# create app using factory
app = create_app()

if __name__ == '__main__':
    app.run()
