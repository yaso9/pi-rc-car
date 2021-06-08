# Pi RC Car
Pi RC Car is a remote control car with a live camera built on a Raspberry Pi single board computer.

## Usage
A web interface is used to control the car with a phone. The tilt of the phone is used to control the speed and direction of the car. A live video stream from the camera on the car is streamed to the phone.

## How It Works
The server on the Pi handles serving the controller web page. When the user is on the web page, starts the car, and tilts their phone, the phone sends a message to the server using web sockets. The server then appropriately controls the motors.

The video stream is served by an Nginx HLS (HTTP Live Streaming) server. When the car starts, FFmpeg is launched and begins streaming to the Nginx HLS server. The controller web page then streams the live stream from the Nginx HLS server.
