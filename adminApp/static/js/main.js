let list=document.querySelectorAll(".navigation li");

function activelink(){
    list.forEach((item)=>{
        item.classList.remove("hovered");
    });
    this.classList.add("hovered");
}

list.forEach((item)=>item.addEventListener("mouseover",activelink));



let toggle = document.querySelector(".toggle");
let navigation = document.querySelector(".navigation");
let main = document.querySelector(".main");
let profile = document.querySelector(".profile-info");
let footerLogo = document.querySelector(".footer-logo");

toggle.onclick = function(){
    navigation.classList.toggle("active");
    main.classList.toggle("active");
    profile.classList.toggle("active");
    footerLogo.classList.toggle("active");
};


let onlineUser = document.querySelector(".online-user");

onlineUser.onclick = function(){
    if(main.classList.contains("expend")){
        main.classList.remove("expend");
    }else{
        main.classList.add("expend");
    }
   
}

let userDropdown=document.querySelector(".dropdown-toggle");
let dropMenu=document.querySelector(".dropdown-menu");


userDropdown.onclick=function(){
    if(userDropdown.classList.contains("show")){
        userDropdown.classList.remove("show")
        dropMenu.classList.remove("show")
    }else{
        userDropdown.classList.add("show")
        dropMenu.classList.add("show")
    }
}