from math import *

class ascgraph:
	
	def __init__(self, x:int=10, y:int=10, char:str="▒"):
		self.array = [[char for  _x in range(x)] for _y in range(y)] 
		self.width, self.height = x, y
		self.char = char
	
	def __str__(self) -> str:
		map_string = "\n".join(["".join([x for x in y]) for y in self.array])
		return map_string
	
	def point(self, x:int=0, y:int=0, char:str="█"):
		if (0 <= x < self.width) and (0 <= y < self.height):
			self.array[y][x] = char
	
	def line(self, x1:int=0, y1:int=0, x2:int=0, y2:int=0, char:str="█"):
		delta_x = abs(x2 - x1)
		delta_y = abs(y2 - y1)
		if x1 < x2:
			sign_x = 1
		else:
			sign_x = -1
		if y1 < y2:
			sign_y = 1
		else:
			sign_y = -1
		
		error = delta_x - delta_y
		self.point(x2, y2, char)
		while (x1 != x2 or y1 != y2): 
			self.point(x1, y1, char)
			error_2 = error * 2
			if error_2 > -delta_y: 
				error -= delta_y
				x1 += sign_x
			if error_2 < delta_x:
				error += delta_x
				y1 += sign_y
	
	def rect(self, x1:int=0, y1:int=0, x2:int=0, y2:int=0, char:str="█"):
		for x in range(x1, x2+1):
			for y in range(y1, y2+1):
				self.point(x, y, char)
	
	def clear(self):
		self.array = [[self.char for  _x in range(self.width)] for _y in range(self.height)] 