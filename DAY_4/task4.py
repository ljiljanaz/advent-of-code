import numpy as np
input_text = np.loadtxt("data4.txt", dtype="int")
input_text_copy = input_text.copy()
#bingo = [7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1]
bingo = [87,7,82,21,47,88,12,71,24,35,10,90,4,97,30,55,36,74,19,50,23,46,13,44,69,27,2,0,37,33,99,49,77,15,89,98,31,51,22,96,73,94,95,18,52,78,32,83,85,54,75,84,59,25,76,45,20,48,9,28,39,70,63,56,5,68,61,26,58,92,67,53,43,62,17,81,80,66,91,93,41,64,14,8,57,38,34,16,42,11,86,72,40,65,79,6,3,29,60,1]

for i in range (0, 4):
    input_text[input_text == bingo[i]] = -1
bingo_win = -1
bingo_k = -1
bingo_raw = 0
tr_k = -1
k_array = []
k = int(len(input_text)/5)
for i in range(1,k+1):
    k_array.append(int(i))
print(k_array)
tru = 0
j = 1
fin_num = -1
tr = -1
new_l = []
for s in  range (4, len(bingo)):
    input_text[input_text == bingo[s]] = -1
    
    bingo_win = -1
    sta = 0
    sto = 5
    j = 1
    while j < k+1:
        pom_input = input_text[sta:sto]
        for i in range (0,5):    
            if (pom_input[i].sum() == -5):
                print("i: ",i)
                bingo_win = i
                bingo_k = j
                bingo_raw = 1
                print(input_text[sta:sto])
                #k_array.pop(j-1)
                print("j ", j)
                print("len ", len(k_array))
                if j not in new_l:
                    new_l.append(j)
                #break           
            else:
                pom_input_trans = pom_input.transpose()  
                for z in range (0,5):
                    
                    if (pom_input_trans[z].sum() == -5):
                        bingo_win = z
                        bingo_k = j
                        bingo_raw = -1
                        #k_array.pop(j)
                        if j not in new_l:
                            new_l.append(j)
                        #break  
        j = j + 1  
        sta = sta + 5
        sto = sto + 5
        if len(new_l) == len(k_array):
            fin_num = bingo[s]
            break

        """
        if bingo_win !=-1:
            tr = bingo_win
            tr_k = bingo_k
            bingo_raw_raw = bingo_raw
            break
    if tr !=-1:
        break
        """
    if fin_num != -1:
        break    
print("bingo s", bingo[s])    
#if final:
#    print("Its done now")
#    print(input_text)
#print(tr, tr_k, bingo_raw_raw)

new_list = []
#new_list = input_text_copy[(tr_k-1)*5:(tr_k-1)*5+5]
st=0
st = new_l[-1]
new_list = input_text[(st-1)*5:(st-1)*5+5]
#new_list = input_text[(tr_k-1)*5:(tr_k-1)*5+5]

sum = 0
for i in range (0,5):
    for j in range(0,5):
        if new_list[i][j] != -1:
            sum = sum + new_list[i][j]
print (sum)  
print(bingo[s])          
print(sum*bingo[s])
