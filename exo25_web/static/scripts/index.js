function formSubmit(event) {
    var url = event.target.action;
    var request = new XMLHttpRequest();
    request.open('POST', url, true);
    request.onload = function () { // request successful
        // we can use server response to our request now
        console.log(request.responseText);
    };

    request.onerror = function () {
        // request failed
    };

    request.send(new FormData(event.target)); // create FormData from form that triggered event
    event.preventDefault();
}

