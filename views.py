from anryan import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
        user={'nickname':'anryan'}
        return render_template("index.html",title="home-anryan",user=user)
	
