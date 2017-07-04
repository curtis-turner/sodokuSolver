class SubBoard: 
	def __init__(self, row1, row2, row3):
		self._allNum = allSet
		self._sbs = row1+row2 + row3
		total = row1 + row2 + row3
		for e in total:
			e._sbs = self

	def choices(self):
		l = []
		for e in self._sbs:
			print(e)
			if e._elementVal != None:
				l.append(e._elementVal)
		s = set(l)
		return self._allNum - s