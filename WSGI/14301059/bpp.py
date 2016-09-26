from flask import Flask
from flask import request

app=Flask(__name__)

@app.route('/aaa',methods=['GET','POST'])
def home():
	return '<h1>hello aaa</h1>'


@app.route('/hello.html',methods=['GET','POST'])
def erro():
	return '<h1>404 NOT FOUND</h1>'

if __name__ == '__main__':
	app.run()

