from flask import Flask,render_template,request
import mlab
from poll import Poll
from random import choice
app = Flask(__name__)
mlab.connect()
@app.route("/new_bike",methods=["GET","POST"])
def new_bike():
    if request.method =="GET":
        return render_template("Exercise_1.html")
    elif request.method=="POST":
        form = request.form
        form=form['first']
        form=form['last']
        form= form['course_imformation']
        form= form['year']
    alphabet="abcdefghijklmnopqrstuvwxyz".upper()
    c =""

    for _ in range(6):
        c+= choice(alphabet)        
    return "OK"

if __name__ == '__main__':
  app.run(debug=True)