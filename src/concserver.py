from flask import Flask
#from flask import request

app = Flask(__name__)

from concinit import *
app.register_blueprint(concinit)

from api.concapi import *
from web.concweb import *
app.register_blueprint(concapi)
app.register_blueprint(concweb)

debugmode = False
try:
    import uwsgi
except ImportError:
    debugmode = True


if __name__ == "__main__":
	# enable WINGDB editor debugging
    import os
    if 'WINGDB_ACTIVE' in os.environ:
        app.debug = False
    app.run()