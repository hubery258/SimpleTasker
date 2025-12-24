import sqlite3
from flask import Flask,render_template,request,redirect

def get_db(): 
    conn = sqlite3.connect("task.db") 
    conn.row_factory = sqlite3.Row # 让结果可以用字典方式访问 
    return conn

app = Flask(__name__)

@app.route("/")
def index():
    tasks = get_db() 
    cursor = tasks.cursor() 
    rows = cursor.execute("SELECT * FROM tasks").fetchall() 
    tasks.close()
    quadrants = [
        {"id": 1, "title": "重要且紧急", "btn_class": "btn-danger", "q_class": "q1"},
        {"id": 2, "title": "重要不紧急", "btn_class": "btn-primary", "q_class": "q2"},
        {"id": 3, "title": "不重要但紧急", "btn_class": "btn-warning", "q_class": "q3"},
        {"id": 4, "title": "不重要不紧急", "btn_class": "btn-success", "q_class": "q4"},
    ]
    return render_template("tasks.html", quadrants=quadrants, tasks=rows)

@app.route("/addTask", methods=["POST"])
def AddTask():
    quadrant = request.form.get("quadrantCheck") # id给JavaScript用，这里查的是name
    name = request.form.get("taskName")
    ddl = request.form.get("taskDDL")
    if not ddl:
        ddl = None

    content = request.form.get("taskCont")
    if not content:
        content = None
    duration = request.form.get("taskDuration")
    duration = int(duration) if duration else None
    
    conn = get_db() 
    cursor = conn.cursor() 
    cursor.execute( "INSERT INTO tasks (name, ddl, content, duration, quadrant) VALUES (?, ?, ?, ?, ?)", (name, ddl, content, duration, quadrant) ) 
    conn.commit() 
    conn.close()
    return redirect("/")
