'use strict';

// Initialize the Image Classifier method with MobileNet
const classifier = ml5.imageClassifier('MobileNet', modelLoaded);

// When the model is loaded
function modelLoaded() {
    console.log('Model Loaded!');
}

// Put variables in global scope to make them available to the browser console.
const video = document.querySelector('video');
const canvas = window.canvas = document.querySelector('canvas');
canvas.width = 480;
canvas.height = 360;

const constraints = {
    audio: false,
    video: {
        facingMode: 'environment'
    }
};

function handleSuccess(stream) {
    window.stream = stream; // make stream available to browser console
    video.srcObject = stream;
}

function handleError(error) {
    console.log('navigator.MediaDevices.getUserMedia error: ', error.message, error.name);
}

function sendForm() {
    // Sends the form
    document.getElementById('display').classList.remove('fade');

    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;
    canvas.getContext('2d').drawImage(video, 0, 0, canvas.width, canvas.height);
    const imageUri = canvas.toDataURL("image/jpeg")
    document.getElementById('image').src = imageUri
    // Make a prediction with a selected image
    classifier.predict(document.getElementById('image'), function (err, results) {
        console.log(results[0].label.split(',')[0])

        var formData = new FormData()
        formData.append('word', results[0].label.split(',')[0])
    
        $.ajax({
            url: '/',
            data: formData,
            type: 'POST',
            contentType: false,
            processData: false,
            success: function (res) {
                document.getElementById('display').classList.add('fade');
                document.getElementById('display').innerHTML = res
                console.log(res)
            },
            error: function (error) {
                console.log(error)
            }
        });
    });

}

navigator.mediaDevices.getUserMedia(constraints).then(handleSuccess).catch(handleError);