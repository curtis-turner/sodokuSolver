import sys        
from heapq import *

allSet = set(range(1, 9+1))

fileName = sys.argv[1]
listOfPuzzles = []
f = open(fileName, 'r')

listOfPuzzles = f.read().split('\n')

del listOfPuzzles[-1] #delete \x1a (EOF Marker)
    		
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