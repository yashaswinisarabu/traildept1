var overlay = document.getElementById("overlay");

var r = document.getElementById("result1");
var speechRecognizer = new webkitSpeechRecognition(); // a new speech recognition object

//function to start listening to voice and then convert it to text
function startConverting() {
  if ("webkitSpeechRecognition" in window) {
    speechRecognizer.continuous = true;
    speechRecognizer.interimResults = true;
    speechRecognizer.lang = "en-IN";
    speechRecognizer.start();
    var finalTranscripts = "";
    speechRecognizer.onresult = function(event) {
      var interimTranscripts = "";
      for (var i = event.resultIndex; i < event.results.length; i++) {
        var transcript = event.results[i][0].transcript;
        transcript.replace("\n", "<br>");
        if (event.results[i].isFinal) {
          finalTranscripts += transcript;
        } else {
          interimTranscripts += transcript;
        }
      }
      r.value = finalTranscripts + interimTranscripts;
    };
    speechRecognizer.onerror = function(event) {};
  } else {
    r.innerHTML = "No browser support. Please upgrade your browser";
  }
}
//function to stop listening
function stopConverting() {
  speechRecognizer.stop();
}
