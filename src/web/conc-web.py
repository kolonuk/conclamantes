
# Root
@app.route('/')
def root():
    #default root
    return 'Thanks for using conclamantes!'
	#forward to web/v1

@app.route('/web/v1/')
def rootweb():
    #default root
    return 'Thanks for using conclamantes!'
	
