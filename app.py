from flask import Flask,redirect,url_for
from sqlalchemy import false
app=Flask(__name__)

@app.route('/')
def welcome():
    return "welcome to my youtube channel"
@app.route('/success/<int:score>')
def success(score):
    return "the person has passed and the marks is"+str(score)

@app.route('/fail/<int:score>')
def fail(score):
    return "the person has failed and the marks is"+str(score)

@app.route('/results/<int:marks>')
def results(marks):
    result=""
    if marks<50:
        result= 'fail'
    else:
        result='success'
    return  redirect(url_for(results,score=marks))





if __name__=='__main__':
    app.run(debug=True)