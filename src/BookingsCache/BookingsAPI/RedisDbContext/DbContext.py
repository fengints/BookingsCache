import redis
from .settings import SETTINGS as s


class RedisDbContext:
    def __init__(self):
        self.context = redis.Redis(s["host"], s["port"], s["db"])

    def get(self, key):
        return self.context.get(key)

    def mset(self, **kwargs):
        return self.context.mset(kwargs)

    def set(self, key, value):
        return self.context.set(key, value)



    
