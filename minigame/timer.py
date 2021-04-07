"""A class for creating a timer widget."""
from kivy.clock import Clock
import kivy.properties as props
from kivy.uix.widget import Widget


class Timer(Widget):
    """Used to dynamically display the current time elapsed on the screen."""

    # initializes a timer with 0 seconds.
    timeText = props.NumericProperty(0)

    def __init__(self, **kwargs):
        super(Timer, self).__init__(**kwargs)

    # need dt to relate update of time to frames per second
    def update_time(self, dt):
        """Updates the time elapsed."""
        self.timeText += 1 * dt

    def reset_time(self):
        """Resets the time elapsed."""
        self.timeText = 0

    def start_time(self):
        # begins a clock interval running at 60 FPS calling update_time
        Clock.schedule_interval(self.update_time, 1.0 / 60.0)
