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
        self.start_time = None
        self.elapsed_at_pause = 0

    def get_remaining_string(self):
        conversion = timedelta(seconds=int(self.remaining))
        return str(conversion) 

    def start(self):
        self.active = True
        self.pause = False
        self.done = False
        self.last_tick = time.time()
        self.start_time = time.time()

    def pause_timer(self):
        self.active = False
        self.pause = True
        self.elapsed_at_pause = self.elapsed

    def tick(self):
        if self.remaining <= 0 and self.active:
            self.remaining = 0
            self.done = True
            self.active = False
        elif self.active and not self.done:
            now = time.time()
            self.elapsed = now - self.start_time + self.elapsed_at_pause
            self.remaining = self.initial - self.elapsed
            return True
        return False

    def set_time(self, seconds):
        self.initial = seconds
        self.reset()

    def reset(self):
        self.done = False
        self.active = False
        self.elapsed = 0
        self.remaining = self.initial

    def __str__(self):
        return(f"remaining: {self.remaining}, elapsed: {self.elapsed}")

