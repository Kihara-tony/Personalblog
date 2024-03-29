from flask import render_template,request,redirect,url_for,abort
from . import main
from ..models import User,Blog,Comment,Subscriber
from .. import db,photos
from .forms import UpdateProfile,BlogForm,CommentForm,SubscriberForm
from flask_login import login_required,current_user
import datetime
from ..email import mail_message

   # main home page
@main.route('/')
def index():
    '''
    View root page function that returnsthe index page and its data
    '''
    title = 'Home - Welcome to My One Time Blog'
    return render_template('index.html',title = title)

#   user profile function
@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)
    return render_template('profile/profile.html',user = user)

# function for updating the users profile
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

# function for updating the users profile picture
@main.route('/user/<uname>/update/pic', methods = ['POST'])
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile', uname = uname))

# function for adding a new blog
@main.route('/blog/new', methods = ['GET','POST'])
@login_required
def new_blog():
    legend = 'New Blog'
    blog_form = BlogForm()
    if blog_form.validate_on_submit():
        title = blog_form.title.data
        blog = blog_form.text.data
        new_blog = Blog(blog_title = title,blog_content = blog,user = current_user)
        new_blog.save_blog()
        subscriber = Subscriber.query.all()
        for email in subscriber:
            mail_message("New Blog Post from My One Time Blog! ","email/postnotification",email.email,subscriber=subscriber)
        return redirect(url_for('main.blog'))
    title = 'New Blog'
    return render_template('new_blog.html', legend = legend, title = title, blog_form = blog_form)

# function for deleting a blog that is no longer up to date or not wanted
@main.route('/blog/delete/<int:id>', methods = ['GET', 'POST'])
@login_required
def delete_blog(id):
    blog = Blog.get_blog(id)
    db.session.delete(blog)
    db.session.commit()
    return render_template('blogs.html', id=id, blog = blog)

# function to delete a comment
@main.route('/blog/comment/delete/<int:id>', methods = ['GET', 'POST'])
@login_required
def delete_comment(id):
    comment = Comment.query.filter_by(id=id).first()
    blog_id = comment.blog
    Comment.delete_comment(id)
    return redirect(url_for('main.blogs',id=blog_id))

# function to save the comments of a blog
@main.route('/blog/<int:id>', methods = ["GET","POST"])
def blog(id):
    blog = Blog.get_blog(id)
    posted_date = blog.posted.strftime('%b %d, %Y')
    comment_form = CommentForm()
    if comment_form.validate_on_submit():
        comment = comment_form.text.data
        name = form.name.data
        new_comment = Comment(comment = comment, name = name, blog_id = blog)
        new_comment.save_comment()
    comments = Comment.get_comments(blog)
    return render_template('blogs.html', blog = blog, comment_form = comment_form,comments = comments, date = posted_date)

# function for helping the user see his blogs
@main.route('/user/<uname>/blogs', methods = ['GET','POST'])
@login_required
def user_blogs(uname):
    user = User.query.filter_by(username = uname).first()
    blogs = Blog.query.filter_by(user_id = user.id).all()
    return render_template('profile/blogs.html', user = user, blogs = blogs)
@main.route('/blogs/recent', methods = ['GET','POST'])
def blogs():
    blogs = Blog.query.order_by(Blog.id.desc()).limit(5)
    return render_template('blogs.html',blogs = blogs)
@main.route('/comments/recent',methods = ['GET','POST'])
def comments():
    comments= Comment.query.order_by(Blog.id.desc()).limit(5)
    return render_template("blogs.html",blogs = blogs)
# function for subscribing in the daily update of a new blog
@main.route('/subscribe', methods=['GET','POST'])
def subscriber():
    subscriber_form=SubscriberForm()
    blogs = Blog.query.order_by(Blog.posted.desc()).all()
    if subscriber_form.validate_on_submit():
        subscriber= Subscriber(email=subscriber_form.email.data,name = subscriber_form.name.data)
        db.session.add(subscriber)
        db.session.commit()
        mail_message("Welcome to My One Time Blog","email/welcome_subscriber",subscriber.email,subscriber=subscriber)
        title= "My One Time Blog"
        return render_template('index.html',title=title, blogs=blogs)
    subscriber = Blog.query.all()
    blogs = Blog.query.all()
    return render_template('subscribe.html',subscriber=subscriber,subscriber_form=subscriber_form,blog=blog)

# function to update the blog
@main.route('/blog/<int:id>/update', methods = ['GET','POST'])
@login_required
def update_blog(id):
    legend = 'Update Blog'
    blog = Blog.get_blog(id)
    form = BlogForm()
    if form.validate_on_submit():
        blog.blog_title = form.title.data
        blog.blog_content = form.text.data
        db.session.commit()
        return redirect(url_for('main.blogs', id = id))
    elif request.method == 'GET':
        form.title.data = blog.blog_title
        form.text.data = blog.blog_content
    return render_template('new_blog.html', legend = legend, blog_form = form, id=id)

