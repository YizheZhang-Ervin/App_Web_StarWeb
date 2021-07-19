import sys
sys.path.append("server_flask/")

from flask import Flask, jsonify, render_template, request
from flask_restful import Api,reqparse
from flask_cors import CORS

import jsonAPI

# Initialize Flask
app = Flask(__name__,static_folder='../client',template_folder='../client',static_url_path="")
api = Api(app)

# Cross Domain
cors = CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)

# parse parameters
parser = reqparse.RequestParser()
parser.add_argument('key', type=str)

# Basic Route
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        key = request.args.get('key', '')
        return render_template('index.html', data=key)

# RESTful API Route
# 路由传参
api.add_resource(jsonAPI.jsonAPI, '/api/<key>')
api.add_resource(jsonAPI.jsonAPI2, '/api/')