
def greedy_change(val):
	v = int(val*100)
	end = dict()
	total = 0
	q = v/25
	v = v-q*25
	end['quarters']=q
	d = v/10
	v = v-d*10
	end['dimes']=d
	n = v/5
	end['nickels']=n
	p = v-n*5
	end['pennies']=p
	for e in end.values():
		total += e
	return repr(end)+'\ntotal coins: '+str(total)

print greedy_change(1.70)
print greedy_change(1.6)
print greedy_change(.3)
print greedy_change(13.72)


