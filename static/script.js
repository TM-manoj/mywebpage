// static/script.js
function sendMessage() {
    const message = document.getElementById("inputMsg").value;

    fetch("/api/message", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ message })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("output").innerText = data.reply;
    })
    .catch(error => console.error("Error:", error));
}
