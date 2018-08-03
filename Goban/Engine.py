


from ChessBoard import *
from ChessMan import *
import random,math

#电脑策略类
class Engine(object):
	#初始化  需要把棋盘对象导入
	def __init__(self, chessboard):
		self.__chessboard = chessboard

	#电脑下棋的策略
	#告诉棋子的颜色 返回棋子的位置
	#传入chessman对象的时候  把棋子的颜色写入
	#该方法中负责填写棋子的位置
	def computer_go(self,chessman):
		if not isinstance(chessman, ChessMan):
			raise RuntimeError('类型不对 第一个必须为ChessMan对象')
		
		while True:
			#pos_x 和pos_y在1~15之间随机生成一个数
			pos_x = math.ceil(random.random() * ChessBoard.board_size)
			pos_y = random.randint(1,15)
			if self.__chessboard.get_chess((pos_x,pos_y)) == '+':
				print('电脑下棋的位置：%d,%d' %(pos_x,pos_y))
				#把pos_x和pox_y传入chessman
				chessman.set_pos((pos_x,pos_y))
				#退出循环
				break


	#用户在终端下棋
	#提示用户 传入输入字符串 并解释该字符串对应的位置
	#传入chessman对象的时候  把棋子的颜色写入
	#该方法中负责填写棋子的位置
	#比如 3，b 表示第3行第2列
	def parse_uesr_input(self, input, chessman):
		if not isinstance(chessman, ChessMan):
			raise RuntimeError('类型不对 第一个必须为ChessMan对象')
			
		ret = input.split(',')
		value1 = ret[0]
		value2 = ret[1]
		#转换成坐标
		pos_x = int(value1)
		pos_y = ord(value2) - ord('a') + 1
		#print(rets)
		chessman.set_pos((pos_x,pos_y))
	
	#方法一
	#判断胜负
	#当pos位置放置color颜色的棋子后 胜负是否已分
	#返回True表示胜负已分  返回False表示胜负未分
	def is_won(self, pos, color):
		#垂直方向的判断
		start_x = 1
		if pos[0]-4 >= 1:
			start_x = pos[0] - 4
		end_x = 15
		if pos[0] + 4 < 15:
			end_x = pos[0] + 4
		count = 0 #统计有多少连续的棋子
		for pos_x in range(start_x, end_x + 1):
			if self.__chessboard.get_chess((pos_x, pos[1])) == color:
				count += 1
				#print(pos_x, count)
				if count >= 5:
					return True
			else:
				#一旦断开 统计计数清零  但不能退出
				count = 0


		#水平方向的判断
		start_y = 1
		if pos[1]-4 >= 1:
			start_y = pos[1] - 4
		end_y = 15
		if pos[1]+4 <= 15:
			end_y = pos[1] + 4
		#print('start_y:%d, end_7:%d'%(start_y, end_y))
		count = 0  # 统计有多少连续的棋子
		for pos_y in range(start_y, end_y + 1):
			if self.__chessboard.get_chess((pos[0],pos_y)) == color:
				count += 1
				#print(pos_y, count)
				if count >= 5:
					return True
			else:
				#一旦断开 统计计数清零  但不能退出
				count = 0
		#左上右下的方向的判断


		#左下右上的方向的判断
		
		return False

	#方法二
	#判断胜负
	# 当pos位置放置color颜色的棋子后 胜负是否已分
	# 返回True表示胜负已分  返回False表示胜负未分
	# 获胜的判断
	def is_Win(self, list):

		for i in range(len(list)):
			for j in range(len(list[i])):
				# 横向判断
				value = []
				if i < len(list) and j < len(list[i]) - 4:
					value.extend([list[i][j], list[i][j + 1], list[i][j + 2],
								  list[i][j + 3], list[i][j + 4]])
					if self.is_same(value):
						return True
				#竖向判断
				value = []
				if i < len(list) and j < len(list[i]) - 4:
					value.extend([list[j][i], list[j + 1][i], list[j + 2][i],
								  list[j + 3][i], list[j + 4][i]])
					if self.is_same(value):
						return True
				#左上右下判断
				value = []
				if i < len(list) - 4 and j < len(list[i]) - 4:  # 正斜
					value.extend([list[i][j], list[i + 1][j + 1], list[i + 2][j + 2],
								  list[i + 3][j + 3], list[i + 4][j + 4]])
					if self.is_same(value):
						return True

				#右上左下
				value = []
				if 4 < i < len(list) and j < len(list[i]) - 4:  # 反斜
					value.extend([list[j][i], list[j + 1][i - 1], list[j + 2][i - 2],
								  list[j + 3][i - 3], list[j + 4][i - 4]])
					if self.is_same(value):
						return True
		return False
	#胜负判断
	def is_same(self, result):
		result = list(set(result))

		if len(result) == 1 and result[0] == "o":
			print("白棋胜利")
			return True
		if len(result) == 1 and result[0] == "x":
			print("黑棋胜利")
			return True

		return False

	#判断胜负
	#判断chessman对象的棋子放置后 胜负是否已分
	#调用is_won()返回她的返回值即可
	def is_woman(self,chessman):
		if not isinstance(chessman, ChessMan):
			raise RuntimeError('类型不对 第一个必须为ChessMan对象')
		pos = chessman.get_pos()
		color = chessman.get_color()
		return self.is_won(pos, color)

	#方法一的play方法
	#def play(self,chessboard,chessman,chesscomputer):

		#实现游戏的主流程
		# while True:
		# 	print('请选择先后，b代表执黑  w代表执白(黑先下，白后行)')
		# 	input1 = input()
		# 	if input1 == 'b':
		# 		chessman.set_color('x')
		# 		chesscomputer.set_color('o')
		# 		print('初始棋盘如下')
		# 		chessboard.init_board()
		# 		chessboard.print_board()
		# 		while True:
        #
		# 			input2 = input('请下棋(如:12,f):')
		# 			self.parse_uesr_input(input2,chessman)
		# 			chessboard.set_chessman(chessman)
		# 			print('此时棋盘如下')
		# 			chessboard.print_board()
		# 			result = self.is_woman(chessman)
		# 			if result == True:
		# 				print('黑棋赢了！')
		# 				break
        #
		# 			self.computer_go(chesscomputer)
		# 			chessboard.set_chessman(chesscomputer)
		# 			chessboard.print_board()
		# 			result = self.is_woman(chesscomputer)
		# 			if result == True:
		# 				print('白棋赢了')
		# 				break
		# 		print('是否再来一局(y/n):')
		# 		input3 = input()
		# 		if input3 == 'y':
		# 			self.play(chessboard,chessman,chesscomputer)
		# 		elif input3 == 'n':
		# 			break
		# 		else:
		# 			print('你输入的有误，请重新输入：')
        #
		# 	elif input == 'w':
		# 		chessman.set_color('o')
		# 		chesscomputer.set_color('x')
		# 		chessboard.init_board()
		# 		chessboard.print_board()
		# 		while True:
		# 			self.computer_go(chesscomputer)
		# 			chessboard.set_chessman(chesscomputer)
		# 			chessboard.print_board()
		# 			result = self.is_Win(chessboard.get_board())
		# 			if result == True:
		# 				break
		# 			input2 = input('请下棋(如:12,f):')
		# 			self.parse_uesr_input(input2, chessman)
		# 			chessboard.set_chessman(chessman)
		# 			print('此时棋盘如下')
		# 			chessboard.print_board()
		# 			result = self.is_Win(chessboard.get_board())
		# 			if result == True:
		# 				break
		# 		print('是否再来一局(y/n):')
		# 		input3 = input()
		# 		if input3 == 'y':
		# 			self.play(chessboard, chessman, chesscomputer)
		# 		elif input3 == 'n':
		# 			break
		# 		else:
		# 			print('你输入的有误，请重新输入：')
		# 	else:
		# 		print('你输入的有误,请重新输入：')
		# 		self.play(chessboard,chessman,chesscomputer)
		#print('游戏退出')


	#方法二的play方法
	def play(self,chessboard,chessman,chesscomputer):

		#实现游戏的主流程
		while True:
			print('请选择先后，b代表执黑  w代表执白(黑先下，白后行)')
			input1 = input()
			if input1 == 'b':
				chessman.set_color('x')
				chesscomputer.set_color('o')
				print('初始棋盘如下：')
				chessboard.init_board()
				chessboard.print_board()
				while True:

					input2 = input('请下棋(如:12,f):')
					self.parse_uesr_input(input2,chessman)
					chessboard.set_chessman(chessman)
					print('此时棋盘如下')
					chessboard.print_board()
					result = self.is_Win(chessboard.get_board())
					if result == True:
						break

					self.computer_go(chesscomputer)
					chessboard.set_chessman(chesscomputer)
					chessboard.print_board()
					result = self.is_Win(chessboard.get_board())
					if result == True:
						break
				print('是否再来一局(y/n):')
				input3 = input()
				if input3 == 'y':
					self.play(chessboard,chessman,chesscomputer)
				elif input3 == 'n':
					break
				else:
					print('你输入的有误，请重新输入：')

			elif input == 'w':
				chessman.set_color('o')
				chesscomputer.set_color('x')
				chessboard.init_board()
				chessboard.print_board()
				while True:
					self.computer_go(chesscomputer)
					chessboard.set_chessman(chesscomputer)
					chessboard.print_board()
					result = self.is_Win(chessboard.get_board())
					if result == True:
						break
					input2 = input('请下棋(如:12,f):')
					self.parse_uesr_input(input2, chessman)
					chessboard.set_chessman(chessman)
					print('此时棋盘如下')
					chessboard.print_board()
					result = self.is_Win(chessboard.get_board())
					if result == True:
						break
				print('是否再来一局(y/n):')
				input3 = input()
				if input3 == 'y':
					self.play(chessboard, chessman, chesscomputer)
				elif input3 == 'n':
					break
				else:
					print('你输入的有误，请重新输入：')
			else:
				print('你输入的有误,请重新输入：')
				self.play(chessboard,chessman,chesscomputer)
		print('游戏退出！')















