f = open("data10.txt","r")
sum_lista = []
set_in = ["(", "{", "[", "<"]
set_out = [")","}","]",">"]
set_1 = [['(', ')'],['{', '}'],['[', ']'],['<', '>']]
k = 0
final_lista = []
#line = f.readline()
for line in f:
    #print(len(line))
    #print(line[len(line)])
    lista = []
    #print(line)
    #print(len(line))
    #print("s ", line[len(line)-2])

    #print(len(line))
    #print(line[len(line)])
    #print("==========")
    for i in range(0,len(line)):
    
        if line[i] in set_in:
            lista.append(line[i])
        elif line[i] == '\n':
            break
        else:
            pom_lista = [] 
            pom_lista.append(lista[-1])
            pom_lista.append(line[i])
            #print("here 1")
            
            if (pom_lista in set_1):
                #print(lista[-1])
                #print(line[i])   
                lista.pop()
                #print("here 2")
                
            else:  
                lista = []
                break  
            """
                if (lista[-1] == set_1[0][0] and line[i] != '\n'):
                    sum_lista.append(set_1[0][1]) 
                    #sum_lista.append(line[i])
                elif (lista[-1] == set_1[1][0] and line[i] != '\n'):
                    sum_lista.append(set_1[1][1]) 
                    #sum_lista.append(line[i])
                elif (lista[-1] == set_1[2][0] and line[i] != '\n'):
                    sum_lista.append(set_1[2][1])
                    #sum_lista.append(line[i])
                elif (lista[-1] == set_1[3][0] and line[i] != '\n'):
                    sum_lista.append(set_1[3][1])
                    #sum_lista.append(line[i])
                else:
                    print(line[i])
                    print("KRAJ")
                """    
               
    final_lista.append(lista)
new_final = []    
for i in range (0, len(final_lista)):
    if final_lista[i] != []:
        new_final.append(final_lista[i])  

fin_fin = []
for i in range (0, len(new_final)):
    new_f=[]
    new_final[i].reverse()
    for j in range (0, len(new_final[i])):
        if (new_final[i][j] == set_1[0][0]):
            new_f.append(set_1[0][1]) 
        elif (new_final[i][j] == set_1[1][0] ):
            new_f.append(set_1[1][1]) 
        elif (new_final[i][j] == set_1[2][0]):
            new_f.append(set_1[2][1])
        elif (new_final[i][j] == set_1[3][0] ):
            new_f.append(set_1[3][1])

    fin_fin.append(new_f)

#print(fin_fin)



#print(new_final)                   
#print(sum_lista)
#print(final_lista)
#print(len(new_final))
final_score = []
#count = {")": 3, ">": 25137, "}": 1197, "]": 57}
count = {")": 1, ">": 4, "}": 3, "]": 2}
for item in fin_fin:
    total_score = 0
    for j in range (0, len(item)):
        total_score = 5 * total_score + count.get(item[j])
    final_score.append(total_score)
final_score.sort()
k = len(final_score)
k = int(k/2)
print(k)
print(final_score)
print(final_score[k])
