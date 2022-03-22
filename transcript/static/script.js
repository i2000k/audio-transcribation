const audio = document.getElementById("audio");
const fileInput = document.getElementById("fileInput");
const source = document.getElementById("source");
const transcribateBtn = document.getElementById("transcribateBtn");
const transcribateText = document.getElementById("transcribateText");

let file;

fileInput.addEventListener("change", handleUpload, false);

function handleUpload(event) {
  file = event.target.files[0];
  source.setAttribute("src", URL.createObjectURL(file));
  audio.load();
}

form.addEventListener("submit", (event) => {
  event.preventDefault();
  const formData = new FormData();
  formData.append("filename", file.name);
  formData.append("file", file);

  fetch("http://127.0.0.1:8000/get_transcribation", {
    method: "post",
    body: formData,
  })
    .then((response) => response.json())
    .then((data) => (transcribateText.innerText = data.text))
    .catch((error) => ("error occured", error));
});
