from flask import Flask,request
import pyredis

app=Flask(__name__)

@app.route('/')
def home():
    return 'you are using <b>pyredis v0.0</b><br>todo:add other contents like documentation ...'


@app.route('/set',methods=['GET','POST'])
def set():
    return str(redis.set(request.values['key'],request.values['value']))

app.run()
