from flask import Blueprint
concweb = Blueprint('concweb', __name__)

# Root
@concweb.route('/')
def root():
    #default root
    return 'Thanks for using conclamantes!'
    #forward to web/v1

@concweb.route('/web/v1/')
def rootweb():
    #default root
    return 'Thanks for using conclamantes!'
	
