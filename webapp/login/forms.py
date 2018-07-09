from flask_wtf import Form,RecaptchaField
from wtforms import StringField,TextAreaField,PasswordField,BooleanField
from wtforms.validators import DataRequired,Length,EqualTo,URL
from ..models import User

class LoginForm(Form):
    username = StringField('Name',[DataRequired(),Length(max=255)])
    password = PasswordField('password',[DataRequired()])

    def validate(self):
        check_validate =super(LoginForm,self).validate()

        if not check_validate:
            return False
        

        user = User.query.filter_by(username = self.username.data).first()
        if not user:
            self.username.errors.append('Invalid username')
            return False

        
        if not self.user.check_password(self.password.data):
            self.username.errors.append('Invalid username or password')
            return False

        return True


class RegisterForm(Form):
    username =StringField('Username',validators=[DataRequired(),Length(max=255)])
    password = PasswordField('Password',validators=[DataRequired(),Length(min=8)])
    confirm = PasswordField('Confirm Password',[DataRequired(),EqualTo('password')])
    recaptcha =  RecaptchaField()

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
class PostForm(Form):
    title = StringField('Title',validators=[DataRequired(),Length(max=255)])
    text = TextAreaField('Content',validators=[DataRequired()])
'''




