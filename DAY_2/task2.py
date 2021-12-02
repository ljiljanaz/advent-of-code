f=open("data.txt", "r")
data = f.readlines()
print(data[0])
f = 0
d = 0
aim = 0
for i in range (0, len(data)):
    p = data[i].split(" ")
    if p[0] == "forward":
        f = f + int(p[1])
        aim = aim + (d * int(p[1]))
    elif p[0] == "up": 
        d = d - int(p[1])
    else: 
        d = d + int(p[1])
print(f)
print(d)
print(f*aim)        
