from flask import render_template,request,redirect,url_for,abort
from . import main
from ..models import User,Blog,Comment,Subcriber
from .. import db
from .forms import UpdateProfile,BlogForm,CommentForm,SubscriberForm
from flask_login import login_required,current_user
import datetime
from ..email import mail_message

@main.route('/')
def index():
    '''
    View root page function that returnsthe index page and its data
    '''
    title = 'Home - Welcome to My One Time Blog'
    return render_template('index.html',title = title)
@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)
    return render_template('profile/profile.html',user = user)
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
        return redirect(url_for('.profile',uname = user.username))
    return render_template('profile/update.html',form = form)
@main.route('/user/<uname>/update/pic', methods = ['POST'])
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile', uname = uname))

@main.route('/blog/new', methods = ['GET','POST'])
@login_required
def new_blog():
    legend = 'New Blog'
    form = BlogForm()
    if form.validate_on_submit():
        title = form.title.data
        blog = form.text.data
        new_blog = Blog(blog_title = title,blog_content = blog,user = current_user)
        new_blog.save_blog()
        subscriber = Subscriber.query.all()
        for email in subscriber:
            mail_message("New Blog Post from My One Time Blog! ","email/postnotification",email.email,subscriber=subscriber)
        return redirect(url_for('main.index'))
    title = 'New Blog'
    return render_template('new_blog.html', legend = legend, title = title, blog_form = form)
@main.route('/blog/delete/<int:id>', methods = ['GET', 'POST'])
@login_required
def delete_blog(id):
    blog = Blog.get_blog(id)
    db.session.delete(blog)
    db.session.commit()
    return render_template('blogs.html', id=id, blog = blog)
@main.route('/blog/comment/delete/<int:id>', methods = ['GET', 'POST'])
@login_required
def delete_comment(id):
    comment = Comment.query.filter_by(id=id).first()
    blog_id = comment.blog
    Comment.delete_comment(id)
    return redirect(url_for('main.blog',id=blog_id))
