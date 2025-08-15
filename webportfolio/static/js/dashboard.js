const hamburger = document.getElementById('hamburger');
const sidebar = document.getElementById('sidebar');

hamburger.addEventListener('click', () => {
    sidebar.classList.toggle('active');
    hamburger.classList.toggle('open');
});



document.getElementById('toggle-add-form').addEventListener('click', function(){
    const form = document.getElementById('add-project-form');
    form.classList.toggle('hidden');
});

