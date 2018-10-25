from flask import Flask,render_template,redirect
app = Flask(__name__)

@app.route("/about-me")
def all_about_me():
    return render_template("aboutme.html")
@app.route("/school")
def all_school_me():
    return redirect("http://techkids.vn")


# @app.route("/")# neeu ng truy caap trang chu goij ham nay
# def homepage():
#     return "wellcome to C4E web module sever"

# @app.route("/Quan")
# def hello_quan():
#     return "hello quan "

# @app.route("/praise/12c")
# def kien_12c():
#     return "dsdsdsdsdsdsds"

# @app.route("/praise/<int:x>/<int:y>")
# # def praise(name):
# #     return name + " is awesome"
# def praise(x,y):
#     s = int(x)+int(y)
#     return str(s)

@app.route("/question")
def show_question():
    return render_template("question.html")


if __name__ =="__main__":
    app.run(debug=True)# reset sever


