"user strict";

const mediaStreamConstraints = {
  video: true
};
const shareTrigger = document.getElementById('share_button')
const inviteTrigger = document.getElementById('invite_button')
const localVideo = document.querySelector("video");

function gotLocalMediaStream(mediaStream) {
  const localStream = mediaStream;
  localVideo.srcObject = mediaStream;
}

function handleLocalMediaStreamError(error) {
  console.log("navigator.getUserMedia error: ", error);
}

function copy() {
    const element = document.createElement('input');
    element.value = location.href;
    document.body.appendChild(element);
    element.select();
    document.execCommand('copy');
    document.body.removeChild(element);
    alert('Copy!')
}

// inviteTrigger.addEventListener('click', () => copy()
// )

shareTrigger.addEventListener('click', () =>
  navigator.mediaDevices
    .getDisplayMedia(mediaStreamConstraints)
    .then(gotLocalMediaStream)
    .catch(handleLocalMediaStreamError)
)

var url = location.href ;
console.log(url);

// navigator.mediaDevices
//   .getDisplayMedia(mediaStreamConstraints)
//   .then(gotLocalMediaStream)
//   .catch(handleLocalMediaStreamError);
