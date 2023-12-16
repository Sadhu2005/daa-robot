function loadHeaderAndFooter() {
    const headerPlaceholder = document.getElementById('header-placeholder');
    const footerPlaceholder = document.getElementById('footer-placeholder');

    // Fetch and insert header content
    fetch('header.html')
        .then(response => response.text())
        .then(data => {
            headerPlaceholder.innerHTML = data;
        });

    // Fetch and insert footer content
    fetch('footer.html')
        .then(response => response.text())
        .then(data => {
            footerPlaceholder.innerHTML = data;
        });
}

function goToNewPage() {
    // Redirect to a new page when the button is clicked
    window.location.href = 'newpage.html';
}

// Call function to load header and footer when the page loads
document.addEventListener('DOMContentLoaded', loadHeaderAndFooter);
