const addBtn = document.getElementById("btn-add"); // fixed ID
const taskField = document.querySelector("#taskInput"); // fixed selector
const taskContainer = document.querySelector(".task-list");

let tasks = [];

document.onload (function () {
    const storedTasks = localStorage.getItem("tasks");
    if (storedTasks) {
        tasks = JSON.parse(storedTasks);
        tasks.forEach(task => {
            const newElement = document.createElement("p");
            newElement.innerHTML = `<span>${task}</span>`; // fixed template literal
            taskContainer.appendChild(newElement);
        });
    }
})

const addTask = function () {
    const task = taskField.value.trim();
    if (task === "") return;

    const newElement = document.createElement("p");
    newElement.innerHTML = `<span>${task}</span>`; // fixed template literal
    taskContainer.appendChild(newElement);

    tasks.push(task); // Now pushes on both click and Enter
    localStorage.setItem("tasks", JSON.stringify(tasks));

    taskField.value = ""; // Clear the input
};

addBtn.addEventListener("click", addTask);

taskField.addEventListener("keypress", function (event) {
    if (event.key === "Enter") {
        addTask(); 
    }
});
