from flask import Flask
from flask import render_template
from flask_script import Manager,Server
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate,MigrateCommand
from sqlalchemy import func
from flask_wtf import Form
import datetime
from wtforms import StringField,TextAreaField
from wtforms.validators import DataRequired,Length
from flask import g,session,abort
from ..models import db,User,Tag,Post,Comment,tags
from .forms import CommentForm,SendEmailForm
from . import main
from flask_mail import Message
from webapp import mail

def sidebar_data():
    recent = Post.query.order_by(Post.publish_date.desc()).limit(5).all()
    
    top_tags =db.session.query(Tag,func.count(tags.c.post_id).label('total')).join(tags).group_by(Tag).order_by('total DESC').limit(5).all()
    return recent,top_tags



def send_mail(to,subject,content,**kwargs):
    msg =Message(subject=subject,sender='121674005@qq.com',recipients=[to])
    msg.body = content
    mail.send(msg)
    
    
    


    
@main.route('/')
@main.route('/<int:page>')
def home(page=1):
    posts = Post.query.order_by(Post.publish_date.desc()).paginate(page,10)
    recent,top_tags = sidebar_data()
    
    return render_template('home.html',posts= posts,recent=recent,top_tags=top_tags)




@main.route('/post/<int:post_id>',methods=('GET','POST'))
def post(post_id):
    
    form = CommentForm()
    if form.validate_on_submit():   #There is some problem in this one
        new_comment = Comment()
        new_comment.name=form.name.data
        new_comment.text = form.text.data
        new_comment.post_id=post_id
        new_comment.date = datetime.datetime.now()
        db.session.add(new_comment)
        db.session.commit()

    post = Post.query.get_or_404(post_id)
    tags = post.tags
    recent,top_tags = sidebar_data()
        
    comments = post.comments.order_by(Comment.date.desc()).all()
    return render_template('post.html',post=post,tags=tags,recent=recent,top_tags=top_tags,comments=comments,form=form)



@main.route('/tag/<string:tag_name>')
def tag(tag_name):
    tag = Tag.query.filter_by(title=tag_name).first_or_404()
    posts = tag.posts.order_by(Post.publish_date.desc()).all()
    recent,top_tags = sidebar_data()

    return render_template('tag.html',tag= tag,posts = posts,recent=recent,top_tags=top_tags)

@main.route('/user/<string:username>')
def user(username):
    user =User.query.filter_by(username=username).first_or_404()
    posts = user.posts.order_by(Post.publish_date.desc()).all()
    recent,top_tags =sidebar_data()

    return render_template('user.html',user=user,posts=posts,recent=recent,top_tags=top_tags)


@main.route('/email',methods = ['GET','POST'])
def sendemail():
    form=SendEmailForm()
    if form.validate_on_submit():
        content =form.content.data
        subject = form.subject.data
        towho =form.towho.data
        send_mail(towho,subject,content)
    return render_template('email.html',form=form)
        




    

    
