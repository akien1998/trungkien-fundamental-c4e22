from flask import Flask, render_template, request,redirect,url_for
import mlab
from poll import Poll 
from random import choice
from vote import Vote

app = Flask(__name__)
mlab.connect()

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/poll/<poll_code>",methods=["GET","POST"])
def poll(poll_code):
  #1. Get poll

  # objects(yob__lt=1990)
  poll_list = Poll.objects(code=poll_code)
  
  if request.method=="GET":
    return render_template("vote.html",poll=poll)
  elif request.method=="POST":
    form = request.form
    choice = form["choice"]
    voter= form["voter"]
    new_vote = Vote(choice=choice,voter=voter,poll=poll)
    new_vote.save()
    return "OK"
  # print(poll.question)
  # print(poll.options)


  #2. Render
   


@app.route("/polls")
def polls():
  #1. Read all polls 
  poll_list = Poll.objects()

  # for p in poll_list:
  #   print(p.question)

  #2. render all polls    
  return render_template("polls.html",polls=poll_list)
@app.route("/vote/<poll_code>")
def vote(poll_code):
  # lay cai poll ra
  poll= Poll.objects(code=poll_code).first()
  # render poll detail
  return render_template("vote.html",poll=poll)# trang la data
  # input , nhan form

@app.route("/new_poll", methods=["GET","POST"])
def new_poll():
  if request.method == "GET":
    return render_template("new_poll.html")
  elif request.method == "POST":
    # 1. unpack data (form)
    form = request.form 
    question = form["Question"]
    options = []
    for k,v in form.items():
      if k != "Question":
        options.append(v)
    print(question)
    print(options)  
    alphabet = "abcdefghijklmnopqrstuvwxyz".upper()
    code = ""
    for _ in range(6):
      code+= choice(alphabet) 

    p = Poll(question=question, options=options, code=code)
    p.save()     
    url = url_for("poll",poll_code = p.code)
    return redirect(url)  

if __name__ == '__main__':
  app.run(debug=True)