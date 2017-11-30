from anryan import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
        user={'nickname':'anryan','nickname2':'syy','nickname3':'milkteawithpearlsin'}
	 posts=[
                {'author':{'authorname':'michael'},
                'body':'it is thursday today'},
               {'author':{'authorname':'Jane'},'body':'it is a cloudy day'},
               {'author':{'authorname':'Maria'},'body':'i do have bad luck today'}
               ]
        return render_template("index.html",title="home-anryan",user=user,posts=posts)
	
