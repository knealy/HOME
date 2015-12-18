*** student exercise: write a bottom-up version of chain_ordering.

def dyn_prog_chain_ordering(chain):
	table = {}

	# initialize results for single matrices
	for start in range(0, len(chain)):
	    end = start + 1
	    table[(start,end)] = Result(None, 0, chain[start], None, None)

	# l is the chain length
	for l in range(2, len(chain)+1):
	    for start in range(0, len(chain)-l+1):
		end = start + l
		best_yet = None
		for split in range(start+1, end):
		    left = table[(start, split)]
		    right = table[(split, end)]
		    cost = left.dim[0] * left.dim[1] * right.dim[1] \
			   + left.cost + right.cost
		    res = Result(split, cost, (left.dim[0], right.dim[1]),
				 left, right)
		    if (not best_yet) or (cost < best_yet.cost):
			best_yet = res
		table[(start,end)] = best_yet
	return table[(0, len(chain))]

