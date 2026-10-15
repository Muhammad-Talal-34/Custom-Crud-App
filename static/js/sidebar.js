document.addEventListener("DOMContentLoaded", () => {
    // Select the sidebar and the toggler button using your actual HTML classes
    const sidebar = document.querySelector('.sidebar');
    const togglerBtn = document.querySelector('.sidebar-toggler');

    // Add click event to toggle the 'collapsed' class
    if (togglerBtn && sidebar) {
        togglerBtn.addEventListener("click", () => {
            sidebar.classList.toggle("collapsed");
        });
    }

    // Optional: Add logic for dropdown menus (nav-group)
    const navGroups = document.querySelectorAll('.nav-group-toggle');
    navGroups.forEach(group => {
        group.addEventListener('click', (e) => {
            e.preventDefault();
            // Toggle the 'show' class on the parent 'li'
            group.parentElement.classList.toggle('show');
        });
    });
});