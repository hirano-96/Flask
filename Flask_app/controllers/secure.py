
from controllers import app,views
from flask import Flask, jsonify, make_response, render_template, request, redirect, session
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
from flask_restx import Api, Resource

api = Api(app, doc='/documents/')

# ユーザー作っとく
users = [
    {'user_id': 'U0000001', 'login_id': 'user1@example.com','password': 'password123', 'name': 'yamada'},
    {'user_id': 'U0000002', 'login_id': 'user2@example.com','password': 'password456', 'name': 'suzuki'},
    {'user_id': 'U0000003', 'login_id': 'user3@example.com','password': 'password789', 'name': 'saitou'},
]

def authenticate(login_id, password):
    """認証処理

    Args:
        login_id (string): ログインID
        password (string): パスワード

    Returns:
        list: 取得したユーザ情報（取得できなければNONE）
    """
    auth_user = next(
        (user for user in users
            if (user.get('login_id') == login_id and user.get('password') == password)),
        None)

    return auth_user


@api.route('/no-secure')
class NoSecureController(Resource):
    """認証不要で呼び出せるクラス（ドア開けっ放し。ログイン画面とか。）"""

    def get(self):
        return make_response(jsonify({'message': 'This is NonSecure Endpoint.'}), 200)

@app.route('/login', methods=['GET'])
class LoginController(Resource):
    """認証用のクラス"""
    def post(self):
        input_data = request.json
        auth_user = authenticate(input_data.get('login_id'), input_data.get('password'))
        if auth_user is None:
            return make_response(jsonify({'message': 'Invalid User.'}), 401)

        access_token = create_access_token(identity=auth_user['user_id'])
        return make_response({'access_token': access_token}, 200)

@api.route('/secure')
class SecureController(Resource):
    """認証必須で呼び出せるクラス（ログイン後の画面遷移とか。）"""
    @jwt_required() # 認証必須とする記述
    def get(self):
        return make_response(jsonify({'message': 'This is Secure Endpoint.'}), 200)