class Cell:

	def __init__(self,cellType='wall'):
		self.cellType = cellType  #or room
		self.visited = False
		self.baseWidth = 50
		self.baseHeight = 25
		self.topEdge = ['+']+['_']*50+['+']
		self.bottomEdge = ['+']+['-']*50+['+']
		self.edgesY = ['|']+(['`']*50)+['|']
		self.baseShapeAt0 = [self.topEdge]+(25*[self.edgesY])+[self.bottomEdge]