from flask import Flask,render_template,request
import mlap
from poll import Poll   
app = Flask(__name__)
mlap.connect()


#



@app.route("/gmail",methods=["GET","POST"])
def gmail():
    if request.method=="GET":
        return render_template("email.html")
    elif request.method=="POST":
        form =request.form
        something = form["something"]
        p =  Poll(something=something)
        p.save()
        return render_template("email.html")

    

if __name__ == '__main__':
  app.run(debug=True)