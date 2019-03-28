from myredis import myredis
import time
from my_thread import mythread

delay_queue_name = "delay_queue"


class delay_queue(myredis):
    def __init__(self, queuename, consumer_work):
        super().__init__()
        self.queuename = queuename
        self.consumer_work = consumer_work

    def producer(self, deley_time, data):
        client = self.get_redis_conne()
        client.zadd(delay_queue_name, deley_time, data)

    def consumer(self):
        client = self.get_redis_conne()
        while True:
            value = client.zrangebyscore(self.queuename, 0, time.time(), start=0, num=1)
            if not value:
                print("sleep 1s")
                time.sleep(1)
                continue
            value = value[0]
            success = client.zrem(delay_queue_name, value)
            if success:
                self.consumer_work(value)


if __name__ == '__main__':
    delay_queue1 = delay_queue(delay_queue_name, lambda value: print(value))
    mythread("thread1", lambda: delay_queue1.producer(time.time() + 5, "Hello World")).start()
    thread2 = mythread("thread1", lambda: delay_queue1.consumer())
    thread2.start()
    thread2.join()
