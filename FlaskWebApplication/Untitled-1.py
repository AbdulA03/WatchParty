def bruteForceStringMatch (t, p):
    for i in range(len(t) - len(p)+1):
        j=0
        while j < (len(p)) and t[i+j] == p[j]:
            j = j+1
        if j == len(p) :
            return i
    return -1

text = ['A','B','C']
pattern = ['D','A','L','A','B','C']

print(bruteForceStringMatch(text,pattern))