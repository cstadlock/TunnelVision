from ..API.user import getUser
from ..allImports import *
from werkzeug.security import check_password_hash
from flask_login import login_user, logout_user
from forms import LoginForm

@app.route('/login', methods=['GET', 'POST'])
def login():
    # Here we use a class of some kind to represent and validate our
    # client-side form data. For example, WTForms is a library that will
    # handle this for us, and we use a custom LoginForm to validate.
    form = LoginForm(request.form)
    
    if form.validate_on_submit():
        # Login and validate the user.
        # user should be an instance of your `User` class
        print "form_submitted"
        username = form.username.data
        password = form.password.data
        print username, password
        user = getUser(username)
        if user is not None:
            print "user found"
            if check_password_hash(user.password, password):
                login_user(user)
            else:
                abort(403)
        else:
            print "user not found"
            abort(403)

        flash('Logged in successfully.')

        next = request.args.get('next')
        # is_safe_url should check if the url is safe for redirects.
        # See http://flask.pocoo.org/snippets/62/ for an example.
        # if not is_safe_url(next):
            # return abort(400)

        return redirect(next or url_for('orders'))
    return render_template('login.html', form=form, cfg=cfg)
    

@app.route('/logout', methods=['GET'])
def logout():
    logout_user()
    return redirect(url_for("orders"))