copyBtn = document.getElementById('copy-btn')

copyBtn.addEventListener('click', e => {
    url = document.getElementById('new-short-url').textContent
    navigator.clipboard.writeText(url)
})
