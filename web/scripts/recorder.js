(async () => {
    let leftchannel = [];
    let rightchannel = [];
    let recorder = null;
    let recording = false;
    let recordingLength = 0;
    let volume = null;
    let audioInput = null;
    let sampleRate = null;
    let AudioContext = window.AudioContext || window.webkitAudioContext;
    let context = null;
    let analyser = null;
    let stream = null;
    let tested = false;
    let silenceCounter = 0;

    try {
        window.stream = stream = await getStream();
        console.log('Got stream');
    } catch (err) {
        alert('Issue getting mic', err);
    }

    const deviceInfos = await navigator.mediaDevices.enumerateDevices();

    var mics = [];
    for (let i = 0; i !== deviceInfos.length; ++i) {
        let deviceInfo = deviceInfos[i];
        if (deviceInfo.kind === 'audioinput') {
            mics.push(deviceInfo);
            let label = deviceInfo.label ||
                'Microphone ' + mics.length;
            console.log('Mic ', label + ' ' + deviceInfo.deviceId)
            const option = document.createElement('option')
            option.value = deviceInfo.deviceId;
            option.text = label;
        }
    }

    function getStream(constraints) {
        if (!constraints) {
            constraints = { audio: true, video: false };
        }
        return navigator.mediaDevices.getUserMedia(constraints);
    }


    setUpRecording();

    function setUpRecording() {
        context = new AudioContext();
        sampleRate = context.sampleRate;

        // creates a gain node
        volume = context.createGain();

        // creates an audio node from teh microphone incoming stream
        audioInput = context.createMediaStreamSource(stream);

        // Create analyser
        analyser = context.createAnalyser();

        // connect audio input to the analyser
        audioInput.connect(analyser);

        // connect analyser to the volume control
        // analyser.connect(volume);

        let bufferSize = 2048;
        let recorder = context.createScriptProcessor(bufferSize, 2, 2);

        // we connect the volume control to the processor
        // volume.connect(recorder);

        analyser.connect(recorder);

        // finally connect the processor to the output
        recorder.connect(context.destination);

        recorder.onaudioprocess = function (e) {
            // Check 
            const array = new Uint8Array(analyser.frequencyBinCount);
            analyser.getByteFrequencyData(array);
            const arraySum = array.reduce((a, value) => a + value, 0);
            const average = arraySum / array.length;
            volume = Math.round(average);

            if (volume >= 20 && !recording) {
                recording = true;
                silenceCounter = 0;
                start();
            }

            if (!recording) return;
            // Do something with the data, i.e Convert this to WAV
            console.log('recording');
            let left = e.inputBuffer.getChannelData(0);
            let right = e.inputBuffer.getChannelData(1);
            if (!tested) {
                tested = true;
                // if this reduces to 0 we are not getting any sound
                if (!left.reduce((a, b) => a + b)) {
                    alert("There seems to be an issue with your Mic");
                    // clean up;
                    stop();
                    stream.getTracks().forEach(function (track) {
                        track.stop();
                    });
                    context.close();
                }
            }
            // we clone the samples
            leftchannel.push(new Float32Array(left));
            rightchannel.push(new Float32Array(right));
            recordingLength += bufferSize;

            if (volume < 15) {
                silenceCounter++;
            }
            else {
                silenceCounter = 0;
            }

            if (silenceCounter > 20) {
                stop();
            }
        };
    };



    function mergeBuffers(channelBuffer, recordingLength) {
        let result = new Float32Array(recordingLength);
        let offset = 0;
        let lng = channelBuffer.length;
        for (let i = 0; i < lng; i++) {
            let buffer = channelBuffer[i];
            result.set(buffer, offset);
            offset += buffer.length;
        }
        return result;
    }

    function interleave(leftChannel, rightChannel) {
        let length = leftChannel.length + rightChannel.length;
        let result = new Float32Array(length);

        let inputIndex = 0;

        for (let index = 0; index < length;) {
            result[index++] = leftChannel[inputIndex];
            result[index++] = rightChannel[inputIndex];
            inputIndex++;
        }
        return result;
    }

    function writeUTFBytes(view, offset, string) {
        let lng = string.length;
        for (let i = 0; i < lng; i++) {
            view.setUint8(offset + i, string.charCodeAt(i));
        }
    }

    function start() {
        recording = true;
        // reset the buffers for the new recording
        leftchannel.length = rightchannel.length = 0;
        recordingLength = 0;
        console.log('context: ', !!context);
        if (!context) setUpRecording();
    }

    async function stop() {
        console.log('Stop')
        recording = false;


        // we flat the left and right channels down
        let leftBuffer = mergeBuffers(leftchannel, recordingLength);
        let rightBuffer = mergeBuffers(rightchannel, recordingLength);
        // we interleave both channels together
        let interleaved = interleave(leftBuffer, rightBuffer);

        ///////////// WAV Encode /////////////////
        // from http://typedarray.org/from-microphone-to-wav-with-getusermedia-and-web-audio/
        //

        // we create our wav file
        let buffer = new ArrayBuffer(44 + interleaved.length * 2);
        let view = new DataView(buffer);

        // RIFF chunk descriptor
        writeUTFBytes(view, 0, 'RIFF');
        view.setUint32(4, 44 + interleaved.length * 2, true);
        writeUTFBytes(view, 8, 'WAVE');
        // FMT sub-chunk
        writeUTFBytes(view, 12, 'fmt ');
        view.setUint32(16, 16, true);
        view.setUint16(20, 1, true);
        // stereo (2 channels)
        view.setUint16(22, 2, true);
        view.setUint32(24, sampleRate, true);
        view.setUint32(28, sampleRate * 4, true);
        view.setUint16(32, 4, true);
        view.setUint16(34, 16, true);
        // data sub-chunk
        writeUTFBytes(view, 36, 'data');
        view.setUint32(40, interleaved.length * 2, true);

        // write the PCM samples
        let lng = interleaved.length;
        let index = 44;
        let volume = 1;
        for (let i = 0; i < lng; i++) {
            view.setInt16(index, interleaved[i] * (0x7FFF * volume), true);
            index += 2;
        }

        // our final binary blob
        const blob = new Blob([view], { type: 'audio/wav' });

        let xmlHttp = new XMLHttpRequest();

        xmlHttp.onreadystatechange = function() {
            if (this.readyState == 4) {
                json = JSON.parse(this.responseText);
                console.log("RESPONSE", nowTime(), json);
                let aud = document.getElementById("player");
                aud.innerHTML = "";
                createElement("source", aud, "", [
                    {"name": "src", "value": json.ANSWER.replaceAll("\\", "/")},
                    {"name": "type", "value": "audio/mpeg"}
                ]);
                aud.currentTime = 0;
                aud.play();
            }
        };

        let formData = new FormData();
        formData.append("file", blob); 
        console.log(blob);

        xmlHttp.open("POST", "/recognition/fromWav");
        xmlHttp.send(formData);
    }
})()