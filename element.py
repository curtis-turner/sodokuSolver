class Element:
	def __init__ (self, value, index):
		self._elementVal = value
		self._index = index
		self._row = None
		self._col = None
		self._sbs = None
	#print('initialized element.')
	
	def __str__(self):
		return str(self._elementVal)
		
	def choices(self):
		x = self._row.choices() & self._col.choices() & self._sbs.choices()
		print(x)
		return x