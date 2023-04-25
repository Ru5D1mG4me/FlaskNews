from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length, Optional

from .models import Category


class NewsForm(FlaskForm):
    title = StringField('News title', validators=[DataRequired(message='Field cannot be empty'),
                                                  Length(max=256)])
    text = TextAreaField('News text', validators=[DataRequired(message='Field cannot be empty')])
    category = SelectField('Category', choices=[(category.id, category.title) for category in Category.query.all()], validators=[Optional()])
    submit = SubmitField('Add news')