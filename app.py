from flask import Flask, g, request           
import sqlite3
import json   

dbpath = 'test.db' #テーブルを保存するファイル
app = Flask(__name__)

def get_db():#データベースのコネクションを取得
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(dbpath)
        db.execute('CREATE TABLE IF NOT EXISTS tweets_tbl(id INTEGER PRIMARY KEY AUTOINCREMENT, tweet VARCHAR(140))')
    return db 

@app.route('/tweet', methods=['GET'])
def get_tweets():
    con = get_db() #コネクションを取得
    con.row_factory = sqlite3.Row #カラム名取得のため
    cur = con.cursor() #カーソル取得

    cur.execute('SELECT * FROM tweets_tbl')
    tweets = []
    for row in cur.fetchall(): #sqlite3.Row オブジェクトを dict に変換
        tweets.append(dict(row))

    return json.dumps(tweets,indent=2)

@app.route('/tweet/<id>', methods=['GET'])
def get_tweet(id):
    con = get_db() #コネクション
    con.row_factory = sqlite3.Row #カラム名取得のため
    cur = con.cursor() #カーソル取得

    cur.execute(f"SELECT * FROM tweets_tbl WHERE id = {id}")
    tweets = []
    for row in cur.fetchall(): #sqlite3.Row オブジェクトを dict に変換
        tweets.append(dict(row))

    return json.dumps(tweets,indent=2)

@app.route('/tweet', methods=['POST'])
def post_tweet():
    con = get_db() #コネクション
    cur = con.cursor() #カーソルインスタンスを作成

    tweet = request.json["tweet"] #POSTメソッド のデータを取得
    cur.execute(f"INSERT INTO tweets_tbl(tweet) values('{tweet}')") #ツイート文をテーブルにINSERT
    con.commit()

    return 'Success a Tweet!\n'

@app.route('/tweet/<id>', methods=['PUT'])
def put_tweet(id):
    con = get_db() #コネクション
    cur = con.cursor() #カーソルインスタンスを作成

    tweet = request.json["tweet"]
    cur.execute(f"UPDATE tweets_tbl SET tweet = '{tweet}' WHERE id = {id}")
    con.commit()

    return 'Update a Tweet!\n'

@app.route('/tweet/<id>', methods=['DELETE'])
def delete_tweet(id):
    con = get_db() #コネクション
    cur = con.cursor() #カーソルインスタンスを作成
    cur.execute(f"DELETE FROM tweets_tbl WHERE id = {id}")
    con.commit()

    return 'Delete a Tweet!\n'

if __name__ == "__main__":
    app.run() 