import sqlite3
from flask import Flask,render_template,request,redirect

tasks = sqlite3.connect("task.db")
cursor = tasks.cursor() # 创建游标，是发sql命令的对象


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

@app.route("/addTask", methods=["POST", "GET"])
def AddTask():
    if request.method == "POST":
        quadrant = request.form.get("quadrantCheck")
        name = request.form.get("taskName")
        ddl = request.form.get("taskDDL")
        if not ddl:
            ddl = None

        content = request.form.get("taskCont")
        if not content:
            content = None
        duration = request.form.get("taskDuration")
        cursor.execute("INSERT INTO tasks (name, ddl, content, duration, quadrant) VALUES(?, ?, ?, ?, ?)", (name, ddl, content, duration, quadrant))
        tasks.commit()
        return redirect("/")
    else:
        rows = cursor.execute("SELECT * FROM tasks").fetchall() 
        return render_template("tasks.html", tasks=rows)
