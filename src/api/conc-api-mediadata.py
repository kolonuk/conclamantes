# get media data
@app.route(apipath + '/film/')
def film_hint():
    return 'Use: ' + apipath + '/film/[imdbid]'

@app.route(apipath + '/film/<imdbid>')
def show_imdbdata(imdbid):
    imdb_access = IMDb()
    film = imdb_access.get_movie(imdbid) 
    return 'Film title for ' + imdbid + ': ' + film['title']
