function checkInput() {
    if (document.querySelector('#password').value.length === 0 || document.querySelector('#username').value.length === 0)
    {
        document.querySelector('#login').disabled = true
    }
    else
    {
        document.querySelector('#login').disabled = false
    }
};

document.addEventListener("DOMContentLoaded", function() {

    checkInput();

    document.querySelector('#username').onkeyup = () => {
        checkInput()
    };

    document.querySelector('#password').onkeyup = () => {
        checkInput()
    };
});