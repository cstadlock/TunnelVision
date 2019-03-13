from app.allImports import *
from werkzeug.security import generate_password_hash
from forms import LoginForm
@app.route("/add/user", methods=["GET", "POST"])
@login_required
def add_user():
    form = LoginForm(request.form)
    users = User.select().where(User.username != current_user.username)
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        
        user = User(username=username, 
                    password=generate_password_hash(password))
        
        if user.save():
            return redirect(url_for("add_user"))
    
    return render_template("add_user.html", users=users, form=form, cfg=cfg)
        