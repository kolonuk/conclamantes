
# shutdown server
def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()
@app.route(apipath + '/shutdown', methods=['GET'])
def shutdown():
    if app.debug:
        shutdown_server()
        return 'Server shutting down...'
    return 'Cheeky!'	# live environment - debug should only be for dev or personal use

	
