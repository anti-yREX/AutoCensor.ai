function call(message){
    $.ajax({
        url: "http://localhost:5000/api/",
        type: "POST",
        contentType: "application/json",
        data: JSON.stringify({"message": message})
    }).done(function(data){
        obj = data
        document.getElementById("demo").innerHTML = obj["message"];
    })
}
function send_filename(){
    m = document.getElementById("fn").value;
    console.log(m);
    call(m);
}