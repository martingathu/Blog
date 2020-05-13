from flask import render_template,request,redirect,url_for, abort, flash
from . import main
from ..models import User, Post
from flask_login import login_required, current_user
from .forms import RegistrationForm, LoginForm
from .. import db
from flask_login import login_user,logout_user,login_required
from ..email import mail_message
from werkzeug.security import generate_password_hash
from .forms import UpdateProfile
from .forms import *
from ..models import *
from ..requests import get_quotes
# from werkzeug.utils import secure_filename


@main.route('/')
def index():
    quotes = get_quotes()
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date.desc()).paginate(page=page, per_page=8)
    return render_template('index.html', posts=posts ,quotes=quotes)


@main.route('/signup' , methods=['GET', 'POST'])
def signup():

    reg_form = RegistrationForm()

    #updates the db if the validation was successful
    if reg_form.validate_on_submit():
        email = reg_form.email.data
        username = reg_form.username.data
        password = generate_password_hash(reg_form.password.data)
        
        user = User(email=email, username=username, password=password)
        db.session.add(user)
        db.session.commit()

        flash(f'Account created for {reg_form.username.data}! successfully.Please login', 'success')

        return redirect(url_for('main.login'))
        
    return render_template('register.html', form=reg_form)


@main.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()

    #login if validation is successful
    if login_form.validate_on_submit():
        # Get a user by username and check password matches hash
        user_object = User.query.filter_by(username=login_form.username.data).first()
        if user_object is not None and user_object.verify_password(login_form.password.data):
            login_user(user_object)
            return redirect(url_for('main.profile',uname=login_form.username.data))
        flash('user or password not found. Please check username and password', 'danger')     
    return render_template('login.html', form=login_form)


@main.route('/user/<uname>', methods=['GET', 'POST'])
def profile(uname):
    user = User.query.filter_by(username = uname).first()
    # form = PostForm()

    if not user.is_authenticated:
        flash('please login', 'danger')
        return redirect(url_for('main.login'))
   
    # if form.validate_on_submit():
    #     topic = form.topic.data
    #     category = form.category.data
    #     description = form.description.data
        
    #     post = Post(owner_id=user.id, topic=topic, category=category, description=description)
    #     db.session.add(post)
    #     db.session.commit()

    #     return redirect(url_for('main.profile', uname=user.username))
    
    page = request.args.get('page', 1, type=int)
    user = User.query.filter_by(username=uname).first()
    posts = Post.query.filter_by(owner_id=user.id). order_by(Post.date.desc()).paginate(page=page, per_page=4)
     

    return render_template("profile/profile.html", user = user, posts=posts )

@main.route('/logout', methods=['GET'])
def logout():
    logout_user()
    flash('you have logged out successfuly', 'success')

    return redirect(url_for('main.index'))


@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data
        user.username = form.username.data
        user.email = form.email.data
        # user.profile_pic_path = form.profile_pic_path.data

        db.session.add(user)
        db.session.commit()

        flash('you have Account has been updated successfuly', 'success')
        return redirect(url_for('main.profile',uname=user.username))

    elif request.method == 'GET':
        form.username.data = user.username
        form.email.data = user.email
        form.bio.data = user.bio
    return render_template('profile/update.html',form =form)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'images/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))


@main.route('/<int:pname>/comment',methods = ['GET','POST'])
@login_required
def comment(pname):
    form = CommentsForm()
    posts = Post.query.filter_by(id=pname).first()
    comment_query = Comment.query.filter_by(post_id = posts.id).all()

    

    if form.validate_on_submit():
        comment = Comment(comment = form.comment.data, post_id = posts.id, user_id= current_user.id)
        
        db.session.add(comment)
        db.session.commit()

        flash('your comment has been posted successfuly', 'success')
        return redirect(url_for('main.comment', pname=pname))

    return render_template('comments.html', form=form, posts = posts, comments = comment_query)

   

@main.route('/<int:pname>/comment',methods = ['POST'])
@login_required
def delete(pname):
    posts = Post.query.filter_by(id=pname).first()
    
    db.session.delete(posts)
    db.session.commit()

    flash('your has been deleted!', 'success')
    
    return redirect(url_for('main.index',pname=pname))


@main.route('/<uname>/blog',methods = ['GET','POST'])
@login_required
def blog(uname):
    user = User.query.filter_by(username = uname).first()
    form = PostForm()

    if not user.is_authenticated:
        flash('please login', 'danger')
        return redirect(url_for('main.login'))
   
    if form.validate_on_submit():
        topic = form.topic.data
        category = form.category.data
        description = form.description.data
        
        post = Post(owner_id=user.id, topic=topic, category=category, description=description)
        db.session.add(post)
        db.session.commit()

        flash('your Blog has been added successfuly!', 'success')
        return redirect(url_for('main.index',uname=user.username))

    return render_template('profile/blog.html', uname=user.username ,form =form)

 


        



