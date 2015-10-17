def disjoint(A,B,C):
	sort_list = []
	sort_list += A
	sort_list += B
	sort_list += C
	sort_list.sort()
	if len(set([x for x in sort_list if sort_list.count(x)>2]))==0:
		return True
	else:
		return False

A = [1,2,6]
B = [4,5,5]
C = [7,8,6]

print disjoint(A,B,C)