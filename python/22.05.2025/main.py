print("nya")

import threading, time

class newThread(threading.Thread):
    def __init__(self, threadName, sleepTime):
        threading.Thread.__init__(self)
        self.threadName = threadName
        self.sleepTime = sleepTime
        
    def run(self):
        num = 0
        while num < 6:
            localtime = time.localtime()
            info = time.strftime("%I:%M:%S", localtime)
            print(self.threadName, num, info)
            time.sleep(self.sleepTime)
            num+=1
            if num == 4: break
        print(self.threadName, "ended.")
thr1 = newThread("thread1", 0.5)
thr2 = newThread("thread2", 0.3)

thr1.start()
thr1.join()

thr2.start()
thr2.join()