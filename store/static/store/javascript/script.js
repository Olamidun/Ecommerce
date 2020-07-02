$(document).ready(function () {
    // FIXED NAVBAR
    $(".js--section-about").waypoint(function (direction) {
        if (direction === "down") {
            $(".js--nav").addClass("fixed")
        } else {
            $(".js--nav").removeClass("fixed")
        }
        
    },{
        offset:"60px"
    });
    // FIXED NAVBAR
    $(".js--section-billing").waypoint(function (direction) {
        if (direction === "down") {
            $(".js--nav").addClass("fixed")
        } else {
            $(".js--nav").removeClass("fixed")
        }
        
    },{
        offset:"60px"
    });




    // LINKING NAVS AND BUTTONS
    $(".link-home").click(function () {
        $("html, body").animate({scrollTop: $(".js--section-home").offset().top}, 1000)
    });
    $(".link-about").click(function () {
        $("html, body").animate({scrollTop: $(".js--section-about").offset().top}, 1000)
    });
    $(".link-offers").click(function () {
        $("html, body").animate({scrollTop: $(".js--section-offers").offset().top}, 1000)
    });
    $(".link-order").click(function () {
        $("html, body").animate({scrollTop: $(".js--section-order").offset().top}, 1000)
    });
    $(".link-products").click(function () {
        $("html, body").animate({scrollTop: $(".js--section-products").offset().top}, 1000)
    });
    $(".link-billing").click(function () {
        $("html, body").animate({scrollTop: $(".js--section-billing").offset().top}, 1000)
    });
    $(".link-contact").click(function () {
        $("html, body").animate({scrollTop: $(".js--section-contact").offset().top}, 1000)
    });

    // RESPONSIVE MENU ICONS 
    $(".js--menu-icon").click(function () {
        var menu = $(".js--menu-icon");
        if (menu.hasClass("ti-menu")) {
            menu.addClass("ti-close");
            menu.removeClass("ti-menu")
        }else {
            menu.addClass("ti-menu");
            menu.removeClass("ti-close")
        }
    });

    // ANIMATIONS ON SCROLL
    $(".js--anime-1").waypoint(function(direction){
        $(".js--anime-1").addClass("animated fadeIn")
    },{
        offset: "70%"
    });
    $(".js--anime-2").waypoint(function(direction){
        $(".js--anime-2").addClass("animated fadeInUp")
    },{
        offset: "70%"
    });
    $(".js--anime-3").waypoint(function(direction){
        $(".js--anime-3").addClass("animated fadeIn")
    },{
        offset: "50%"
    });
    $(".js--anime-4").waypoint(function(direction){
        $(".js--anime-4").addClass("animated fadeIn")
    },{
        offset: "70%"
    });
    $(".js--anime-5").waypoint(function(direction){
        $(".js--anime-5").addClass("animated fadeIn")
    },{
        offset: "90%"
    });
    $(".js--anime-6").waypoint(function(direction){
        $(".js--anime-6").addClass("animated fadeIn")
    },{
        offset: "70%"
    });
    $(".js--anime-7").waypoint(function(direction){
        $(".js--anime-7").addClass("animated fadeIn")
    },{
        offset: "70%"
    })

    // // INCREASE QUANTITY

    // $(".add").on("click", function(){
    //     $(".input").value++
    // })

    // $(".sub").on("click", function(){
    //     if ($(".input").value >= 1) {
    //         $(".input").value--
    //     }else {
    //         return false
    //     }
       
    // })

});

