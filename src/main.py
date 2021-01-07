import RPi.GPIO as GPIO
from time import sleep
from car import Car
from motor import Motor

from flask import Flask, send_file
from flask_socketio import SocketIO

MOTOR_ENABLES = [7, 11]
MOTOR_PINS = [[8, 10], [13, 12]]


# if __name__ == "__main__":
#     # Initialize stuff
#     GPIO.setmode(GPIO.BOARD)
#     motors = [
#         Motor(pin_enable, pin_1, pin_2)
#         for (pin_enable, (pin_1, pin_2)) in zip(MOTOR_ENABLES, MOTOR_PINS)
#     ]

#     for motor in motors:
#         motor.move(50)
#     sleep(1)
#     for motor in motors:
#         motor.stop()

#     GPIO.cleanup()

app = Flask(__name__, static_url_path="/", static_folder="www")
socketio = SocketIO(app, async_mode="gevent_uwsgi")

GPIO.setmode(GPIO.BOARD)
car = Car(
    *(
        [
            Motor(pin_enable, pin_1, pin_2)
            for (pin_enable, (pin_1, pin_2)) in zip(MOTOR_ENABLES, MOTOR_PINS)
        ][::-1]
    )
)


@app.route("/")
def root():
    return send_file("www/index.html")


@socketio.on("setMovement")
def set_movement(data):
    car.set_vel(data["vel"])
    car.set_dir(data["dir"])


@socketio.on("enable")
def enable_movement(enable):
    if enable:
        car.start()
    else:
        car.stop()


if __name__ == "__main__":
    socketio.run(
        app,
        host="0.0.0.0",
        debug=True,
        # ssl_context=("ssl/certificate.pem", "ssl/key.pem"),
    )
