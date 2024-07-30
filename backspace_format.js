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
