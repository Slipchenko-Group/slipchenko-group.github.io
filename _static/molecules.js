// _static/molecules.js

document.addEventListener('DOMContentLoaded', function() {
    const molecules = document.querySelectorAll('.molecule');
    molecules.forEach(molecule => {
        molecule.style.top = Math.random() * 100 + 'vh';
        molecule.style.left = Math.random() * 100 + 'vw';
    });
});

