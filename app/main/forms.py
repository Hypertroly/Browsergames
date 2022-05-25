#from tkinter.tix import Select
from flask import request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField, FileField
from wtforms.validators import ValidationError, DataRequired, Length
from flask_babel import _, lazy_gettext as _l
from app.models import User


class EditProfileForm(FlaskForm):
    username = StringField(_l('Username'), validators=[DataRequired()])
    about_me = TextAreaField(_l('About me'),
                             validators=[Length(min=0, max=140)])
    full_name = StringField(_l('Full name'), validators=[DataRequired()])
    birthday = StringField(_l('Birthday'), validators=[DataRequired()])
    country = StringField(_l('Country'), validators=[DataRequired()])
    state = StringField(_l('State'), validators=[DataRequired()])
    submit = SubmitField(_l('Submit'))

    def __init__(self, original_username, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.original_username = original_username

    def validate_username(self, username):
        if username.data != self.original_username:
            user = User.query.filter_by(username=self.username.data).first()
            if user is not None:
                raise ValidationError(_('Please use a different username.'))


class EmptyForm(FlaskForm):
    submit = SubmitField('Submit')


class PostForm(FlaskForm):
    post = TextAreaField(_l('Say something'), validators=[DataRequired()])
    submit = SubmitField(_l('Submit'))
    
class GameForm(FlaskForm):
    name = TextAreaField(('Name'), validators=[DataRequired()])
    url = TextAreaField(('URL'), validators=[DataRequired()])
    urlvideo = TextAreaField(('Video URL'))
    description = TextAreaField(('Description'))
    name_category = TextAreaField(('Category'), validators=[DataRequired()])
    photo = FileField(('Photo'))
    submit = SubmitField(('Submit'))
    
class ReviewForm(FlaskForm):
    review = TextAreaField(_l('Review the game'), validators=[DataRequired()])
    stars = SelectField(_l('Stars'), choices=[(1),(2),(3),(4),(5)], validators=[DataRequired()])
    submit = SubmitField(_l('Submit'))

class CategoryForm(FlaskForm):
    name = TextAreaField(('Name'), validators=[DataRequired()])
    submit = SubmitField(('Submit'))

class SearchForm(FlaskForm):
    q = StringField(_l('Search'), validators=[DataRequired()])

    def __init__(self, *args, **kwargs):
        if 'formdata' not in kwargs:
            kwargs['formdata'] = request.args
        if 'meta' not in kwargs:
            kwargs['meta'] = {'csrf': False}
        super(SearchForm, self).__init__(*args, **kwargs)
