import time

from . import cacher

while True:
    print("update")
    if cacher.cache.is_old():
        cacher.cache.update()
    time.sleep(cacher.cache.ttl)