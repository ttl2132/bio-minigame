"""A class for creating a timer widget."""
from kivy.clock import Clock
import kivy.properties as props

class Timer():
    """Used to dynamically display the current time elapsed on the screen."""

    #initializes a timer with 100 seconds. Can replace 100 with any number or
    #reference variable

    timeText = 100

    def __init__(self, **kwargs):
        super(Timer, self).__init__(**kwargs)

    #need dt to relate update of time to frames per second
    def update_time(self, dt):
        """Updates the time elapsed."""
        self.timeText -= 1 * dt
        #uncomment this line to see timer is working but for some reason it is not being printed in kv reference
        #print(self.timeText)

    def reset_time(self):
        """Resets the time elapsed."""
        self.timeText = 100

    def start_time(self):
    	#begins a clock interval running at 60 FPS calling update_time
    	Clock.schedule_interval(self.update_time, 1.0 / 60.0)
