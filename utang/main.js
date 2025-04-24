
function addUtang() {
    const lenders = document.getElementById("utangList"); // fix: correct id

    const nameInput = document.getElementById("nameInput").value;
    const utang = document.getElementById("utang").value;

    if (nameInput.trim() === "" || utang.trim() === "") {
        alert("Please fill in both fields.");
        return;
    }

    const newUtang = document.createElement("li");
    newUtang.textContent = nameInput + " - " + utang;

    lenders.appendChild(newUtang);
}