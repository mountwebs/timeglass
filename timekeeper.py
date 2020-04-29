import time
from datetime import timedelta

class Timer():
    def __init__(self,seconds):
        self.initial = seconds
        self.remaining = seconds
        self.elapsed = 0
        self.pause = False
        self.done = False
        self.active = False
        self.last_tick = time.time()

    def get_remaining_string(self):
        conversion = timedelta(seconds=self.remaining)
        return str(conversion) 

    def start(self):
        self.active = True
        self.pause = False
        self.done = False
        self.last_tick = time.time()

    def pause(self):
        self.active = False
        self.pause = True

    def tick(self):
        if self.active and not self.done:
            now = time.time()
            if now - self.last_tick >= 1:
                seconds = int(now - self.last_tick)
                self.elapsed += seconds
                self.remaining -= seconds
                self.last_tick = now
                return True

        if self.remaining <= 0 and self.active:
            self.remaining = 0
            self.done = True
            self.active = False
        return False

    def set_time(self, seconds):
        self.initial = seconds
        self.reset()

    def reset(self):
        self.done = False
        self.active = False
        self.elapsed = 0
        self.remaining = self.initial

