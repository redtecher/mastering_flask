from flask_wtf import Form
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import DataRequired,Length,Required,Email


class CommentForm(Form):
    name = StringField('Name',validators=[DataRequired(),Length(max=255)])
    text = TextAreaField(u'Comment',validators=[DataRequired()])



class SendEmailForm(Form):
    towho = StringField('Towho',validators=[Required(),Email()])
    subject =StringField('Subject',validators=[Required(),Length(max=64)])
    content =StringField('Content',validators=[DataRequired(),Length(max=255)])
    submit = SubmitField('发送')

