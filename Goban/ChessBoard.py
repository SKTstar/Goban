
from ChessMan import *


#五子棋棋盘类
class ChessBoard(object):
	#类属性
	board_size = 15 #棋盘的大小
	
	#初始化
	def __init__(self):
		#下标从0到15
		self.__board = [[0 for i in range(ChessBoard.board_size+1)] for i in range(ChessBoard.board_size+1)]
	
	
	#清空
	def init_board(self):
		for i in range(1, ChessBoard.board_size+1):
			for j in range(1, ChessBoard.board_size+1):
				self.__board[i][j] = '+'
	
	#打印棋盘
	def print_board(self):
		#打印列号
		print('   ', end='')
		for i in range(1, ChessBoard.board_size+1):
			c = chr(ord('a') + i - 1)
			print(c, end = ' ')
		print()
		#打印行号加棋盘
		for i in range(1, ChessBoard.board_size+1):
			#打印行号
			if 1 <= i <= 9:
				print(' ', end='')
			print(i, end=' ')
			#打印棋盘内容
			for j in range(1,ChessBoard.board_size+1):
				print(self.__board[i][j], end=' ') #不能换行
			#换行
			print("")


	#摆放棋子
	#参数 坐标（必须为元组 长度为2）
	#参数 棋子的颜色
	def set_chess(self, pos, color):
		if not isinstance(pos, tuple):
			raise RuntimeError('第一个参数必须为元组')
		if pos[0] <= 0 or pos[0] > ChessBoard.board_size:
			raise RuntimeError('下标越界')
		if pos[1] <= 0 or pos[1] > ChessBoard.board_size:
			raise RuntimeError('下标越界')
		self.__board[pos[0]][pos[1]] = color

	#把chessman对象摆放到棋盘上
	def set_chessman(self,chessman):
		if not isinstance(chessman, ChessMan):
			raise RuntimeError('类型不对 第一个必须为ChessMan对象')
		pos = chessman.get_pos()
		color = chessman.get_color()
		return self.set_chess(pos, color)

	#根据位置获取棋子的颜色
	def get_chess(self,pos):
		if pos[0] <= 0 or pos[0] > ChessBoard.board_size:
			raise RuntimeError('下标越界')
		if pos[1] <= 0 or pos[1] > ChessBoard.board_size:
			raise RuntimeError('下标越界')
		return self.__board[pos[0]][pos[1]]

	def get_board(self):
		return self.__board






































