async function checkHealth() {
  const output = document.getElementById("status");
  output.textContent = "Checking...";
  try {
    const response = await fetch("/health");
    const data = await response.json();
    output.textContent = response.ok ? `Healthy — service: ${data.service}` : "Application check failed.";
  } catch (error) {
    output.textContent = "Could not reach the application.";
  }
}

async function loadStudent() {
  const output = document.getElementById("student-data");
  output.textContent = "Loading...";
  try {
    const response = await fetch("/api/student");
    const data = await response.json();
    output.textContent = JSON.stringify(data, null, 2);
  } catch (error) {
    output.textContent = "Could not load student service data.";
  }
}

document.getElementById("check-button").addEventListener("click", checkHealth);
document.getElementById("student-button").addEventListener("click", loadStudent);
checkHealth();
loadStudent();
