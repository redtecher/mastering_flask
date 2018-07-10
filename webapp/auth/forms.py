#coding:utf-8

from flask_wtf import Form,RecaptchaField
from wtforms import StringField,TextAreaField,PasswordField,BooleanField,SubmitField,BooleanField
from wtforms.validators import DataRequired,Length,EqualTo,URL,Required,Email
from ..models import User

class LoginForm(Form):
    email = StringField('Email',validators=[Required(),Length(1,64),Email()])
    password = PasswordField('password',[DataRequired()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('LOG IN')



class RegisterForm(Form):
    username =StringField('Username',validators=[DataRequired(),Length(max=255)])
    password = PasswordField('Password',validators=[DataRequired(),Length(min=8)])
    confirm = PasswordField('Confirm Password',[DataRequired(),EqualTo('password')])
    recaptcha =  RecaptchaField()
'''
    def validate(self):
        check_validate=super(RegisterForm,self).validate()
        if not check_validate:
            return False

        user = User.query.filter_by(username = self.username.data).first()    


        if user:
            self.username.errors.append('User with that name already exits')    

            return False

        return True
        '''