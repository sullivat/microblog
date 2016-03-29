from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Timothy'}  # fake user
    posts = [  # fake array of posts
    	{
    		'author': {'nickname': 'John'},
    		'body': 'Beautiful day in Denver'
    	},
        {
            'author': {'nickname': 'Jess'},
            'body': 'I lost my iPhone today! :( :( '
        },
        {
            'author': {'nickname': 'Fred'},
            'body': 'Anyone free to grab a coffee?'
        },
    	{
    		'author': {'nickname': 'Susan'},
    		'body': 'The Avengers movie was so cool!'
    	}
    ]
    return render_template('index.html',
                           title='Home',
                           user=user,
                           posts= posts)
