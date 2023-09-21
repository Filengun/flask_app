import os

from flask import Flask

# CONFIG
DATABASE = '/tmp/flsite.db'
DEBUG = True
SECRET_KEY = "asdgegsdf8a7er03rhosfhaowfyq93r3oiofh"

# APP
app = Flask(__name__)
app.config["SECRET_KEY"] = SECRET_KEY
app.config.from_object(__name__)
app.config.update(dict(DATABASE=os.path.join(app.root_path, 'app.db')))
