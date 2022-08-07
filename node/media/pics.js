    let submit = document.querySelector(".bakici");
    let username = document.querySelector(".username");
    let password = document.querySelector(".password");

    username.addEventListener('change',
    function username_(){
        if (username.value.length > 5 && password.value.length > 5){
            console.log(username.value)
            submit.style.backgroundColor = "rgb(3, 131, 243)"
        }    
    })
    password.addEventListener('change',
    function password_(){
        if (username.value.length > 5 && password.value.length > 5){
            console.log(password.value)
            submit.style.backgroundColor = "rgb(3, 131, 243)"
        }    
    })
    

  
    eklenecek_div = document.querySelector('.foto-ekle');
    var eklemelik_div = `<div class="V64Sp fade-in-image"><img alt="" class="RP4i1 JtrJi test" id="telefon_fotolari"src="pic1.png"
    style="width: 470px; margin-left: -190px; height: 610px; margin-top: -100px;object-fit: contain;  position:absolute;
    left:0;
    ">`
    div_sil = document.querySelector('.fade-in-image')
    eklenecek_div.innerHTML = eklemelik_div
    
    
    setTimeout(() => {
        var e = eklenecek_div.firstElementChild
        eklenecek_div.removeChild(e);
        console.log("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
        var eklemelik_div = `<div class="V64Sp fade-in-image"><img alt="" class="RP4i1 JtrJi test" id="telefon_fotolari"src="pic2.png"
    style="width: 470px; margin-left: -190px; height: 610px; margin-top: -100px;object-fit: contain;  position:absolute;
    left:0;
    ">`
    eklenecek_div.innerHTML = eklemelik_div
    ;
        }, 5000);
    
    
    
        setTimeout(() => {
            var eklemelik_div = `<div class="V64Sp fade-in-image"><img alt="" class="RP4i1 JtrJi test" id="telefon_fotolari"src="pic3.png"
    style="width: 470px; margin-left: -190px; height: 610px; margin-top: -100px;object-fit: contain;  position:absolute;
    left:0;
    ">`
    
    eklenecek_div.innerHTML = eklemelik_div
    ;
        }, 10000);
