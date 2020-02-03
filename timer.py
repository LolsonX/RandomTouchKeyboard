from kivy.clock import Clock


class Timer(object):
    @staticmethod
    def start(callback: callable, interval: float):
        return Clock.schedule_interval(callback, interval)
