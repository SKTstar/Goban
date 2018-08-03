#author:caofeng
#Time:2018/8/3/003 18:06
import threading

class UserThread(threading.Thread):
    def __init__(self,engine, chessman):
        super().__init__()
        self.engine = engine
        self.chessman = chessman
        self.user_input = ''

    def run(self):
        while True:
            # 1 在终端输入坐标
            print('请输入坐标：')
            user_input = input('>')
            self.user_input = user_input
            #2 用户notify
            self.chessman.do_notify()
            # 3 用户wait
            self.chessman.do_wait()

class PcThread(threading.Thread):
    def __init__(self, engine, chesspc):
        super().__init__()
        self.engine = engine
        self.chesspc = chesspc

    def  run(self):
        while True:
            # 1 电脑wait
            self.chesspc.do_wait()
            # 2 电脑下棋
            self.engine.computer_go(self.chesspc)
            # 3 电脑notify
            self.chesspc.do_notify()
