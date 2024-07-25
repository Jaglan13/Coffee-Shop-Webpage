document.getElementById('rating-form').addEventListener('submit', function(event) {
    event.preventDefault();
    var rating = document.querySelector('#stars .star.selected').getAttribute('data-value');
    var comment = document.getElementById('comment').value;

    // Simulate submitting the data to the backend
    // Replace this with your actual submission logic

    // Show a dialog box confirming submission
    var dialogBox = document.createElement('div');
    dialogBox.className = 'dialog-box';
    dialogBox.innerHTML = 'Rating: ' + rating + '<br>Comment: ' + comment;
    this.appendChild(dialogBox);

    // Clear the form after submission
    document.querySelectorAll('#stars .star.selected').forEach(function(star) {
        star.classList.remove('selected');
    });
    document.getElementById('comment').value = '';

    // Close the dialog box after a few seconds
    setTimeout(function() {
        dialogBox.style.opacity = '0';
        setTimeout(function() {
            dialogBox.parentNode.removeChild(dialogBox);
        }, 1000);
    }, 3000);
});

// Add event listeners to stars
document.querySelectorAll('#stars .star').forEach(function(star) {
    star.addEventListener('click', function() {
        document.querySelectorAll('#stars .star').forEach(function(s) {
            s.classList.remove('selected');
        });
        var value = parseInt(this.getAttribute('data-value'));
        for (var i = 0; i < value; i++) {
            document.querySelectorAll('#stars .star')[i].classList.add('selected');
        }
    });
});
