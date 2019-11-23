n = 0
function do_it(){
    if( n++ % 2 == 0){
        console.log("Hey");
        document.getElementById("demo").innerHTML = "Hey";    
    } else {
        console.log("Hello");
        document.getElementById("demo").innerHTML = "Hello";    
    }
}