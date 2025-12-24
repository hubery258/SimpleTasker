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