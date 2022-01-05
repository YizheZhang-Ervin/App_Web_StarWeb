import sys
sys.path.append("EasyServer/")

from controller.visualizationAPI import visualAPI
from flask_restful import Api, reqparse
from flask_cors import CORS
from flask import Flask, jsonify, render_template, request

# 初始化Flask
app = Flask(__name__, static_folder='../EasyClient',
            template_folder='../EasyClient', static_url_path="")
api = Api(app)

# 前后端跨域处理
cors = CORS(app, resources={r"/*": {"origins": "*"}},
            supports_credentials=True)

# 解析前后端传参
parser = reqparse.RequestParser()
parser.add_argument('key', type=str)

# 请求显示主页


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        key = request.args.get('key', '')
        return render_template('index.html', data=key)


# RESTful API 路径
# 路由传参
api.add_resource(visualAPI, '/api/data')
