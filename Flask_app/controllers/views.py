from flask import render_template
from controllers import app

@app.route('/')
def index():
    data = 'views.pyのinsert_something部分'
    dict = {
        'insert_dictionary1' : 'views.pyのinsert_dictionary1部分',
        'insert_dictionary2' : 'views.pyのinsert_dictionary2部分',

        'test_titles' : ['タイトル1', 'タイトル2', 'タイトル3']
    }
    return render_template('Flask_app/index.html', insert_something = data, dict = dict)

@app.route('/test')
def test():
    return render_template('Flask_app/testpage.html')