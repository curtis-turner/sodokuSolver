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