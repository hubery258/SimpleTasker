// 点击加号时记录象限编号
document.querySelectorAll(".add-task-btn").forEach(btn => {
    btn.addEventListener("click", () => {
        const quadrant = btn.dataset.quadrant;
        document.getElementById("quadrantInput").value = quadrant;
    });
});

// 提交任务
document.getElementById("submitTask").addEventListener("click", () => {
    const q = document.getElementById("quadrantInput").value;
    const name = document.getElementById("taskName").value;
    const ddl = document.getElementById("taskDDL").value;
    const desc = document.getElementById("taskDesc").value;
    const attr = document.getElementById("taskAttr").value;
    const loc = document.getElementById("taskLocation").value;
    const dur = document.getElementById("taskDuration").value;

    // 生成任务卡片
    const card = document.createElement("div");
    card.className = "task-card";
    card.innerHTML = `
        <strong>${name}</strong><br>
        <small>DDL: ${ddl}</small><br>
        <small>${desc}</small><br>
        <small>属性: ${attr}</small><br>
        <small>地点: ${loc}</small><br>
        <small>预计: ${dur} 分钟</small>
    `;

    // 插入对应象限
    document.querySelector(`.q${q} .task-list`).appendChild(card);

    // 清空表单
    document.getElementById("taskForm").reset();

    // 关闭 modal
    const modal = bootstrap.Modal.getInstance(document.getElementById("taskModal"));
    modal.hide();
});
