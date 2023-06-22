const scanButton = document.querySelector(".scanner-scan");
const statusIndicator = document.querySelector(".scanner-status");
const outputBox = document.querySelector(".scanner-output");

scanButton.addEventListener("click", function() {
  // Simulate scanning a fingerprint
  statusIndicator.style.backgroundColor = "#0f0";
  outputBox.innerText = "Fingerprint scanned successfully!";
  setTimeout(function() {
    statusIndicator.style.backgroundColor = "#f00";
    outputBox.innerText = "";
  }, 2000);
});