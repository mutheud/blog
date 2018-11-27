
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from app import db
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin,db.Model):

    __tablename__ = 'users'
    
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(),index =True)
    email = db.Column(db.String(),unique = True,index = True)
    bio = db.Column(db.String())
    profile_pic_path = db.Column(db.String())
    pass_secure = db.Column(db.String())
    blogs = db.relationship('Blog',backref = 'user', lazy = 'dynamic')
    comments = db.relationship('Comment',backref = 'user',lazy ='dynamic')
 

    @property
    def password(self):
        raise AttributeError('You cannot access password')

    @password.setter
    def password(self,password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

          
    
    def __repr__(self):
        return f'user {self.username}'


class Blog(db.Model):
    __tablename__ = 'blog'
    
    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String)
    blog =db.Column(db.String(),index = True)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    comments = db.relationship('Comment',backref = 'blog', lazy ='dynamic')

    
    
class Comment(db.Model):
    __tablename__ = 'comment'

    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String)
    comment =db.Column(db.String(),index = True)
    blog_id = db.Column(db.Integer,db.ForeignKey('blog.id'))
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))

