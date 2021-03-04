# -*- coding = utf-8 -*-

from flask import Flask, jsonify, request
import json

app = Flask(__name__)


@app.route('/test01', methods=['get'])
def test01():
    res = {'msg': '这是一个测试接口'}
    return jsonify(res)


@app.route('/test02', methods=['POST'])
def test02():
    raw_data = request.get_data()   # 获取json参数，即以raw方式POST
    # test_words = raw_data.get('test_words')

    return raw_data


app.run(host='0.0.0.0', port=5000, debug=True)
