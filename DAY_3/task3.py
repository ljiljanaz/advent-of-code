f= open("test3.txt", "r")
data = f.readlines()
gama = " "
epsilon = " "
l = len(data[0])-1
for i in range (0,l):
    g, e = 0, 0
    for j in range (0, len(data)-1):
        p=data[j]
        if p[i] == "1":
            g = g + 1
        else:
            e = e + 1
    if g > e:
        gama = gama + "1"
        epsilon = epsilon + "0"
    else:
        gama = gama + "0"
        epsilon = epsilon + "1"
b=int(gama,2)
d=int(epsilon, 2)
#print(b*d)

k = 0
while k < l:
    t = (len(data))
    new_data_1 = []
    new_data_2 = []
    for j in range (0, t):     
        p = data[j]
        if p[k] == "1":
            new_data_1.append(data[j])
            #print(new_data_1)
        else:
            new_data_2.append(data[j])
        #print(new_data_1)
    #print("=========")
    #print(new_data_2)        
    if (len(new_data_1) >= len(new_data_2) and len(new_data_2) != 0):
        data = new_data_1
        #data = new_data_2
    else:
        data = new_data_2
        #data = new_data_1
    k = k + 1
    if(len(data) == 1):
         break
print(data)    
print(len(data))   
b1=int(data[0],2)      
print(b1)     



