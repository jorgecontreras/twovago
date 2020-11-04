
function reserve() {
    checkin = document.querySelector("#checkin").value;
    checkout = document.querySelector("#checkout").value;
    room_id = document.querySelector("#room_id").value;

    var ci = new Date(checkin);
    var co = new Date(checkout);

    fetch('/reserve/' + room_id, {
        method: "POST",
        body: JSON.stringify({
            checkin: ci.toISOString(),
            checkout: co.toISOString()
        })
    })
    .then(response => response.json())
    .then(result => {
        console.log(result.status)

        
        if(result.status == 'success'){
            document.querySelector("#room_info").innerHTML = '<div class="alert alert-success" role="alert">' + result.message + '</div>'
        } else {
            document.querySelector("#room_info").innerHTML = '<div class="alert alert-danger" role="alert">' + result.message + '</div>'
        }
    })
}

function cancel(reservation_id) {
    if (confirm("Are you sure you want to cancel this reservation?")) {

        fetch('/cancel/' + reservation_id, {
            method: "POST",
            body: ""
        })
        .then(response => response.json())
        .then(result => {
            if (result.status == 'success'){
                document.querySelector("#alert_info").innerHTML = '<div class="alert alert-success" role="alert">' + result.message + '</div>'
            } else {
                document.querySelector("#alert_info").innerHTML = '<div class="alert alert-danger" role="alert">' + result.message + '</div>'
            }
        })
        console.log("canceled: " + reservation_id)
    } else {
        console.log("nothing changed")
    }
}