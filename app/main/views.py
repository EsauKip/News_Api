
from .. import app
from flask import render_template
from ..request import get_source,article_source,get_category,get_headlines

#our views
@app.route('/')
def index():
    '''
    Root function returning index/home page with data
    '''
    source= get_source('business')
    headlines = get_headlines()
    return render_template('index.html',sources=source,headlines=headlines)
@app.route('/article/<id>')
def article(id):

    '''
    View article page function that returns the various article details page and its data
    '''
    # title= 'Articles'
    articles = article_source(id)
    return render_template('article.html',articles= articles,id=id )

@app.route('/categories/<cat_name>')
def category(cat_name):
    '''
    function to return the categories.html page and its content
    '''
    category = get_category(cat_name)
    title = f'{cat_name}'
    cat = cat_name

    return render_template('categories.html',title = title,category = category, cat= cat_name)
