document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('searchInput').addEventListener('input', function() {
        var input = this.value.toLowerCase();
        var cards = document.querySelectorAll('.card-container');
        cards.forEach(function(card) {
            var title = card.querySelector('.card-title').innerText.toLowerCase();
            if (title.includes(input)) {
                card.style.display = '';
            } else {
                card.style.display = 'none';
            }
        });
    });
});