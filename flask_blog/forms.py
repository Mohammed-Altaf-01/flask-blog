# flask-wtf for creating login forms 
# pip install wtforms[email] for email validation seprately 
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_blog.models import User

# python classes are automatically converted into html forms 

class RegistrationForm(FlaskForm):
    username = StringField("Username",
                           validators=[DataRequired(),Length(min=2,max=30)])
    
    email = StringField('Email Id', 
                        validators=[DataRequired(),Email()])
    
    password = PasswordField('Password', 
                             validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', 
                                     validators=[DataRequired(), EqualTo('password')])
    
    submit = SubmitField('Sign Up')
    
    def validate_username(self, username):
        user = User.query.filter_by(username = username.data).first()
        if user:
            raise ValidationError('That Username is Already Taken, Please Choose Another One!')
    
    def validate_email(self, email):
        user = User.query.filter_by(email = email.data).first()
        if user:
            raise ValidationError("That Email Already Exists, Please Login")
class LoginForm(FlaskForm):
    
    email = StringField('Email Id', 
                        validators=[DataRequired(),Email()])
    
    password = PasswordField('Password', 
                             validators=[DataRequired()])
    
    remember = BooleanField('Remember Me')
    
    submit = SubmitField('Login')



class UpdateForm(FlaskForm):
    username = StringField("Username",
                           validators=[DataRequired(),Length(min=2,max=30)])
    
    email = StringField('Email Id', 
                        validators=[DataRequired(),Email()])
    
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg','png'])])
    submit = SubmitField('Update')
    
    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username = username.data).first()
            if user:
                raise ValidationError('That Username is Already Taken, Please Choose Another One!')
    
    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email = email.data).first()
            if user:
                raise ValidationError("That Email Already Exists, Please Login")
            

class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Post')