class Row:
	def __init__(self, row):
		self._allNum = allSet
		self._row = row
		for e in self._row:
			e._row = self
	#print('initialized row.')
	def choices(self):
		l = []
		for e in self._row:
			print(e)
			if e._elementVal != None:
				l.append(e._elementVal)
		s = set(l)
		return self._allNum - s