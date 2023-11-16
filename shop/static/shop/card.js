    if(localStorage.getItem("cart")==null){
        var cart = {};
    }
    else{
        cart = JSON.parse(localStorage.getItem("cart"));
    }
    
    
    document.addEventListener('DOMContentLoaded', function () {
        var addToCartButtons = document.querySelectorAll('.atc');

        addToCartButtons.forEach(function (button) {
            button.addEventListener('click', function (event) {
                var productId = event.target.id;

                if(cart[productId]!=undefined){
                    cart[productId] = cart[productId]+1;
                }else{
                    cart[productId] = 1;
                }
                localStorage.setItem('cart', JSON.stringify(cart));

                console.log(localStorage.getItem("cart"));
                document.getElementById("cart").innerHTML="Cart("+Object.keys(cart).length+")";
            });
        });
    });
    // Popover'ı oluştur
const popoverTriggerList = document.querySelectorAll('[data-bs-toggle="popover"]');
const popoverList = [...popoverTriggerList].map(popoverTriggerEl => new bootstrap.Popover(popoverTriggerEl));

// // Popover'ı tıklanabilir öğe üzerine ekle
// const popoverButton = document.querySelector('[data-bs-toggle="popover"]');
// popoverButton.addEventListener('click', function () {
//     // Yeni değeri belirle
//     const yeniPopoverIcerik = 'Yeni Değer';

//     // Popover'ı güncelle
//     const popoverInstance = bootstrap.Popover.getInstance(popoverButton);
//     if (popoverInstance) {
//         popoverInstance.config.content = yeniPopoverIcerik;
//         popoverInstance._setContent();

//         // Popover'ı göster
//         popoverInstance.show();
//     }
// });

   