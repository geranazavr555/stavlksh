from datetime import datetime
import time


class Cache:
    def __init__(self, time_to_live):
        self.func = None
        self.date = datetime.min
        self.ttl = time_to_live
        self.data = None
        self.args = None
        self.kwargs = None

        self.update()

    def __call__(self, *args, **kwargs):
        if self.is_old():
            self.update()
        return self.data

    def is_old(self):
        return (datetime.now() - self.date).total_seconds() > self.ttl or (self.data is None)

    def update(self):
        if self.func is None:
            return None

        try:
            self.data = self.func(*self.args, **self.kwargs)
            self.date = datetime.now()
        except Exception:
            pass

    def set_args(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    def set_function(self, function):
        self.func = function

cache = Cache(60)
