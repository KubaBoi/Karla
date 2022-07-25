var volume = 0;
var rec = false;
var silenceCounter = 0;
var byteBuffer = [];

navigator.mediaDevices.getUserMedia({
    audio: true
  })
    .then(function(stream) {
      const audioContext = new AudioContext();
      const analyser = audioContext.createAnalyser();
      const microphone = audioContext.createMediaStreamSource(stream);
      const scriptProcessor = audioContext.createScriptProcessor(2048, 1, 1);
  
      analyser.smoothingTimeConstant = 0.8;
      analyser.fftSize = 1024;
  
      microphone.connect(analyser);
      analyser.connect(scriptProcessor);
      scriptProcessor.connect(audioContext.destination);
      scriptProcessor.onaudioprocess = function() {
        const array = new Uint8Array(analyser.frequencyBinCount);
        analyser.getByteFrequencyData(array);
        const arraySum = array.reduce((a, value) => a + value, 0);
        const average = arraySum / array.length;

        volume = Math.round(average);

        if (volume >= 20 && !rec) {
            rec = true;
            silenceCounter = 0;
            start();
        }
        else if (rec) {
            byteBuffer.push(array);

            if (volume < 15) {
                silenceCounter++;
            }
            else {
                silenceCounter = 0;
            }

            if (silenceCounter > 20) {
                sendRecord();
            }
        }
      };
    })
    .catch(function(err) {
      /* handle the error */
      console.error(err);
    });

async function sendRecord() {
    rec = false;
    
    blob = stop();
    
    var response = await callEndpoint("POST", "/recognition/fromWav", blob);
    if (response.ERROR == null) {
        console.log(response);
    }
    else {
        showErrorAlert(response.ERROR, alertTime);
    }
}