document.getElementById("loginForm").addEventListener("submit", async function(event) {
    event.preventDefault();

    const username = document.getElementById("username").value;
    const tagline = document.getElementById("tagline").value;

    try {
        const response = await fetch("/api/playstyle", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ username, tagline }),
        });

        if (!response.ok) {
            throw new Error("Failed to fetch playstyle data");
        }

        const data = await response.json();

        // Extracting and displaying the playstyle result
        const resultText = `${JSON.stringify(data)}`; // You can format this based on your backend response
        document.getElementById("result-text").innerText = resultText;

        // Hide the input form and show the result
        document.getElementById("input-form").style.display = "none";
        document.getElementById("playstyle-result").style.display = "block";
    } catch (error) {
        console.error("Error fetching playstyle:", error);
    }
});

function goBack() {
    // Hide the result and show the input form again
    document.getElementById("input-form").style.display = "block";
    document.getElementById("playstyle-result").style.display = "none";
}

form.addEventListener('submit', async function (event) {
    event.preventDefault();  // Prevent form from submitting normally

    const username = document.getElementById("username").value;
    const tagline = document.getElementById("tagline").value;

    console.log("Username:", username);
    console.log("Tagline:", tagline);

    const response = await fetch("/api/playstyle", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ username: username, tagline: tagline })
    });

    const result = await response.json();
    console.log(result);

    if (response.ok) {
        // Replace the page content with the result (or redirect to a new page)
        document.body.innerHTML = `<h1>Playstyle Result</h1><p>${result}</p><button onclick="window.location.href='/';">Go Back</button>`;
    } else {
        alert("Error: " + result.message);
    }
});
