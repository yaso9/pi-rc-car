class Car:
    def __init__(self, left_motor, right_motor):
        self.left_motor = left_motor
        self.right_motor = right_motor
        self.vel = 0
        self.dir = 0
        self.running = False

    def set_vel(self, vel):
        self.vel = vel
        if self.running:
            self.start()

    def set_dir(self, dir):
        self.dir = dir
        if self.running:
            self.start()

    def start(self):
        self.running = True
        ratio = self.dir / 90
        diff = ratio * 100

        left = min(100, max(0, self.vel + diff))
        right = min(100, max(0, self.vel - diff))

        self.left_motor.move(left)
        self.right_motor.move(right)

    def stop(self):
        self.left_motor.stop()
        self.right_motor.stop()
        self.running = False
