import threading, time

class sumThread(threading.Thread):
    def __init__(self, threadName, sleepTime):
        threading.Thread.__init__(self)
        self.threadName = threadName
        # self.sleepTime = sleepTime
        
    def run(self):
        num=sum(range(1,26))
        print(num)
        print(self.threadName, "ended.")
        

thr1 = sumThread("thread1", 0.5)
thr1.start()
thr1.join()