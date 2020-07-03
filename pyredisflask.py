from flask import Flask,request
import pyredis as redis

app=Flask(__name__)

@app.route('/')
def home():
    return 'you are using <b>pyredis v0.0</b><br>todo:add other contents like documentation ...'


@app.route('/set',methods=['GET','POST'])
def set():
    return str(redis.set(request.values['key'],request.values['value']))

@app.route('/get',methods=['GET','POST'])
def get():
    return str(redis.get(request.values['key']))

@app.route('/remove',methods=['GET','POST'])
def remove():
    return str(redis.remove(request.values['key']))

@app.route('/save')
def save():
    return str(redis.save())

@app.route('/load')
def load():
    return str(redis.load())

app.run()
