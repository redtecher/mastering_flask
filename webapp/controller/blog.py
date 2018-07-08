from webapp.models import Post,tags,Tag
from webapp import db
from sqlalchemy import func
from os import path
from flask import Blueprint

def sidebar_data():
    recent = Post.query.order_by(Post.publish_date.desc()).limit(5).all()
    
    top_tags =db.session.query(Tag,func.count(tags.c.post_id).label('total')).join(tags).group_by(Tag).order_by('total DESC').limit(5).all()
    return recent,top_tags


blog_blueprint = Blueprint('blog',__name__,template_folder=path.join(path.pardir,'templates','blog'),url_prefix="/blog")

