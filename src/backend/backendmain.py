# Filename : backendmain.py
# Author by : Qinliang Xue
# Date : 2024-01-01

from flask import Flask
from flask import request
from flask_cors import CORS # 跨域
from openai import OpenAI
import os

os.environ["http_proxy"] = "http://localhost:7890"
os.environ["https_proxy"] = "http://localhost:7890"

app = Flask(__name__)
CORS(app)
client = OpenAI(api_key='your api key')
@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/get_reply', methods=['GET', 'POST'])
def get_reply():
    if request.method == 'POST':
        question = request.json.get('question')
        system = request.json.get('system')
    else:
        question = request.args.get('question')
        system = request.args.get('system')
    messages = [{'role': 'system', 'content': "你是一个"+system}]
    for i in question[:-1]:
        messages.append({'role': i['role'], 'content': i['text']})
    print("msg:", messages)
    res = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0.7
    )
    print("reply complete!")
    print("res:", res)
    return res.choices[0].message.content

@app.route('/get_more_question', methods=['GET', 'POST'])
def get_more_question():
    if request.method == 'POST':
        system = request.json.get('system')
    else:
        system = request.args.get('system')
    messages = [{'role': 'system', 'content': "你是一个"+system},
                {'role': 'user', 'content': "用户可能会有哪些提问，请帮忙想一想，不超过10个，以python的列表形式返回有利于我阅读，例如：['问题1','问题2','问题3',...,'问题10']"}]
    print("msg:", messages)
    res = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0.7
    )
    print("reply complete!")
    print("res:", res)
    return res.choices[0].message.content

if __name__ == '__main__':
    app.run(debug = True, port=504)
