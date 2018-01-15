from flask import Blueprint
concinit = Blueprint('concinit', __name__)

#Python modules
import configparser
import os

#Custom modules
#from miscfuncs import *

# load config
dir_path = os.path.dirname(os.path.realpath(__file__))

config = configparser.ConfigParser()
config.read("config.ini")

#IMDB
from imdb import IMDb
imdb_access = IMDb()

#OMDB

#TVDB
#tvdb_api = config['TVDB']['tvdb_api']
#from pytvdbapi import api as tvdb
#tvdb_access = tvdb.TVDB(tvdb_api)

# load DB functions (regardless of connector)
#import importlib
#load_class('db.' + config['db']['connector'])

# only 1 api version
apiversion = 1
apipath = "/api/v1"
apienable = 1 # disable to just run the web interface
#apikey = 	# future development

webversion = 1
webpath = "/web/v1"
webenable = 1 # disable to run your own web frontend
#webauth = [

conclamantesversion = 0.01

# load db initialisation
#from conc-init-db import *
