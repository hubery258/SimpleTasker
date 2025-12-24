// 点击加号时记录象限编号
document.querySelectorAll(".add-task-btn").forEach(btn => {
    btn.addEventListener("click", () => {
        const quadrant = btn.dataset.quadrant;
        document.getElementById("quadrantCheck").value = quadrant;
    });
});

document.addEventListener('click', async (e) => {
if (e.target.matches('.delete-task-btn')) {
const id = e.target.dataset.id;
if (!confirm('确认删除该任务？')) return;
const resp = await fetch('/deleteTask', { method: 'POST', body: new URLSearchParams({ id }) });
if (resp.ok) e.target.closest('.task-item').remove();
else alert('删除失败');
}
});

document.addEventListener('click', async (e) => {
  if (e.target.matches('.edit-task-btn')) {
    const id = e.target.dataset.id;
    const resp = await fetch(`/task/${id}`);
    if (!resp.ok) { alert('加载任务失败'); return; }
    const t = await resp.json();
    document.getElementById('taskId').value = t.id;
    document.querySelector('[name="taskName"]').value = t.name || '';
    document.querySelector('[name="taskDDL"]').value = t.ddl || '';
    document.querySelector('[name="taskCont"]').value = t.content || '';
    document.querySelector('[name="taskDuration"]').value = t.duration || '';
    document.getElementById('quadrantCheck').value = t.quadrant || '';
    document.getElementById('taskCompleted').checked = t.completed == 1;
    document.getElementById('taskForm').action = '/editTask';
    document.querySelector('#taskModal .modal-title').textContent = '编辑任务';
    new bootstrap.Modal(document.getElementById('taskModal')).show();
  }
});

// 当点击“新增”按钮时，清空 modal（保留你已有记录逻辑）
document.querySelectorAll('.add-task-btn').forEach(btn => {
  btn.addEventListener('click', () => {
    document.getElementById('taskForm').action = '/addTask';
    document.getElementById('taskId').value = '';
    document.getElementById('taskCompleted').checked = false;
    document.querySelector('#taskModal .modal-title').textContent = '添加任务';
  });
});

// √ 按钮：切换完成状态并更新 UI
document.addEventListener('click', async (e) => {
  if (e.target.matches('.done-task-btn')) {
    const btn = e.target;
    const id = btn.dataset.id;
    const cur = btn.dataset.completed === '1' ? 1 : 0; // current state
    const next = cur ? 0 : 1;

    const resp = await fetch('/completeTask', {
      method: 'POST',
      body: new URLSearchParams({ id, state: String(next) })
    });

    if (resp.ok) {
      btn.dataset.completed = String(next);
      const taskItem = btn.closest('.task-item');
      const nameEl = taskItem && taskItem.querySelector('.task-name');
      if (nameEl) {
        if (next === 1) nameEl.classList.add('completed');
        else nameEl.classList.remove('completed');
      }
      location.reload();
    } else {
      alert('更新完成状态失败');
    }
  }
});