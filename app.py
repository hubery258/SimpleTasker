import sqlite3
from flask import Flask,render_template,request,redirect,jsonify

def get_db(): 
    conn = sqlite3.connect("task.db") 
    conn.row_factory = sqlite3.Row # 让结果可以用字典方式访问 
    return conn

app = Flask(__name__)

@app.route("/")
def index():
    tasks = get_db() 
    cursor = tasks.cursor() 
    rows = cursor.execute(
    "SELECT * FROM tasks ORDER BY quadrant, completed ASC, (ddl IS NULL) ASC, ddl ASC"
    ).fetchall() # 排序方式：完成置底，未完成按ddl排
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
    completed = 1 if request.form.get("taskCompleted") == "1" else 0
    
    conn = get_db() 
    cursor = conn.cursor() 
    cursor.execute( "INSERT INTO tasks (name, ddl, content, duration, quadrant, completed) VALUES (?, ?, ?, ?, ?, ?)", 
                   (name, ddl, content, duration, quadrant, completed) ) 
    conn.commit() 
    conn.close()
    return redirect("/")

@app.route("/deleteTask", methods=["POST"])
def DeleteTask():
    deleteid = request.form.get("id") 
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks WHERE id = ?", (deleteid,))
    conn.commit()
    conn.close()
    return ("",204)

@app.route("/editTask", methods=["POST"])
def EditTask():
    editid = request.form.get("taskId")
    if not editid:
        return ("Missing id", 400)
    
    name = request.form.get("taskName")
    ddl = request.form.get("taskDDL") or None
    content = request.form.get("taskCont") or None
    duration = request.form.get("taskDuration")
    duration = int(duration) if duration else None
    quadrant = request.form.get("quadrantCheck")
    completed = 1 if request.form.get("taskCompleted") == "1" else 0

    conn = get_db()
    cur = conn.cursor()
    cur.execute(
      "UPDATE tasks SET name=?, ddl=?, content=?, duration=?, quadrant=?, completed=? WHERE id=?",
      (name, ddl, content, duration, quadrant, completed, editid)
    )
    conn.commit()
    conn.close()
    return redirect("/")

# actually I'm not very sure about what the hack happen about the code below
# but it can run,powerful AI indeed.
@app.route("/task/<int:editid>")
def GetTask(editid):
    conn = get_db()
    cur = conn.cursor()
    row = cur.execute("SELECT * FROM tasks WHERE id = ?", (editid,)).fetchone()
    conn.close()
    if not row:
        return ("Not found", 404)
    return jsonify(dict(row))

@app.route("/completeTask", methods=["POST"])
def CompleteTask():
    compid = request.form.get('id')
    state = request.form.get('state')
    if not compid or state is None:
        return ("Missing parameters", 400)
    state_update = 1 if str(state) == '1' else 0
    conn = get_db()
    cur = conn.cursor()
    cur.execute("UPDATE tasks SET completed = ? WHERE id = ?", (state_update, compid))
    conn.commit()
    conn.close()
    return ("", 204)