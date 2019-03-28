from myredis import myredis
import time



class windows_limit(myredis):
    def __init__(self, limit_time, limit_count):
        myredis.__init__(self)
        self.limit_time = limit_time
        self.limit_count = limit_count

    def is_cross(self,key):
        client = self.get_redis_conne()
        with client.pipeline() as pipe:
            now_ts, limit_time = time.time() / 1000, self.limit_time
            pipe.zadd(key, now_ts, now_ts)
            pipe.zremrangebyscore(key, 0, now_ts - limit_time)
            pipe.zcard(key)
            pipe.expire(key, limit_time + 1)
            _, _, current_count, _ = pipe.execute()
            return current_count <= self.limit_count


if __name__ == '__main__':
    limit = windows_limit(60, 5)
    for i in range(20):
        print(limit.is_cross("limt"))
