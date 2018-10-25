from flask import Flask
app = Flask(__name__)

@app.route("/BMI/<int:weight>/<int:height>")
def Body_Mass_Index(weight,height):
    height = height/100
    bmi = weight/(height*height)
    if bmi < 16 :
        return "your bmi = " + str(bmi)+ " Severely underweight"
    elif 16<=bmi<18:
        return "your bmi = " + str(bmi)+ " Underweight"
    elif 18.5<=bmi<25:
        return "your bmi = " + str(bmi)+ " Normal"
    elif 25<=bmi<30:
        return "your bmi = " + str(bmi)+ " Overweight"
    elif bmi > 30:
        return "your bmi = " + str(bmi)+ " Obese"


if __name__ == '__main__':
  app.run(debug=True)