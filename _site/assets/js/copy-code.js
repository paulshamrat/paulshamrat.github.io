document.addEventListener('DOMContentLoaded', () => {
    const codeBlocks = document.querySelectorAll('pre');

    codeBlocks.forEach((block) => {
        // Create wrapper to handle relative positioning of the button
        const wrapper = document.createElement('div');
        wrapper.className = 'code-wrapper';
        wrapper.style.position = 'relative';

        // Insert wrapper before the pre block, then move pre inside wrapper
        block.parentNode.insertBefore(wrapper, block);
        wrapper.appendChild(block);

        // Create the copy button
        const button = document.createElement('button');
        button.className = 'copy-code-button';
        button.type = 'button';
        button.innerHTML = '<i class="fa-regular fa-copy"></i>';
        button.setAttribute('aria-label', 'Copy code to clipboard');

        wrapper.appendChild(button);

        button.addEventListener('click', () => {
            const code = block.querySelector('code') || block;
            const text = code.innerText.trim();

            navigator.clipboard.writeText(text).then(() => {
                // Success feedback
                button.innerHTML = '<i class="fa-solid fa-check"></i>';
                button.classList.add('copied');

                setTimeout(() => {
                    button.innerHTML = '<i class="fa-regular fa-copy"></i>';
                    button.classList.remove('copied');
                }, 2000);
            }).catch((err) => {
                console.error('Failed to copy: ', err);
                button.innerHTML = '<i class="fa-solid fa-xmark"></i>';
                setTimeout(() => {
                    button.innerHTML = '<i class="fa-regular fa-copy"></i>';
                }, 2000);
            });
        });
    });
});
