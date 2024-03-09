from flask import Flask,render_template,request
import joblib

#initalize the app
app = Flask(__name__)

#initalize the model
model = joblib.load("C:\\Users\\Tarunn\\Desktop\\Deployment\\joblib\\Cardio_vascular.pkl")

@app.route("/")
def hello():
    return render_template("Homepage.html")

@app.route("/Contacts")
def contacts():
    return render_template("Contacts.html")

@app.route("/User")
def form_submission():
    return render_template("form.html")

@app.route("/submit", methods = ['post'])
def take_user_input():
    age = int(request.form.get("age"))
    sex = int(request.form.get("sex"))
    cp = int(request.form.get("cp"))
    trestbps = int(request.form.get("trestbps"))
    chol = int(request.form.get("chol"))
    fbs = int(request.form.get("fbs"))
    restecg = int(request.form.get("restecg"))
    thalach = int(request.form.get("thalach"))
    exang = int(request.form.get("exang"))
    oldpeak = float(request.form.get("oldpeak"))
    slope = int(request.form.get("slope"))
    ca = int(request.form.get("ca"))
    thal = int(request.form.get("thal"))


    input = [age, sex , cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
    output = model.predict([input])
    if output[0] == 1:
        return "Patient has Cardio Vascular risk"
    else:
        return "Patient has no Cardio Vascular risk"

app.run(debug=True)