document.addEventListener('DOMContentLoaded', function() {

    const isbn = document.getElementById('isbn').innerHTML;

    fetch(`http://cors-anywhere.herokuapp.com/https://www.goodreads.com/book/review_counts.json?isbns=${isbn}&key=gT9afGYzdoskLjqMgUmUg`)
    .then(response => response.json())
    .then(data => {
        document.getElementById('average_rating').innerHTML = `Average rating: ${data.books[0].average_rating}`
        document.getElementById('reviews_count').innerHTML = `Review Count ${data.books[0].reviews_count}`
    })
});