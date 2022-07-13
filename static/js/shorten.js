shortenSubmit = document.getElementById('shorten-submit')
shortenForm = document.getElementById('shorten-form')
urlType = document.getElementById('urlType')
example = document.getElementById('example-url')


shortenForm.addEventListener('input', (e) => {
    let type = e.target.value;
    if (type === 'ltl-url') {
        example.textContent = 'https://ltl-url.herokuapp.com/ltl-url'
    } else if (type === '4Letters') {
        example.textContent = 'https://ltl-url.herokuapp.com/lahu'
    } else if (type === 'sillySentence') {
        example.textContent = 'https://ltl-url.herokuapp.com/89lazypandas'
    }
})
