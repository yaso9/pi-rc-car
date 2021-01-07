let vel = 0
let dir = 0
let enabled = false
let carBox

const gn = new GyroNorm();
const socket = io({transports: ['websocket']});

socket.on('image', image => {
  document.getElementById('car').src = image
})

gn.init({
  frequency: 100
}).then(() => {
  gn.start(data => {
    vel = 90 - data.do.beta
    dir = data.do.gamma

    carBox.style.backgroundColor = `#00${Math.round((0xFF / 90) * vel).toString(16)}00`
    document.getElementById('car').style.transform = `rotate(${dir - 90}deg)`

    if (enabled) {
      socket.emit('setMovement', {vel, dir})
    }
  });
});

document.addEventListener("DOMContentLoaded", () => {
  carBox = document.getElementById('car-box')

  carBox.addEventListener('touchstart', () => {
    enabled = true;
    socket.emit('enable', true)
  })
  
  carBox.addEventListener('touchend', () => {
    socket.emit('enable', false)
    enabled = false;
  })

  const videoEl = document.getElementsByTagName('hls-video')[0]
  videoEl.addEventListener('click', () => videoEl.play())
});
