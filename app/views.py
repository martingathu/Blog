from flask import render_template
import app
from .request import get_quote

@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    # Getting a Random quote
    random_quote = get_quote('random')
    print(random_quote)
    return render_template('index.html',random = random_quote)