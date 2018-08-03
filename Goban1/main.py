from ChessBoard import *
from ChessMan import *
from Engine import *
from chessmanthread import *
from gothread import *



def test1():
	chessboard = ChessBoard()
	chessboard.init_board()
	chessboard.print_board()

def test2():
	chessboard = ChessBoard()
	chessboard.init_board()
	#在10,8位置上放置黑棋
	chessboard.set_chess((10,8), 'x')
	#创建一个棋子对象 颜色为白棋 位置为4,7
	chessman = ChessMan()
	chessman.set_pos((4,7))
	chessman.set_color('o')
	chessboard.set_chessman(chessman)
	chessboard.print_board()

#测试电脑下棋
def test3():
	chessboard = ChessBoard()
	chessboard.init_board()
	#创建Engine对象
	engine = Engine(chessboard)
	#创建chessMan对象 并写入棋子颜色
	chessman = ChessMan()
	chessman.set_color('o')
	engine.computer_go(chessman)#方法中填入位置
	#把该棋子对象放置到棋盘上
	chessboard.set_chessman(chessman)
	#打印棋盘
	chessboard.print_board()

#测试棋手下棋
def test4():
	chessboard = ChessBoard()
	chessboard.init_board()
	engine = Engine(chessboard)
	#创建chessMan对象 并写入棋子颜色
	chessman = ChessMan()
	chessman.set_color('x')
	input = '13,b'
	engine.parse_uesr_input(input, chessman)
	#把该棋子对象放置到棋盘上
	chessboard.set_chessman(chessman)
	#打印棋盘
	chessboard.print_board()


def test5():
	chessboard = ChessBoard()
	chessboard.init_board()
	#创建Engine对象
	engine = Engine(chessboard)
	#垂直方向判断
	chessboard.set_chess((3,5), 'x')
	chessboard.set_chess((4,5), 'x')
	chessboard.set_chess((5,5), 'x')
	chessboard.set_chess((6,5), 'x')
	#chessboard.set_chess((7,5), 'x')
	chessboard.set_chess((8,5), 'x')
	chessboard.set_chess((9,5), 'x')
	chessboard.set_chess((10,5), 'x')
	chessboard.set_chess((11,5), 'x')
	chessboard.set_chess((12,5), 'x')
	#打印棋盘
	chessboard.print_board()
	ret = engine.is_won((8,5), 'x')

	#水平方向判断
	chessboard.set_chess((5,4), 'x')
	chessboard.set_chess((5,5), 'x')
	chessboard.set_chess((5,6), 'x')
	chessboard.set_chess((5,7), 'x')
	#chessboard.set_chess((5,8), 'x')
	chessboard.set_chess((5,9), 'x')
	chessboard.set_chess((5,10), 'x')
	chessboard.set_chess((5,11), 'x')
	chessboard.set_chess((5,12), 'x')
	chessboard.set_chess((5,13), 'x')

	#打印棋盘
	chessboard.print_board()
	ret = engine.is_won((5,12), 'x')
	print(ret)

	chessman = ChessMan()
	chessman.set_color('x')
	chessman.set_pos((5,9))
	ret = engine.is_woman(chessman)
	print(ret)


def test6():
	chessboard = ChessBoard()
	engine = Engine(chessboard)
	chessboard.init_board()
	chessboard.set_chess((8, 5), 'x')
	chessboard.set_chess((9,5), 'x')
	chessboard.set_chess((10,5), 'x')
	chessboard.set_chess((11,5), 'x')
	chessboard.set_chess((12,5), 'x')
	print(chessboard.get_board())
	ret = engine.is_Win(chessboard.get_board())
	chessboard.print_board()
	#print(chessboard.get_board())
	print(ret)

def main():
	#创建棋盘类
	chessboard = ChessBoard()
	#创建
	chessman = ChessMan() #人的棋子
	chesscomputer = ChessMan() #电脑的棋子
	#创建Engine对象
	engine = Engine(chessboard)
	#开始游戏
	engine.play(chessboard, chessman,chesscomputer)

def mainThread():
	#创建棋盘对象 并初始化
	chessboard = ChessBoard()
	chessboard.init_board()
	print('初始化棋盘如下：')
	chessboard.print_board()
	#创建策略类对象 并初始化
	engine = Engine(chessboard)
	#创建两个棋子线程对象
	chessman = ChessManThread()
	chessman.set_color('x')
	chesspc = ChessManThread()
	chesspc.set_color('o')

	#创建用户线程对象
	userthread = UserThread(engine, chessman)

	userthread.start()


	#创建电脑线程对象 并启动
	computerthread = PcThread(engine,chesspc)
	computerthread.setDaemon(True)
	computerthread.start()

	while True:
		#用户wait
		chessman.do_wait()
		#在棋盘上摆放棋子
		engine.parse_uesr_input(userthread.user_input, chessman)
		chessboard.set_chessman(chessman)
		print('此时棋盘如下')
		chessboard.print_board()
		result = engine.is_Win(chessboard.get_board())
		if result == True:
			break
		# 电脑notify
		chesspc.do_notify()
		# 电脑wait
		chesspc.do_wait()
		# 在棋盘上摆放棋子

		chessboard.set_chessman(chesspc)
		chessboard.print_board()
		result = engine.is_Win(chessboard.get_board())
		if result == True:
			break
		#用户notify
		chessman.do_notify()

if __name__ == '__main__':
	#test1()
	#test2()
	#test3()
	#test4()
	#test5()
	#test6()
	#main()
	mainThread()




























































