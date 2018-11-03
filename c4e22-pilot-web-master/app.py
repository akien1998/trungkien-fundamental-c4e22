
from flask import Flask, render_template,request
import mlab
from poll import Poll
from random import choice
app = Flask(__name__)
mlab.connect()

@app.route("/")
def home():
  return render_template("home.html")


@app.route("/poll/<poll_code>")
def poll(poll_code):
  #1 get pull
  poll_list = Poll.objects(code=poll_code)
  poll = poll_list[0]
  # print(poll.question)

  #2 render 
  return render_template("polls1.html",p=poll)


@app.route("/polls")
def polls():
  #1 lay du lieu trong tesst2
  poll_list = Poll.objects()
  # print("asjjd")
  #render all polls
  # for p in poll_list:
  #   print(p.question)
  #   print(p.options)
  #   print(p.code)
  return render_template("polls.html",polls=poll_list)

@app.route("/new_poll",methods=["GET","POST"])# kha nang .
def new_poll():
  if request.method=="GET":# thuc te la nhu nao
    return render_template("new_poll.html")
  elif request.method=="POST":
    form = request.form
    Question1 = form["Question1"]
    Question2 = form["Question2"]
    Question3 = form["Question3"]
    alphabet="abcdefghijklmnopqrstuvwxyz".upper()
    code =""
    for _ in range(6):
      code += choice(alphabet)
    p = Poll(question1=q1,question2= q2,question3=q3,code=c )
    p.save()
    #1 unpack data
    # form = request.form
    # question= form['Question']# bat trong html
    # options=[]
    # for k,v in form.items():
    #   if k!='Question':
    #     options.append(v)
    # print(question)
    # print(options)
    # alphabet="abcdefghijklmnopqrstuvwxyz".upper()
    # code =""
    # for _ in range(6):
    #   code += choice(alphabet)
    # p =Poll(question=question,options = options,code=code)
    # p.save()
    return "Gotcha"


if __name__ == '__main__':
  app.run(debug=True)