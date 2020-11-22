import redis
from . import settings.SETTINGS as s


class RedisDbContext:
    def __init__(self):
        self.context = redis.Redis(s["host"], s["port"], s["db"])

    def get(self, key):
        return context.get(key)

    def mset(self, **kwargs):
        return context.mset(kwargs)

    def set(self, key, value):
        return context.set(key, value)



    
