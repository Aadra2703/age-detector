document.getElementById("uploadForm").addEventListener("submit", async (event) => {
    event.preventDefault();  // Prevent form from refreshing the page

    const fileInput = document.getElementById("imageInput");
    const formData = new FormData();
    const file = fileInput.files[0];

    if (!file) {
        alert("Please choose an image file first!");
        return;
    }

    formData.append("file", file);

    try {
        // Send the form data to the backend for prediction
        const response = await fetch("/predict", {
            method: "POST",
            body: formData
        });

        const result = await response.json();
        document.getElementById("output").innerText = `Age: ${result.age}, Gender: ${result.gender}`;
    } catch (error) {
        console.error("Error:", error);
        document.getElementById("output").innerText = "Error in prediction.";
    }
});
