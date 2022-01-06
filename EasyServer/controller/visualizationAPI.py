from flask_restful import Resource,reqparse
from flask import jsonify, request
import random
from service.serialCRUD import EasySerial
from service.dataCRUD import EasyData

# parse parameters
parser = reqparse.RequestParser()
parser.add_argument('key', type=str)

# 常量
dataName = "data"

# 问号传参
class visualAPI(Resource):
    # http://127.0.0.1:5000/api/data?status=值
    def get(self):
        try:
            status = request.args.get("status","close")
            if status=="open":
                pass
            else:
                pass
            serial001 = EasySerial(EasyData(dataName))
            print(serial001.availablePorts)
            singleVal = random.randrange(0,100,1)
            jsonObj = {"result":singleVal,"code":200,"msg":"Succeed"}
            return jsonify(jsonObj)
        except Exception as e:
            return jsonify({"result":"","code":500,"msg":f"Fail->{e}"})
    
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