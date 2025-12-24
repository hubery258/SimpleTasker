// 点击加号时记录象限编号
document.querySelectorAll(".add-task-btn").forEach(btn => {
    btn.addEventListener("click", () => {
        const quadrant = btn.dataset.quadrant;
        document.getElementById("quadrantCheck").value = quadrant;
    });
});