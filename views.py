from anryan import app

@app.route('/')
@app.route('/index')
def index():
    return '''<html>
	<body style="background-color:Bisque"><h1 style="background-color:Aqua">hi ,anryan,we meet again after almost half a year!</h1>
	</body></html>'''
