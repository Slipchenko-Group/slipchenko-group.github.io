// custom.js

document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('.bibliography .title').forEach(function(element) {
        var url = element.dataset.url;
        if (url) {
            var link = document.createElement('a');
            link.href = url;
            link.textContent = element.textContent;
            element.textContent = '';
            element.appendChild(link);
        }
    });
});
