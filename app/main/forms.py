from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import InputRequired


class CommentForm(FlaskForm):
    comment = TextAreaField('Post a Comment')
    submit = SubmitField('Submit')
