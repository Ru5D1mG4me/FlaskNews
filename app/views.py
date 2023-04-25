from flask import render_template, redirect, url_for

from . import app, db
from .forms import NewsForm
from .models import Category, News


@app.route('/')
def index():
    news = News.query.all()
    categories = Category.query.all()
    return render_template('index.html',
                           news=news, categories=categories)


@app.route('/news_detail/<int:id>')
def news_detail(id):
    news = News.query.get(id)
    categories = Category.query.all()
    return render_template('news_detail.html',
                           news=news, categories=categories)


@app.route('/category/<int:id>')
def news_in_category(id):
    news = News.query.filter(News.category_id == id).all()
    category_name = Category.query.get(id).title
    categories = Category.query.all()
    return render_template('category.html',
                           news=news, category_name=category_name, categories=categories)


@app.route('/add_news', methods=['GET', 'POST'])
def add_news():
    categories = Category.query.all()
    form = NewsForm()
    if form.validate_on_submit():
        news = News(
            title=form.title.data,
            text=form.text.data,
            category_id=form.category.data
        )
        db.session.add(news)
        db.session.commit()
        return redirect(url_for('news_detail', id=news.id))
    return render_template('add_news.html',
                           form=form, categories=categories)