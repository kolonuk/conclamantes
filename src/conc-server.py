from flask import Flask
from flask import request

import configparser

from imdb import IMDb
from pytvdbapi import api as tvdb

import os

dir_path = os.path.dirname(os.path.realpath(__file__))

config = configparser.ConfigParser()
config.read("src/config.ini")

tvdb_apikey = config['TVDB']['tvdb_api']

imdb_access = IMDb()
tvdb_access = tvdb.TVDB(tvdb_apikey)

app = Flask(__name__)

debugmode = False
try:
    import uwsgi
except ImportError:
    debugmode = True


# shutdown server
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

@app.route('/')
def root():
    #default root
    return 'Thanks for using conclamantes!'

# search for titles
@app.route('/film/')
def film_hint():
    return 'Use: /film/[imdbid]'

@app.route('/film/<imdbid>')
def show_imdbdata(imdbid):
    imdb_access = IMDb()
    film = imdb_access.get_movie(imdbid) 
    return 'Film title for ' + imdbid + ': ' + film['title']

@app.route('/search/')
def search_hint():
    return 'Use: /search/[film|character|person|series|seriesep]/[string]'

@app.route('/search/film/<searchstring>')
def searchfilm(searchstring):
    s_result = imdb_access.search_movie(searchstring)
    responsedata = ""
    for item in s_result:
        responsedata = responsedata + item['long imdb canonical title'] + ':' + item.movieID + '\n'
    return responsedata

@app.route('/search/character/<searchstring>')
def searchcharacter(searchstring):
    s_result = imdb_access.search_character(searchstring)
    responsedata = ""
    for item in s_result:
        responsedata = responsedata + item['name'] + ':' + item.characterID + '\n'
    return responsedata

@app.route('/search/person/<searchstring>')
def searchperson(searchstring):
    s_result = imdb_access.search_person(searchstring)
    responsedata = ""
    for item in s_result:
        responsedata = responsedata + item['name'] + ':' + item.personID + '\n'
    return responsedata

@app.route('/search/series/<searchstring>')
def searchseries(searchstring):
    s_result = tvdb_access.search(searchstring,'en')
    responsedata = ""
    for item in s_result:
        responsedata = responsedata + item.SeriesName + ':' + item.id + '\n'
    return responsedata



