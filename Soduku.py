import sys        
from heapq import *

allSet = set(range(1, 9+1))

fileName = sys.argv[1]
listOfPuzzles = []
f = open(fileName, 'r')

listOfPuzzles = f.read().split('\n')

del listOfPuzzles[-1] #delete \x1a (EOF Marker)


class Puzzle:
    def __init__(self, puzzle):
        self._all = allSet
        self._puzzle = puzzle
        self._solution = 'None'
        self._elements = []
        self._rows = []
        self._cols = []
        self._sbs = []

        #initialize elements
        for e,j in zip(puzzle, range(len(puzzle))):
            if e != '.':
                self._elements.append(Element(int(e),j))
            else:
                self._elements.append(Element(None, j))
        
        #self._elements[Element(int(e), j) if e != '.' else Element(None,j) for e,j in zip(puzzle, range(len(puzzle)))]
        
        #initialize rows
        #for i in range(0, 81, 9):
        #    l = self._elements[i:i+9]
        #    self._rows.append(Row(self._all, l))
#self._all, goes before self._elements in below function call
        self._rows = [Row(self._elements[i:i+9]) for i in range(0,81,9)]
        
        #initialize columns
        #for i in range(9):
        #    l = self._elements[i:81:9]
        #    self.cols.append(self._all, l)
     #self._all, goes before sel._elements in below Column __init__   
        self._cols = [Column(self._elements[i:81:9]) for i in range(9)]

        #initialize subboards
        for i in range(0, 81, 27): 
            for j in range(0, 9, 3):
                s = i + j
                row1 = self._elements[s:s+3]
                row2 = self._elements[s+9:s+12]
                row3 = self._elements[s+18:s+21]
                self._sbs.append(SubBoard(row1, row2, row3))#self._all, put this before row1, ... in SubBoard(...) __init__
        
        #self._sbs = [SubBoard(self._all, self._elements[s:s+3], self._elements[s+9:s+12], self._elements[s+18:s+21]) for i,j in zip(range(0,81,27), range(0,9,3))]
        for i in self._elements:
            print(i)
			
        print('Initialized successfully.')
    
    def __str__(self):
    	l = []
    	for e in self._elements:
    		if e._elementVal == None:
    			l.append('.')
    		else:
    			l.append(e._elementVal)
    	return ''.join(map(str, l))
    	#l = [ x._name for x in self._elements if x == None ]
    	#s= ''.join(map(str, l))
    	#if
    	


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
		
def sodokuSolver(puzzle):
	#blank = puzzle.find('.')
	h = []
	for e in puzzle._elements:
		#print(e)
		if e._elementVal == None:
			guess = e.choices()
			if len(guess) == 1:
				e._elementVal = next(iter(guess))
		else:
			heappush(h,(len(e.choices()), e))# goes inbetween according to notes(len(e.choices()))e
	g=[]
	g = heappop(h)
	e = g[0]
	for c in e.choices():
		e.set(c)
		str(B)
		g.append(s)
	currentGuess = g.pop()
	puzzle.reinit(currentGuess)

def main():     
	newPuzzle = Puzzle(listOfPuzzles[0])
	print(newPuzzle)

	sodokuSolver(newPuzzle)
	#solution = sodokuSolver(newPuzzle)
	#print(solution)

if __name__ == '__main__':
    main()