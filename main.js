//jshint esversion: 6
let original_audio;
function dropHandler(ev) {
    console.log('File(s) dropped');
  
    // Prevent default behavior (Prevent file from being opened)
    ev.preventDefault();
  
    if (ev.dataTransfer.items) {
      // Use DataTransferItemList interface to access the file(s)
      for (let i = 0; i < ev.dataTransfer.items.length; i++) {
        // If dropped items aren't files, reject them
        if (ev.dataTransfer.items[i].kind === 'file') {
          var file = ev.dataTransfer.items[i].getAsFile();
            console.log('... file[' + i + '].name = ' + file.name);
          document.getElementById('audio_name').textContent = file.name;
          original_audio = file.name;
          console.log(file.name);
          call(file.name);
        }
      }
    } else {
      // Use DataTransfer interface to access the file(s)
      for (let i = 0; i < ev.dataTransfer.files.length; i++) {
        console.log('... file[' + i + '].name = ' + ev.dataTransfer.files[i].name);
      }
  }
  let hiddenElemennts = document.querySelectorAll('.hide-on-drop');
  hiddenElemennts.forEach((element) => { 
    element.classList.add('hide');
  });

  document.querySelector('.show-on-drop').classList.remove('hide');
}
  
function dragOverHandler(ev) {
    console.log('File(s) in drop zone'); 
    ev.preventDefault();
}

function call(message){
  $.ajax({
      url: "http://localhost:5000/api/",
      type: "POST",
      contentType: "application/json",
      data: JSON.stringify({"message": message})
  }).done(function (data) {
      document.getElementById("original_audio").src = `audios/${original_audio}`;
      document.getElementById("censored_audio").src = data.message;
  })
}