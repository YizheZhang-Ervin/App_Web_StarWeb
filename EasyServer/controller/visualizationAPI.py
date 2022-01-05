from flask_restful import Resource,reqparse
from flask import jsonify, request
import random

# parse parameters
parser = reqparse.RequestParser()
parser.add_argument('key', type=str)

# 问号传参
class visualAPI(Resource):
    # http://127.0.0.1:5000/api/data?pkg=值
    def get(self):
        try:
            # pkg = request.args.get("pkg","")
            singleVal = random.randrange(0,100,1)
            jsonObj = {"result":singleVal,"code":200,"msg":"Succeed"}
            return jsonify(jsonObj)
        except Exception:
            return jsonify({"result":"","code":500,"msg":"Fail"})
    
    # http://127.0.0.1:5000/api/
    # 传{"key":"值"}
    def post(self):
        try:
            args = parser.parse_args()
            key = eval(args['key'])
            jsonObj = {"result":key}
            return jsonify(jsonObj)
        except Exception:
            return jsonify({"error":"error"})