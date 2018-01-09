from flask import Flask
from flask import request

app = Flask(__name__)

debugmode = False
try:
    import uwsgi
except ImportError:
    debugmode = True

from api import *
from web import *

if __name__ == "__main__":
	# enable WINGDB editor debugging
    import os
    if 'WINGDB_ACTIVE' in os.environ:
        app.debug = False
    app.run()