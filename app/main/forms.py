from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, SelectField, BooleanField
from wtforms.validators import InputRequired, Length, EqualTo, ValidationError, Email, Required
from ..models import User
from wtforms import ValidationError
from flask_wtf.file import FileField, FileAllowed

def invalid_credentials(form, field):
    """Username and password checker"""
    username_entered =form.username.data
    password_entered = field.data

    user_object = User.query.filter_by(username=username_entered).first()
    if user_object is None or not user_object.verify_password(password_entered):
        raise ValidationError("Username or Password is incorrect")

    
class RegistrationForm(FlaskForm):
    """Restration form"""
    email = StringField('Your Email Address',validators=[InputRequired(),Email()])
    username = StringField('username', validators=[InputRequired(message='Username required'), Length(min=4, max=25, message='Username must be between 4 and 25 characters')])
    password = PasswordField('password', validators=[InputRequired(message='Password required'), Length(min=4, max=25, message='Password must be between 4 and 25 characters')])
    confirm_pswd = PasswordField('confirm Password', validators=[InputRequired(message='Password required'), EqualTo('password', message="Passwords must match")])
    remember = BooleanField('Subscribe')
    submit_button = SubmitField('Sign up')

    def validate_email(self,data_field):
            if User.query.filter_by(email =data_field.data).first():
                raise ValidationError('There is an account with that email')

    def validate_username(self,data_field):
        if User.query.filter_by(username = data_field.data).first():
            raise ValidationError('That username is taken')


class LoginForm(FlaskForm):
    """Login form"""
    username = StringField('username', validators=[InputRequired(message="Username required")])
    password = PasswordField('password', validators=[InputRequired(message="Password required"), invalid_credentials])
    remember = BooleanField('Remember Me')
    submit_button = SubmitField('Sign In')

class PostForm(FlaskForm):
    topic = StringField('Topic', validators=[InputRequired(message="Topic required")])
    category = SelectField('Category', choices=[('product', 'product'), ('interview', 'interview'), ('promotion', 'promotion')], validators=[InputRequired(message="Category required")])
    description = StringField('Description', validators=[InputRequired(message="Description required")])
    submit= SubmitField('Post')


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    email = StringField('Your Email Address',validators=[InputRequired(),Email()])
    username = StringField('username', validators=[InputRequired(message='Username required'), Length(min=4, max=25, message='Username must be between 4 and 25 characters')])
    profile_pic_path = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Submit')


class CommentsForm(FlaskForm):
    comment = TextAreaField('Type Comment.',validators = [Required()])
    submit = SubmitField('Submit')