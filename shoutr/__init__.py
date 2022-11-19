import os

from flask import Flask
from .env_vars import SECRET_KEY


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY=SECRET_KEY,
        DATABASE=os.path.join(app.instance_path, 'shoutr.sqlite'),
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from . import db
    db.init_app(app)
    
    from . import auth
    app.register_blueprint(auth.bp)
    
    from . import shout
    app.register_blueprint(shout.bp)
    app.add_url_rule('/', endpoint='index')
    
    from . import profile
    app.register_blueprint(profile.bp)
    
    return app