from flask import render_template,request,redirect,url_for
from . import main
from flask import render_template,request,redirect,url_for
from ..request import get_source,article_source,get_category,get_headlines
#our view
@main.route('/')
def index():
    """return home page with data
    """
    sources = get_source
    headlines=get_headlines
    return render_template('index.html', sources=sources, headlines=headlines)