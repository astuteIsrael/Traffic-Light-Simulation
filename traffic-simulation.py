import time

class TrafficLight:
    def __init__(self, cycles=3):
        self.state = "Red"
        self.cycles = cycles

    def change_to_green(self):
        self.state = "Green"
        print("Light changed to Green. Go!")
        time.sleep(5)

    def change_to_yellow(self):
        self.state = "Yellow"
        print("Light changed to Yellow. Slow down!")
        time.sleep(2)

    def change_to_red(self):
        self.state = "Red"
        print("Light changed to Red. Stop!")
        time.sleep(5)

    def run(self):
        cycle_count = 0
        while cycle_count < self.cycles:
            self.change_to_green()
            self.change_to_yellow()
            self.change_to_red()
            cycle_count += 1
        print("Traffic light sequence completed.")


if __name__ == "__main__":
    traffic_light = TrafficLight(cycles=3)
    traffic_light.run()
