# List Comprehension 

case1 = [1,2,3]
case2 = [4,2,1]

result = [i+j for i in case1 for j in case2 if i!=j]

print(result)


words = "the quick brown fox jumps over the lazy dog".split()
print(words)
result = [[w.upper(), w.lower(), len(w)] for w in words]
print(result)
