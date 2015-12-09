# knapsack problem: 
# You break in some house, you have a weight limit you can carry:
# Need to steal the stuff with the highest value and lowest cost

# Original:

# def knpsack(weight_remaining,items,used):
# 	maxV = 0
# 	for item in items:
# 		if item not in used and (item-weight <= weight_remaining):
# 			newV = item-valuer + knpsack((weight_remaining - item_weight), items, used.append(item))
# 			if maxV < newV:
# 				maxV = newV
# 	return maxV



# Memoized version (dyn. programming):

def knpsack(weight_remaining,items,used, memo):
	if used in memo:
		return memo[used]
	maxV = 0
	for item in items:
		if item not in used and (item-weight <= weight_remaining):
			newV = item-valuer + knpsack((weight_remaining - item_weight), items, used.append(item), memo)
			if maxV < newV:
				maxV = newV
	memo[used] = maxV
	return maxV
