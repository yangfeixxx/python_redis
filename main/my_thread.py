import threading


class mythread(threading.Thread):
    def __init__(self, thread_name, work):
        threading.Thread.__init__(self)
        self.thread_name = thread_name
        self.work = work

    def run(self) -> None:
        self.work()
