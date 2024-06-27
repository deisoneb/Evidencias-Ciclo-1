
// Detectar el final del scroll
window.addEventListener('scroll', () => {
    if (window.innerHeight + window.scrollY >= document.body.offsetHeight) {
        window.scrollTo(0,0)
    }
});
