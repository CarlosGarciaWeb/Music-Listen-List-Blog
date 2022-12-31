from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SubmitField
from wtforms.validators import InputRequired

class MusicForm(FlaskForm):
    name = StringField("Song Name", validators=[InputRequired()])
    author = StringField("Author", validators=[InputRequired()])
    album = StringField("Album", validators=[InputRequired()])
    genre = StringField("Genre", validators=[InputRequired()])
    submit = SubmitField("Add Song")