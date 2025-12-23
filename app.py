from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/")
def index():
    quadrants = [
        {"id": 1, "title": "重要且紧急", "btn_class": "btn-danger", "q_class": "q1"},
        {"id": 2, "title": "重要不紧急", "btn_class": "btn-primary", "q_class": "q2"},
        {"id": 3, "title": "不重要但紧急", "btn_class": "btn-warning", "q_class": "q3"},
        {"id": 4, "title": "不重要不紧急", "btn_class": "btn-success", "q_class": "q4"},
    ]
    return render_template("tasks.html", quadrants=quadrants)
