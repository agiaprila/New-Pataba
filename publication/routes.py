from publication import app, db
from publication.models import Users
from flask import render_template, flash, redirect, url_for, request
from publication.forms import LoginForm
from flask_login import login_user, logout_user, current_user

# home page
@app.route('/')
@app.route('/home')
def home_page():
  return render_template('index.html')

# publication page
@app.route('/publikasi')
def publikasi_page():
  return render_template('publikasi.html')

# login
@app.route('/login', methods=['GET', 'POST'])
def login_page():
  if current_user.is_authenticated:
    flash("You are already login", category='danger')
    return redirect(url_for('home_page'))
  else:
    form = LoginForm()
    if form.validate_on_submit():
      attempted_user = Users.query.filter_by(email=form.email.data).first()
      if attempted_user:
        if attempted_user.check_password_correction(attempted_password=form.password.data):
          login_user(attempted_user)
          flash('Anda Berhasil Login', category="success")
          return redirect(url_for('home_page'))
        else:
          flash('Password Salah', category="danger")
      else:
        flash('Email Tidak DItemukan', category="danger")
  return render_template('login.html', form=form)

# logout
@app.route('/logout')
def logout_page():
  logout_user()
  flash('Anda Telah Keluar', category="info")
  return redirect(url_for('login_page'))