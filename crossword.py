m,p = int(input()),1
while m != 0:
    n,l,a,b = int(input()),[],[],[]
    num,sum = 0,0
    for i in range(m):
        i = [x for x in input()]
        a.append(i)

    for i in range(m):
        l = []
        for j in range(n):
            if i == 0 or j == 0 and a[i][j] != '*':
                sum += 1
                l.append(sum)
            elif a[i][j-1] == '*' or a[i-1][j] == '*' and a[i][j] != '*':
                sum += 1
                l.append(sum)
            else:
                l.append(0)
        b.append(l)
    print(" PUZZLE #",p)
    print("ACROSS=============")
    for i in range(m):
        s = ''
        for j in range(n):
            if a[i][j] != '*':
                if len(s) == 0:
                    num = b[i][j]
                s += a[i][j]
            if j == n-1 or a[i][j] == '*':
                s += '\0'
                if s[0] != '\0':
                    print(str(num) + '.' + s)
                s = ''

    print("DOWN===============")
    l3,l4 = [],[]
    for i in range(n):
        s = ''
        for j in range(m):
            if a[j][i] != '*':
                if len(s) == 0:
                    num = b[j][i]
                s += a[j][i]
            if j == m-1 or a[j][i] == '*':
                s += '\0'
                if s[0] != '\0':
                    l3.append(num)
                    l4.append(s)
                s = '' 
    
    my_dict = dict(zip(l3,l4))
    for i in sorted(my_dict.keys()):
        print(str(i) + '.' + my_dict[i])
    p += 1
    m = int(input())



