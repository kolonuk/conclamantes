from flask import Blueprint
concapi = Blueprint('concapi', __name__)

import concinit

# shutdown server
def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()
@concapi.route(concinit.apipath + '/shutdown', methods=['GET'])	# GET moethod only
def shutdown():
    if debug:
        shutdown_server()
        return 'Server shutting down...'
    return 'Cheeky!'	# live environment - debug should only be for dev or personal use

