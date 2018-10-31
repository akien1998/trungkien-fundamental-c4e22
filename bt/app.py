from flask import Flask,render_template,request
app = Flask(__name__)

@app.route("/home",methods=["GET","POST"])
def customer():
    if request.method=="GET":
        return render_template("home.html")
    elif  request.method=="POST":
        form = request.form
        question = form["Question"]
        options=[]
        #post
        for k,v in form.items():
            if k!='Question':
                options.append(v)
                print(options)
        return "OK"
if __name__ == '__main__':
  app.run(debug=True)