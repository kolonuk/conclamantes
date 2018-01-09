#DB maintenance

from db.sqlite import * as db
from db.upgrade import *

def cleandb
	db.wipe()
	db.create()

def upgrade
	
	loop until db.version matches conclamantes
	
	if db.version() = 0:			# first version - no db yet
		db.init
	elif db.version() < 0.01		# upgrade to 0.02
		db.upgrade002
	
	

def __main__
