def fact(n):
    if n == 1 :   # basis part
        return 1
    else:
        return n * fact(n-1) # inductive

print(fact(4))