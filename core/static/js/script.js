document.addEventListener('DOMContentLoaded', function () {
    const items = document.querySelectorAll('li');
    items.forEach(function (item) {
        item.addEventListener('click', function () {
            alert("You clicked on: " + item.querySelector('.name').textContent);
        });
    });
});
