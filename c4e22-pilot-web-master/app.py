from flask import Flask, render_template,request
app = Flask(__name__)

@app.route("/")
def home():
  return render_template("home.html")

@app.route("/new_poll",methods=["GET","POST"])# kha nang .
def new_poll():
  if request.method=="GET":# thuc te la nhu nao
    return render_template("new_poll.html")
  elif request.method=="POST":
    #1 unpack data
    form = request.form
    question= form['Question']# bat trong html
    options=[]
    for k,v in form.item():
      if k!='Question':
        options.append(v)
    print(question)
    print(options)
    return "Gotcha"


if __name__ == '__main__':
  app.run(debug=True)