from anryan import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
        user={'nickname':'anryan','nickname2':'syy','nickname3':'milkteawithpearlsin'}
        return render_template("index.html",title="home-anryan",user=user)
	
