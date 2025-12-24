# note

## ABOUT `layout.html`
- body里的`bg-light`是bootstrap的背景工具

## ABOUT `tasks.html`
- `container-fluid`是bootstrap的*容器类*，占满视口横向空间，`p-4`是bootstrap的间距工具，给这个大元素的四周都加上一点间距，可用 `pt-`, `pb-`, `px-`, `py-` 调整方向性内边距,`mb-4`大约同理
- `row`来自bootstrap，`quadrant-container`是css自定义
- `position-relative`来自bootstrap，把元素设置为相对定位，以此元素作为定位参照
- `col-6`是bootstrap的一个设置，把横向分成12份，每份占6，
- `btn`,`btn-sm`,`btn-danger`是bootstrap类，控制按钮样式和配色，`position-...`用于绝对定位，`top-0`,`end-0`用于向上对齐和靠右对齐
- `add-task-btn`是自定义项，在`tasks.js`里绑定点击事件
- HTML 属性是 `data-quadrant="1"`，浏览器把所有以 `data-` 开头的自定义属性映射到元素的 `dataset`对象上，`data-`前缀在 `dataset` 中被去掉，所以用 `element.dataset.quadrant` 访问（返回字符串 "1"）。
  - `data-bs-toggle`是bootstrap的data-API属性，告诉Bootstrap JS 把这个触发器当作打开 modal 的控件（modal是一个覆盖页面的对话框/弹窗，用于临时收集信息或提示，阻断页面其它交互直到关闭。）
  - `data-bs-target="#taskModal"：Bootstrap` 用来定位要打开的 modal 的选择器（这里是 id 为 taskModal 的元素，应该在 `task_modal.html` 中定义）。可以是任何有效的 CSS 选择器（常用 #id）
- 在熟练后，考虑到这些都是重复工作，用jinja的for语法代替写好了
- `span`只是用来包裹小块文本，与`div`不同，不会换行，可以配合`text-muted`(柔和文本 from [bootstrap](https://getbootstrap.com/docs/4.0/utilities/colors/))用来显示较淡的东西
- `flex`和他的各种[参数](https://getbootstrap.com/docs/4.0/utilities/flex/)
- **值得一学**:`src="{{ url_for('static', filename='tasks.js') }}"`用于实现jinja中非同路径的文件调用

## ABOUT `task_modal.html`
- bootstrap容器：
  - `modal`,`fade`控制卡片呈现动画
  - `modal-diaglog`，`modal-content`,`modal-body`,`modal-header`,`modal-footer`是boo标准结构与样式容器；
  - `btn-close`boo控制关闭样式；
  - `form-label`, `form-control`, `mb-3`: boo控制表单布局与间距、输入样式。
  - `data-bs-dismiss="modal"`: Bootstrap data-API，用于让按钮自动关闭 modal。
  - [about button](https://getbootstrap.com/docs/4.0/components/buttons/)

## ABOUT `tasks.js`
- 使用class查找可以用`document.querySelectiorAll(".xxxx")`,而对于id查找`document.getElementById("<idname>")`会更方便
- 其他的大致都能理解，反正JavaScript只能一点一点理解，一动起来就有点不懂desuwa,以后再来搞懂，主要还是看得懂，就是具体怎么执行就会比较复杂。

## ABOUT `app.py`
- 真实环境中的sql不同于cs50里的使用方式，可以趁此机会学习，`sqlite3`是python内置库：
  - `connect`函数可以打开一个db文件
  - `conn.row_factory = sqlite3.Row`实现字典式的键值对应访问
  - `connect().cursor`创建一个新的*游标*，用来执行操作,`connect().cursor.execute(...)`即可，后面跟的`fetchall`可以用来一次性取回游标里剩下的所有结果行，返回一个列表（list），默认会返回元组（tuple），但是前面已经设置了字典风格，`fetchone`就是只返回一条
  - `commit()`如果不是查询操作，需要commit结果进db文件
  - `cursor.execute("DELETE FROM tasks WHERE id = ?", (deleteid,))` sql命令里需要给参数时要写成tuple形式
  - 记得`close()`
  - sql里要设置成null需写`None`

- `request.form.get`表单都是直接返回字符串，要手动修改一下格式，可以看看`if else`的简写

- `return("",204)`就是只需要返回一个无内容的成功通知，在js中检测,`return jsonify(dict(row))`就是返回了JSON（对于JSON我只能说基本一窍不通，待学习）

## 碎碎念
- **cs的各种文档确实是很多很杂，css一个，js一个，bootstrap又一个，python一个，杂七杂八还有很多...因为本意也不是从头读到尾的再去用的，应该是实际边做边根据当下实际需要去翻去找怎么做怎么理解，而vibe-coding使得这种“面向项目学习”方式更加容易实现了**


