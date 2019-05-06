size,num,l1 = int(input()),int(input()),[]
l ='123456789'
start,limit = int(l[:size]),int(l[-size:])

def isAscending(num):
    if len(set(list(num))) == len(num):
        return 1
    return 0

def previous(num,l1):
    if int(num) in l1:
        a = l1.index(int(num))
        return l1[a-1]

def next(num,l1):
    if num == l1[-1]:
        return l1[0]
    if int(num) in l1:
        a = l1.index(int(num))
        return l1[a+1]

def previous_nth_reading(num,l1,n):
    for i in range(n):
        a = l1.index(int(num))
        p = previous(num,l1)
        num = l1[a-1]
    return num

def next_nth_reading(num,l1,m):
    for i in range(m):
        a = l1.index(int(num))
        n = next(num,l1)
        if num == l1[-1]:
            num = l1[0]
        else:
            num = l1[a+1]
    return num

def difference(num1,num2,l1):
    if num2 > num1:
        return l1.index(num2) - l1.index(num1)
    else:
        count = 0
        while num1 != num2:
            count,a = count + 1,l1.index(num1)
            if num1 == l1[-1]:
                num1 = l1[0]
            else:
                num1 = l1[a+1]


for x in range(start,limit + 1):
    if list(str(x)) == sorted(str(x)) and x % 11 != 0 and isAscending(str(x)):
        l1.append(x)

if num not in l1:
    print("invalid")
else:
    print("prvious number = ",previous(num,l1))
    print("next number = ",next(num,l1))

    n = int(input())
    print("previous nth number = ",previous_nth_reading(num,l1,n))

    m = int(input())
    print("next nth reading = ",next_nth_reading(num,l1,m))

    num1,num2 = int(input()),int(input())
    print("difference = ",difference(num1,num2,l1))




