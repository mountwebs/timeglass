import rumps
import sys
import icon_manager
from datetime import timedelta
import timekeeper
import os

rumps.debug_mode(True)

class TimerApp(rumps.App):
    def __init__(self, initial_seconds):
        super(TimerApp, self).__init__("")

        self.mode = "hourglass"

        self.timekeeper = timekeeper.Timer(initial_seconds)

        self.im = icon_manager.Icon_manager(initial_seconds)
        self.change_icon()        
        
        self.remaining_sec = rumps.MenuItem(self.timekeeper.get_remaining_string())
        self.menu = [self.remaining_sec]
        self.next_icon_change = self.im.icon_interval

        self.rumps_timer = rumps.Timer(self.tick,0.5)
        self.rumps_timer.callback(self.tick)

    def change_icon(self):
        #self.im.draw_icon(frame)
        print("frame:", self.im.icon_counter)
        if self.mode == "hourglass":
            self.icon = self.im.get_icon_path()
        elif self.mode == "hoursquares":
            self.icon = self.im.draw_squares(self.timekeeper.initial,
                                             self.timekeeper.remaining)



    def change_remaining(self):
        self.remaining_sec.title = self.timekeeper.get_remaining_string()


    def tick(self, _):
        if self.timekeeper.tick():
            self.change_remaining()
            if self.timekeeper.elapsed >= self.next_icon_change:
                self.im.icon_counter = int(self.timekeeper.elapsed/self.im.icon_interval) + 1 #1-89
                self.change_icon()
                self.next_icon_change += self.im.icon_interval

                print(self.timekeeper.elapsed)
                print(self.timekeeper.elapsed/self.im.icon_interval)
                print(int(self.timekeeper.elapsed/self.im.icon_interval))

        if self.timekeeper.done:
            self.im.active = False
            self.change_icon()
            self.rumps_timer.stop()

    @rumps.clicked("Start")
    def pause(self, sender):
        if sender.title == "Pause":
            self.timekeeper.pause = True
            self.timekeeper.active = False

            self.rumps_timer.stop()
            sender.title = "Start"
        elif sender.title == "Start":
            self.timekeeper.start()
            self.im.active = True
            self.change_icon()
            self.rumps_timer.start()
            sender.title = "Pause"

    @rumps.clicked("Reset")
    def reset_button(self, sender):
        self.reset()
        self.menu["Start"].title = "Start"

    def reset(self):
        self.timekeeper.reset()
        self.rumps_timer.stop()
        
        self.im.active = False
        self.im.reset()
        self.change_icon()
        
        self.change_remaining()
        self.next_icon_change = self.im.icon_interval


    @rumps.clicked("Set time")
    def set_time(self, _):
        response = rumps.Window("Enter time, (ex. 25:00 = 25 minutes)").run()
        if response.clicked:
            if ":" in response.text:
                time_input = response.text.split(":")
                seconds = (int(time_input[0]) * 60) + int(time_input[1])
            else: 
                seconds = int(response.text)
            #except: print("Wrong input")
            self.rumps_timer.stop()
            self.timekeeper.set_time(seconds)
            
            #self.im.icon_interval = seconds / self.im.icon_steps
            self.im.set_icon_interval(seconds)
            self.im.reset()
            self.im.active = False
            self.next_icon_change = self.im.icon_interval
            self.change_icon()
            
            self.change_remaining()
            self.menu["Start"].title = "Start"


if __name__ == "__main__":
    default_secounds = 60 * 45
    TimerApp(default_secounds).run()

