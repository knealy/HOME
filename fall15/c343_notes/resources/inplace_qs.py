def inplace_qs(S,a,b):
	if a>=b: return
	pivot = S[b]
	left = a 
	right = b-1
	while left <= right:
		while left <= right and S[left] < pivot:
			left +=1 
		while left <=right and pivot < S[right]:
			right -=1
		if left <= right:
			S[left],S[right] = S[right],S[left]
			left,right = left+1, right-1

	S[left], S[b] = S[b], S[left]
	inplace_qs(S,a,left-1)
	inplace_qs(S,left+1,b)

A = [1,4,3,9,5,6,9,7,8]
print A
inplace_qs(A,0,len(A)-1)
print A