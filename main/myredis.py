import redis


class myredis(object):
    def __init__(self):
        self.pool = redis.ConnectionPool(host='192.168.35.130', port=6379, db=0, decode_responses=True)

    def get_redis_conne(self):
        return redis.StrictRedis(connection_pool=self.pool)
