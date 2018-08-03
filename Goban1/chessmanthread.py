#author:caofeng
#Time:2018/8/3/003 18:07
from ChessMan import *
import threading

class ChessManThread(ChessMan):
    #初始化 线程的状态
    def __init__(self):
        super().__init__()
        self.con = threading.Condition()

    def do_notify(self):
        self.con.acquire()
        self.con.notify()
        self.con.release()

    def do_wait(self):
        self.con.acquire()
        self.con.wait()
        self.con.release()


