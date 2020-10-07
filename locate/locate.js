window.addEventListener("DOMContentLoaded", function () {
    const srcTemplate = "https://iwillvote.com/locate/results?address=";
    const mapElement = document.querySelector("#iwillvote");
    const addressElement = document.querySelector("#address");
    const buttonElement = document.querySelector("#btn");
    const addressTextElement = document.querySelector("#addressText");

    buttonElement.onclick = function () {
      // Populate address text.
      const address = addressElement.value;
      addressTextElement.textContent = address;

      // Update map.
      const encodedAddress = encodeURIComponent(address);
      const newSrc = srcTemplate + encodedAddress;
      mapElement.src = newSrc;

      // Display results.
      mapElement.removeAttribute("style");
      addressTextElement.parentElement.removeAttribute("style");
    };
  });
