from flask import render_template, request, flash, redirect, url_for  # url)for generates URLs
from flask_login import login_user, logout_user, login_required, current_user
from app.auth.forms import RegistrationForm, LoginForm
from app.auth import authentication as at
from app.catalog import main
from app.auth.models import User


@at.route('/register', methods=['GET', 'POST']) # the get displays the form, the post allows user to submit the data
def register_user():
    form = RegistrationForm()
    if current_user.is_authenticated:
        flash('you are already registered')
        return redirect(url_for('main.display_books'))
    if form.validate_on_submit(): # checks if form is a post request and checks if data is valid
        # these are arguments we have defined in the class method to store user data in the DB
        # form.name.data and the rest come from our form.py
        User.create_user(
            user=form.name.data,
            email=form.email.data,
            password=form.password.data)
        flash('Registration Successful') # # flashes a message that says they are registered
        return redirect(url_for('authentication.do_the_login')) # redirect to a login page after they are successful
    return render_template('registration.html', form=form) # if not unsuccessful send back to registration page- This is a get request as opposed to a post request


@at.route('/login', methods=['GET', 'POST'])
def do_the_login():
    if current_user.is_authenticated:
        flash('you are already logged-in')
        return redirect(url_for('main.display_books'))
    form = LoginForm()   # get request brings back and instance of the form
    if form.validate_on_submit(): # for post request,. checks if data entered by user is valida
        user = User.query.filter_by(user_email=form.email.data).first() # compares what user entered to what is stored in the DB
        if not user or not user.check_password(form.password.data): # if does not exist or password is not corrrect. check_password is one we wrote in models.py
                                                                    # check_password compares hashed PW in DB to what user entered- form.password.data is PW supplied in form.
            flash('Invalid Credentials, Please try again') # if not valid, will flash a message
            return redirect(url_for('authentication.do_the_login')) # rediect to login screen
        login_user(user, form.stay_loggedin.data)
        return redirect(url_for('main.display_books'))
    return render_template('login.html', form=form)  # this send the form to the browser


@at.route('/logout')
@login_required
def log_out_user():
    logout_user()
    flash('Logged out Successfully')
    return redirect(url_for('main.display_books'))


@at.app_errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404
