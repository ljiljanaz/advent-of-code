import re
import collections

points: collections.Counter[tuple[int, int]] = collections.Counter()
#f = open("test5.txt", "r")
f = open("data5.txt", "r")
lines = f.readlines()
min_l = 0
max_l = 0
rest, row, col = 0, 0, 0
new_l, new_ll = [], []
for line in lines:
    data = str(line)
    p = data[0:len(data)-1].replace(' -> ',',').split(',')
    #new_l.append((p))
    #print(p)
    new_ll = [int(x) for x in p]
    new_l.append((new_ll))
    #print(new_ll)
    if min_l > min(new_ll):
        min_l = min(new_ll)
    if max_l < max(new_ll):
        max_l = max(new_ll)

res_mat = [ [ 0 for i in range(1 + max_l) ] for j in range(1 + max_l) ]
#print(res_mat)
print(min_l, max_l)
#print("new_l = ",len(new_l))
print(new_l[0])
for i in range (0,len(new_l)):
    t = new_l[i]
    if t[1] == t[3]:
        
        row = row + 1
        k = int(t[1])
        #print("k = ",k)
        min_b = int(min(t[0],t[2]))
        max_b = int(max(t[0],t[2]))
        max_b = max_b + 1
        #print(min_b, max_b)
        for j in range (min_b, max_b):
            s = res_mat[k][j]
            s = s + 1
            res_mat[k][j] = s
            points[j,t[1]] +=1
            #print(points[j,t[1]])

    elif t[0] == t[2]:
        col = col + 1
        v = int(t[0])
        min_b = int(min(t[1],t[3]))
        max_b = int(max(t[1],t[3]))
        max_b = max_b + 1
        for j in range (min_b, max_b):
            m = res_mat[j][v]
            m = m + 1
            res_mat[j][v] = m
            points[t[0],int(j)] +=1
    else:
        rest = rest + 1
suma = 0
for i in range(0, 991):
    for j in range(0, 991):
        if res_mat[i][j] > 1:
            suma = suma + 1
count = 0
for k,v in points.most_common():
    if v > 1:
        count +=1
    else:
        pass

#print(len(res_mat))
#print(len(res_mat[0]))
print(suma)
#print(points)
#print(rest, row, col)
print("count =", count)
