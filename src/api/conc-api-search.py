@app.route(apipath + '/search/')
def v1_search():
    return 'Use: ' + apipath + '/search/[film|series]'

	
#searching films
@app.route(apipath + '/search/film/')
def v1_search_film():
    return 'Use: ' + apipath + '/search/film/[title|character|person|IMDBID]/string'

@app.route(apipath + '/search/film/title/<searchstring>')
def v1_search_film_title(searchstring):
    s_result = imdb_access.search_movie(searchstring)
    responsedata = ""
    for item in s_result:
        responsedata = responsedata + item['long imdb canonical title'] + ':' + item.movieID + '\n'
    return responsedata

@app.route(apipath + '/search/film/character/<searchstring>')
def searchcharacter(searchstring):
    s_result = imdb_access.search_character(searchstring)
    responsedata = ""
    for item in s_result:
        responsedata = responsedata + item['name'] + ':' + item.characterID + '\n'
    return responsedata

@app.route(apipath + '/search/film/person/<searchstring>')
def searchperson(searchstring):
    s_result = imdb_access.search_person(searchstring)
    responsedata = ""
    for item in s_result:
        responsedata = responsedata + item['name'] + ':' + item.personID + '\n'
    return responsedata


# TV searching
@app.route(apipath + '/search/series/')
def v1_search_film():
    return 'Use: ' + apipath + '/search/series/[title|character|person|TVDBID|episodeno|episodename]/string'

@app.route(apipath + '/search/series/title/<searchstring>')
def searchseries(searchstring):
    s_result = tvdb_access.search(searchstring,'en')
    responsedata = ""
    for item in s_result:
        responsedata = responsedata + item.SeriesName + ':' + str(item.id) + '\n'
    return responsedata