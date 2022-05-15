from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.user_models import User
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)


@app.route('/')
def index():
    return render_template('index.html')


# Registration Form app route #

@app.route('/register', methods=['POST'])
def register():
    if not User.validate_email(request.form):
        return redirect('/')    
    if not User.validate_pass(request.form):
        return redirect('/')
    if not User.validate_names(request.form):
        return redirect('/')
    pw_hash = bcrypt.generate_password_hash(request.form['pw1'])
    data = {
        'first_name':request.form['first_name'],
        'last_name':request.form['last_name'],
        'email':request.form['email'],
        'pw_hash' : pw_hash
    }
    user_id = User.save(data)
    session['user_id'] = user_id
    return redirect('/success')

# Login app route #

@app.route('/login', methods = ['POST'])
def login():
    data = {
        'email': request.form['email']
    }
    user_in_db = User.get_by_email(data)
    if not user_in_db:
        flash('Email not registered!')
        return redirect('/')
    if not bcrypt.check_password_hash(user_in_db.pw_hash, request.form['pw']):
        flash('Invalid Password!')
        return redirect('/')
    session['user_id'] = user_in_db.id
    return redirect('/success')

# Session ID creation #

@app.route('/success')
def success():
    data = {
        'id': session['user_id']
    }
    user = User.get_one(data)
    return render_template('success.html', user = user)

# Logout Session clear #

@app.route('/logout')
def logout():
    session.clear()
    return redirect ('/')
