from flask_restful import Resource,reqparse
from flask import jsonify, request

# parse parameters
parser = reqparse.RequestParser()
parser.add_argument('key', type=str)

class SupportAPI(Resource):
    # http://127.0.0.1:5000/api/?pkg=值
    def get(self):
        try:
            pkg = request.args.get("pkg","")
            # 单行代码
            jsonObj = {"result":eval(pkg),'function':2}

            return jsonify(jsonObj)
        except Exception:
            return jsonify({"error":"error"})
    
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