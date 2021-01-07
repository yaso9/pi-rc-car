import RPi.GPIO as GPIO


class Motor:
    def __init__(self, pin_enable, pin_1, pin_2):
        self.pin_enable = pin_enable
        self.pin_1 = pin_1
        self.pin_2 = pin_2

        GPIO.setup(pin_enable, GPIO.OUT)
        GPIO.setup(pin_1, GPIO.OUT)
        GPIO.setup(pin_2, GPIO.OUT)

        self.pwm = GPIO.PWM(pin_enable, 1000)

    def move(self, speed):
        GPIO.output(self.pin_1, GPIO.LOW)
        GPIO.output(self.pin_2, GPIO.HIGH)
        self.pwm.start(speed)

    def stop(self):
        GPIO.output(self.pin_enable, GPIO.LOW)
        GPIO.output(self.pin_1, GPIO.LOW)
        GPIO.output(self.pin_2, GPIO.LOW)
