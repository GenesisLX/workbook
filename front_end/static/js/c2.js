const button_delete_all = document.querySelector("[type='delete_all']")
const input_blocks = document.querySelectorAll("[class='input_value_tasks']")

console.log(button_delete_all)



button_delete_all.addEventListener("click", function() {
    console.log("Кнопка нажата. А теперь попробуй подключить к ней функционал! Это ужас.")
})

// 2 вар.
// button_delete_all.addEventListener("click", function(event) {
//         input_blocks.forEach(function (item) {
//             console.log(item)
//             item.setAttribute(value, 0)
//     })
// })




// buttons_delete_all.forEach(function(item){
//     item.addEventListener("click", function(){
//         this.nextElementSibling.setAttribute(value, this.nextElementSibling.getAttribute(value)-1);
//                                             })
// })



// button_delete_all.forEach(function(item) {
//     item.addEventListener("click", function() {
//         input_blocks.forEach(function (item) {
//             item.setAttribute(value, 0)
//         })
//     })
// })
