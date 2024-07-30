$(".inputTxt").bind("keypress keyup keydown", function (event) {
    var evtType = event.type;
    var eWhich = event.which;
    var echarCode = event.charCode;
    var ekeyCode = event.keyCode;

    switch (evtType) {
        case 'keypress':
            $("#log").html($("#log").html() + "<b>" + evtType + "</b>" + " keycode: " + ekeyCode + " charcode: " + echarCode + " which: " + eWhich + "<br>");
            break;
        case 'keyup':
            $("#log").html($("#log").html() + "<b>" + evtType + "</b>" + " keycode: " + ekeyCode + " charcode: " + echarCode + " which: " + eWhich + "<p>");
            break;
        case 'keydown':
            $("#log").html($("#log").html() + "<b>" + evtType + "</b>" + " keycode: " + ekeyCode + " charcode: " + echarCode + " which: " + eWhich + "<br>");
            break;
        default:
            break;
    }
});


// The rough code of backspace event key.
note.addEventListener('keydown', function(event) {
    const key = event.key; // const {key} = event; ES6+
    if (key === "Backspace") {
        // Do something
    }
});


//The second rough code 
var keys = {};

$('input').keydown(function (e) {
    keys[e.which] = true;
});

$('input').keyup(function (e) {        
    getKeys();
    delete keys[e.which];    
});

function getKeys() {    
   if(keys[8]) {
        alert('bakspace pressed');
    }else if(keys[17] && keys[18] && keys[48]) {
        alert('@ pressed');
    }else if(keys[17] && keys[18] && keys[51]) {
        alert('# pressed');
    }    
}
