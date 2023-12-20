
const headers_accordeon = document.querySelectorAll("[data-name='accordeon_title']")

headers_accordeon.forEach(function(item){
    item.addEventListener("click", function(){
        this.nextElementSibling.classList.toggle("accordeon_body");
        this.nextElementSibling.firstElementChild.setAttribute("style", null);
        // this.nextElementSibling.nextElementSibling.setAttribute("style", null);
    })
})
