from flask import Flask,request
import pyredis

app=Flask(__name__)

@app.route('/')
def home():
    return 'you are using <b>pyredis v0.0</b><br>todo:add other contents like documentation ...'

app.run()
