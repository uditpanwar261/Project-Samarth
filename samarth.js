async function askQuery() {
    const query = document.getElementById("query").value;
    const responseDiv = document.getElementById("response");
    const graphImg = document.getElementById("graph");

    responseDiv.innerHTML = "Processing...";
    graphImg.classList.add("hidden");

    const res = await fetch("/ask", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({query})
    });

    const data = await res.json();
    responseDiv.innerHTML = `<p>${data.answer}</p>`;
    
    if (data.graph) {
        graphImg.src = "data:image/png;base64," + data.graph;
        graphImg.classList.remove("hidden");
    }
}
