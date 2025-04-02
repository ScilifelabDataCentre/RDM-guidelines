/*  Adds functionality to copy-to-clipboard buttons which sit above each code/citation block.
Adapted from https://logfetch.com/hugo-add-copy-to-clipboard-button/
*/

const clipboard = navigator.clipboard;

// on click swap the copy button with the copied button for a few seconds
const handleButtonClick = (copyButton, copiedButton, codeBlock) => {
    clipboard.writeText(codeBlock.innerText).then(
        () => {
            copyButton.style.display = 'none';
            copiedButton.style.display = 'inline-block';
            setTimeout(() => {
                copyButton.style.display = 'inline-block';
                copiedButton.style.display = 'none';
            }, 2000);
        },
        (error) => {
            console.error("Clipboard write failed", error);
            copyButton.innerText = "Error";
        }
    );
};


// attach event listeners to the existing clipboard buttons
const attachClipboardListeners = () => {
    document.querySelectorAll(".clipboard").forEach((clipboardContainer) => {
        const copyButton = clipboardContainer.querySelector('.copy-button');
        const copiedButton = clipboardContainer.querySelector('.copied-button');
        const codeBlock = clipboardContainer.nextElementSibling.querySelector('code');

        copyButton.addEventListener('click', () => handleButtonClick(copyButton, copiedButton, codeBlock));
    });
};

document.addEventListener("DOMContentLoaded", () => {
    attachClipboardListeners();
});