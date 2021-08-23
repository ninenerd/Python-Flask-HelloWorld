
from flask import Flask, request, jsonify
app=Flask(__name__)
import random

@app.route('/',methods=['GET','POST'])
def test():
    if request.method=='GET':
        return jsonify({'reponse':"received,OK "})

@app.route('/square')       
def square():
    if request.method=='GET':
        return jsonify({"square":random.randint(11,111)**2})


@app.route('/sqrt')       
def sqrt():
    if request.method=='GET':
        return jsonify({"sqrt":random.randint(11,111)**(0.5)})


if __name__ =='__main__':
    app.run()

