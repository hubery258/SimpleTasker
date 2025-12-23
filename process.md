# SIMPLE-TASKER
## 0. 项目起点

- 我为什么要做这个 app：final project需要，现有的任务管理我不满意
- 这个项目的初步完成标准是什么：
    - 四象限页面可以正常运行
    - 实现基础任务操作（新增、编辑、删除、移动象限）
- 当前状态：刚立项


# ✅ 如果你想完成这个项目，接下来应该这样做

## **第 1 步：先把 Flask 项目跑起来（最小骨架）**
- 有一个 `app.py`
- 能跑起来
- 浏览器打开 `http://localhost:5000` 能看到一句话

## **第 2 步：创建四象限页面的 HTML 框架（不需要功能）**

你现在只需要一个文件：

```
templates/
    quadrants.html
```

里面放一个最简单的四象限布局（纯 HTML + CSS，不需要 JS，不需要数据库）：

```html
<div class="quadrant q1">重要且紧急</div>
<div class="quadrant q2">重要不紧急</div>
<div class="quadrant q3">不重要但紧急</div>
<div class="quadrant q4">不重要不紧急</div>
```

CSS 也可以先写最简单的：

```css
.quadrant {
    border: 1px solid #ccc;
    height: 200px;
}
```

做到这一步，你就有了：

- 一个能跑的 Flask 项目
- 一个能显示四象限的页面

**这就是最正确的起点。**

---

## **第 3 步：让 Flask 渲染这个页面**

在 `app.py` 里加：

```python
@app.route("/quadrants")
def quadrants():
    return render_template("quadrants.html")
```

然后你就能访问：

```
http://localhost:5000/quadrants
```

看到你的四象限。

---

## **第 4 步：加“添加任务”的最小功能（不接数据库）**

你先不用 SQL。

你只需要：

- 一个输入框
- 一个按钮
- 点击按钮后，把任务显示在某个象限里（前端 JS 完成）

比如：

```html
<input id="task-input" />
<button onclick="addTask()">添加任务</button>

<script>
function addTask() {
    const text = document.getElementById("task-input").value;
    const q1 = document.querySelector(".q1");
    q1.innerHTML += `<div class="task">${text}</div>`;
}
</script>
```

做到这一步，你就有了：

- 四象限页面
- 能添加任务（虽然刷新就没了）

这已经是 **可展示的 demo**。

---

## **第 5 步：再接数据库（SQL）**

等你前端页面跑顺了，再做：

- 创建 `tasks` 表
- 写一个 `/add_task` 的 POST 接口
- 用 AJAX 把任务发给 Flask
- Flask 存进数据库
- 页面刷新后能看到任务

这一步你已经很熟悉了（你记账 app 也做过）。

---

# 🔥 总结成一句话

**不是从“写文档”开始，也不是从“设计系统”开始，而是从“让四象限页面跑起来”开始。**

顺序就是：

1. **Flask 最小骨架跑起来**
2. **四象限 HTML 页面搭出来**
3. **Flask 渲染这个页面**
4. **前端实现最小任务添加（无数据库）**
5. **再接数据库，让任务持久化**

这就是你现在最应该做的路线。


## ⭐ 1. 如何在 `layout.html` 同时引用 `static` 里的 CSS？

Flask 的静态文件必须通过 `url_for('static', filename='...')` 来引用。

假设你有：

```
static/
    css/
        main.css
```

那么在 `layout.html`（或 `base.html`）里这样写：

```html
<link rel="stylesheet" href="{{ url_for('static', filename='css/main.css') }}">
```

只要你把这行放在 `<head>` 里，全站就能用这个 CSS。

---

## ⭐ 3. 如何让不同页面使用不同的 CSS？

你已经有一个全局 layout（比如 `layout.html`），那你可以在里面预留一个 block：

### layout.html

```html
<head>
    <!-- Bootstrap -->
    <link 
        href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" 
        rel="stylesheet">

    <!-- 全局 CSS -->
    <link rel="stylesheet" href="{{ url_for('static', filename='css/main.css') }}">

    {% block extra_css %}{% endblock %}
</head>
```

然后每个页面可以选择性地加自己的 CSS：

### quadrants.html

```html
{% extends "layout.html" %}

{% block extra_css %}
<link rel="stylesheet" href="{{ url_for('static', filename='css/quadrants.css') }}">
{% endblock %}

{% block content %}
<div class="container">
    <h1>四象限</h1>
</div>
{% endblock %}
```

这样你就能做到：

- 全站共享 Bootstrap + main.css  
- 某些页面再加载自己的 quadrants.css  
- 不同页面互不影响  

这是 Flask 项目里最标准、最干净的写法。

