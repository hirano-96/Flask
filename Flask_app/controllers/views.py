from flask import request, redirect, flash, render_template, session
from controllers import app

@app.route('/')
def root():
    if 'flag' in session and session['flag']:
        return render_template('Flask_app/login.html', username=session['username'])
    return redirect('/login')

@app.route('/login', methods=['GET'])
def login():
    if 'flag' in session and session['flag']:
        return redirect('/index')
    return render_template('Flask_app/login.html')

@app.route('/login', methods=['POST'])
def login_post():
    username = request.form['username']
    password = request.form['password']
    if username != app.config['USERNAME'] or password != app.config['PASSWORD']:
        flash('ユーザ名またはパスワードが異なります')
    else:
        session['flag'] = True
        session['username'] = username
    if session['flag']:
        return render_template('Flask_app/index.html', username=session['username'])
    else:
        return redirect('/login')

@app.route('/index')
def index():
    if 'flag' in session and session['flag']:
        return render_template('Flask_app/index.html', username=session['username'])
    return redirect('/login')

@app.route('/contents')
def contents():
    if 'flag' in session and session['flag']:
        return render_template('Flask_app/contents.html', username=session['username'])
    return redirect('/login')

@app.route('/detail', methods=['GET'])
def detail():
    return render_template('Flask_app/detail.html')

@app.route('/update', methods=['GET'])
def update():
    return render_template('Flask_app/update.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    session.pop('flag', None)
    session['username'] = None
    session['flag'] = False
    flash('ログアウトしました')
    return redirect('/login')