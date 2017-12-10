from flask import Flask
from flask import request

app = Flask(__name__)

debugmode = False
try:
    import uwsgi
except ImportError:
    debugmode = True

@app.route('/')
def root():
    #default root
    return 'Thanks for using conclamantes!'


@app.route('/film/')
def film_hint():
    return 'Use: /film/[imdbid]'

@app.route('/film/<imdbid>')
def show_imdbdata(imdbid):
    # show the user profile for that user
    from imdb import IMDb
        
    imdb_access = IMDb()
    film = imdb_access.get_movie(imdbid) 
    
    return 'Film title for ' + imdbid + ': ' + film['title']



@app.route('/search/<searchstring>')
def search(searchstring):
    
    # show the user profile for that user
    from imdb import IMDb
    import json
    
    imdb_access = IMDb()
    s_result = imdb_access.search_movie(searchstring)
    
    responsedata = ""
    for item in s_result:
        responsedata = responsedata + item['long imdb canonical title'] + ':' + item.movieID + '\n'
    return responsedata



# shutdown server remotely
def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()

@app.route('/shutdown', methods=['GET'])
def shutdown():
    if app.debug:
        shutdown_server()
        return 'Server shutting down...'
    
    return 'Cheeky!'
    
    
