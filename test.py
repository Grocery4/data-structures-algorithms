l = [1,2,5,7,3]
l_2 = [1,3,5,7,2]

a = None
b = None

for i in range(len(l)):
    if(l_2[i] != l[i]):
        if (a != None):
            b = i
        else:
            a = i

print(a,b)