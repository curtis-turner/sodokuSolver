class Column:
	def __init__(self, column):
		self._allNum = allSet
		self._col = column
		for e in self._col:
			e._col = self
	#print('initialized column.')
	def choices(self):
		l = []
		for e in self._col:
			print(e)
			if e._elementVal != None:
				l.append(e._elementVal)
		s = set(l)
		return self._allNum - s
    