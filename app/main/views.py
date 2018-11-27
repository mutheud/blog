from flask_login import login_required,current_user
from flask import render_template,request,redirect,url_for,abort
from . import main
from ..models import User,Comment,Blog
from .forms import UpdateProfile,BlogForm,CommentForm
from .. import db,photos


@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)
    
    return render_template("profile/profile.html",user = user)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))

@main.route('/',methods=['GET','POST'])
def index():
    blogs = Blog.query.all()
    return render_template('index.html',blogs = blogs)

@main.route('/add/blog',methods = ['GET','POST'])
def add_blog():
    form = BlogForm()

    if form.validate_on_submit():
        title = form.Title.data
        blog = form.blog.data
        #category = form.category.data
        
        new_blog = Blog(title = title, blog = blog, user = current_user)
        db.session.add(new_blog)
        db.session.commit()
        return redirect(url_for('main.index'))

    return render_template('add_blog.html', form = form)


@main.route('/add/comment/<blog_id>',methods = ['GET','POST'])
def add_comment(blog_id):
    form = CommentForm()
    blog = Blog.query.filter_by(id = blog_id).first()
    if form.validate_on_submit():
        title = form.Title.data
        comment = form.comment.data
        new_comment = Comment(title = title, comment = comment, user = current_user, blog = blog)
        db.session.add(new_comment)
        db.session.commit()
        return redirect(url_for('main.index'))
        
    return render_template('add_comment.html', form = form)

@main.route('/view/comment<blog_id>',methods = ['GET','POST'])
def view_comment(blog_id):
    blog = Blog.query.filter_by(id = blog_id).first()
    comments = Comment.query.filter_by(blog_id = blog.id)
        
    return render_template('view_comment.html', comments = comments)





