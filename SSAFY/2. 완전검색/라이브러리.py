import itertools

arr = [1,2,3]

result = itertools.permutations(arr) # (arr, 3)
print("순열 : ", end =" ")
print(list(result))


result = itertools.product(arr, repeat =2)
print("중복순열 : ", end =" ")
print(list(result))

result = itertools.combinations(arr, r=2)
print("조합 : ", end =" ")
print(list(result))

result = itertools.combinations_with_replacement(arr, r=2) 
print("중복조합 : ", end =" ")
print(list(result))
