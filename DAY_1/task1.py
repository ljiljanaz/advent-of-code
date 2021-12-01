f = open("day1.txt", "r")
count = 0
#print(f.read())
data = f.readlines()
print(len(data))
for i in range (1, len(data)):
    if int(data[i])>int(data[i-1]):
        #print(data[i])
        count=count+1
print(count)

count1=0
for i in range (0,len(data)-3):
    sum1 = int(data[i]) + int(data[i+1]) + int(data[i+2])
    sum2 = int(data[i+1]) + int(data[i+2]) + int(data[i+3])
    if sum2 > sum1:
        count1 = count1 + 1
print(count1)        