f = open("data10.txt","r")
#lista = []
sum_lista = []
set_in = ["(", "{", "[", "<"]
set_out = [")","}","]",">"]
set_1 = [['(', ')'],['{', '}'],['[', ']'],['<', '>']]
k = 0

#line = f.readline()

for line in f:
    print(sum_lista)

    lista = []
#if (len(line)%2 == 0):
    print(line)
    for i in range(0,len(line)):
        #print(i)
        if line[i] in set_in:
            #print("here")
            lista.append(line[i])
            #print(lista)
        else:
            pom_lista = [] 
            pom_lista.append(lista[-1])
            pom_lista.append(line[i])
            print(pom_lista)
            #print(len(lista))
            
            if (pom_lista in set_1):
                print(lista[-1])
                print(line[i])   
                lista.pop()
                print(len(lista))
                #break
                #print(lista)
            else:
                if (lista[-1] == set_1[0][0] and line[i] != '\n'):
                    #sum_lista.append(set_1[0][1]) 
                    sum_lista.append(line[i])
                elif (lista[-1] == set_1[1][0] and line[i] != '\n'):
                    #sum_lista.append(set_1[1][1]) 
                    sum_lista.append(line[i])
                elif (lista[-1] == set_1[2][0] and line[i] != '\n'):
                    #sum_lista.append(set_1[2][1])
                    sum_lista.append(line[i])
                elif (lista[-1] == set_1[3][0] and line[i] != '\n'):
                    #sum_lista.append(set_1[3][1])
                    sum_lista.append(line[i])
                else:
                    print("KRAJ")
                #lista.pop() 
                break
            #print(len(lista))   
#print(lista)                   
print(sum_lista)
total = 0
count = {")": 3, ">": 25137, "}": 1197, "]": 57}
for item in sum_lista:
    total = total + count.get(item)
print(total)
