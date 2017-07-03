import jQuery from "jquery";
import "jquery-hotkeys";


(function($) {

var current=null;
var hovered=null;

$("#text span").on("click",function(e) {
    var $e=$(this);
    $e.toggleClass("selected");
    current=$e;
});

$("#text span").on("mouseover",function(e) {
    if (hovered != null) {
        hovered.removeClass("hovered");
    }
    hovered=$(this);
    hovered.addClass("hovered");
});

$(document).bind('keydown', 'right', function() {
    if (hovered != null) {
        hovered.removeClass("hovered");
    }
    hovered=$(hovered.next());
    hovered.addClass("hovered");
});

$(document).bind('keydown', 'left', function() {
    if (hovered != null) {
        hovered.removeClass("hovered");
    }
    hovered=$(hovered.prev());
    hovered.addClass("hovered");
});


$(document).bind('keydown', 'down', function(e) {
    var pos=hovered.position();
        pos.right=pos.left+(hovered.width()/2)
    var c=hovered;

    while ((typeof c.position() != typeof undefined) && (c.position().top == pos.top)){
        c=$(c.next());
    };
    var min=Math.abs(pos.right-(c.position().left+(c.width()/2)))
    while ((typeof c.position() != typeof undefined) && (min != null)) {
        var a=min;
        c=$(c.next());
        min=Math.abs(pos.right-(c.position().left+(c.width()/2)));
        if (min>a) {
            min=null;
        };
    };
    c=$(c.prev());
    if (typeof c.position() != typeof undefined) {
        if (hovered != null) {
            hovered.removeClass("hovered");
        }
        hovered=c;
        hovered.addClass("hovered");
        // hovered.scrollIntoView();
    }
    e.preventDefault();
});




$(document).bind('keydown', 'shift+right', function() {
    if (hovered != null) {
        hovered.toggleClass("selected");
    };
    hovered=$(hovered.next());
    hovered.addClass("hovered");
});

$(document).bind('keydown', 'space', function(e) {
    if (hovered != null) {
        hovered.toggleClass("selected");
    };
    e.preventDefault();
});


$(document).bind('keydown', 'shift+left', function(e) {
    if (hovered != null) {
        hovered.toggleClass("selected");
    };
    hovered=$(hovered.prev());
    hovered.addClass("hovered");
    e.preventDefault();
});


})(jQuery);
