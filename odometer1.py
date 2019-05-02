l,a = list(filter(lambda x : x%10 and x%11 and(x%10 > x//10),range(12,90))),int(input())
print('invalid') if a not in l else print(l[-2],l[0]) if a==l[-1] else exit() if l.index(a) == -1 else print(l[l.index(a)-1],l[l.index(a)+1]) if l.index(a) in range(len(l)) else 0
