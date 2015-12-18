def dyn_prog_rod_cut(p,n):
	table = [None for _ in range(0,n+1)]
	table[0] = $0
	for i in range(1,n+1):
		best = -1
		for cut in range(1,i+1):
			best = max(best,p[cut]+table[i-cut])
		table[i] = best
	return table[n]

## general template for dyn. programming: ##

class DynamicProgramming:
	def solve(self):
		table = {}
		for p in self.base_cases():
			table[p] = self.initial_solution(p)
		for p in self.enumerate_subproblems():
			best = None
			for choice in self.choices(p,table):
				if (not best) or (choice.better_than(best)):
					best = choice
			table[p] = best
		return table[self.complete_problem()]

	def enumerate_problems(self):
		for i in range(1,self.n+1):  # maybe meant to be (1, self, n+1) ?
			yield i
	def choices(self, i, table):
		for cut in range(1,i+1):
			yield Result(self.p[cut]+table[i-cut])


class CutRod(DynamicProgramming):
	def __init__(self,p,n):
		self.p = p
		self.n = n
	def base_cases(self):
		yield 0
	class Result:
		def better_than(self,other):
			return self.price >  other.price


def dna_align(X,Y,startX,startY,lenX,lenY):
	pass