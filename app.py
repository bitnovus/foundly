from flask import Flask, request, render_template, redirect, url_for, flash, json, jsonify
from flask.ext.login import (LoginManager, current_user, login_required,
                            login_user, logout_user, UserMixin, AnonymousUser,
                            confirm_login, fresh_login_required)
import os

#=========================================================

app = Flask(__name__)

app.debug=True

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL') \
        if os.environ.get('DATABASE_URL') else 'sqlite:///test.db'

app.config['SECRET_KEY'] = "dgTBa2XnE4xE4RUU4CsUr6czvarLmsENBtCFY8m7KA5BHNgn"

login_manager = LoginManager()
login_manager.setup_app(app)

#=========================================================

@login_manager.user_loader
def load_user(userid):
    return User.get(userid)

#=========================================================

@app.route('/')
def home_page(name=None):
    return render_template('home.html', name=name)

@app.route('/register', methods=["POST"])
def register(name=None):
    print request.json 
    results = dict()
    results["value"] = "A8eADiuohi" #Generate randomly later 
    return render_template('register.html', returned_stuff="A8eADiuohi")

@app.route("/login", methods=["GET", "POST"])
def login(form=None):
    """if request.method ==  "POST" and "username" in request.form:
        # login and validate the user...
        login_user(user)
        flash("Logged in successfully.")
        return redirect(request.args.get("next") or url_for("index"))"""
    return render_template("login.html", form=form)

@app.route('/about')
def about_page(name=None):
    return render_template('about.html', name=name)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
