def powerset(s):
	masks = [1 << i for i in range(len(s))]
	for i in range( 1 << len(s) ):
		yield [ss for ss, mask in zip(s, masks) if mask & i]
		
		
print(list(powerset([1,2,3,4])))