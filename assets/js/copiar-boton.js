document.addEventListener("DOMContentLoaded", function () {
    const copyButtons = document.querySelectorAll(".copy-button");
  
    copyButtons.forEach(function (copyButton) {
      copyButton.addEventListener("click", function () {
        const codeElement = this.previousElementSibling.querySelector("code");
        const textToCopy = codeElement.textContent;
  
        const textArea = document.createElement("textarea");
        textArea.value = textToCopy;
        document.body.appendChild(textArea);
        textArea.select();
  
        document.execCommand("copy");
        document.body.removeChild(textArea);
  
        this.textContent = "Copiado";
  
        setTimeout(() => {
          this.textContent = "Copiar";
        }, 3000);
      });
    });
  });
  