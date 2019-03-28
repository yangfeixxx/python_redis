import time
from my_thread import mythread
from myredis import myredis

block_queue = "block_queue"


class redis_block_queue(myredis):

    def __init__(self):
        super().__init__()

    def block_producer(self, queue_name, data):
        time.sleep(2)
        clinet = self.get_redis_conne()
        clinet.lpush(queue_name, data)

    def block_consumer(self, queue_name):
        clinet = self.get_redis_conne()
        while True:
            try:
                data = clinet.brpop(queue_name)
                print(data[1])
            except:
                self.block_consumer(queue_name)


if __name__ == '__main__':
    block_queue = redis_block_queue()
    mythread("thread1", lambda: block_queue.block_producer(block_queue, "hahah")).start()
    thread2 = mythread("thread2", lambda: block_queue.block_consumer())
    thread2.start()
    thread2.join()
