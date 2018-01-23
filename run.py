from flask import Flask
from flask import render_template
from flask import request
import time
import ss
from ss import *
app=Flask(__name__)
print('请输入端口号')
p=input()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ss.html')
def ss():
    pic_dl()
    rs=pic_upload()
    return render_template('ss.html',s=rs)
app.run(host='0.0.0.0',port=int(p)) 
