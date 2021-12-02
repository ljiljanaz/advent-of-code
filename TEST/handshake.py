val = 1
rem = 0
count = 0
#while val != 6929599:
# while val != 2448427:
while val != 5764801:
    val = val * 7
    val = val % 20201227
    count = count + 1
print(val, count)

pk = 1
for i in range (0, 8652834):
    pk = pk * 6929599
    pk = pk % 20201227
print(pk)

pk1 = 1
for i in range (0, 15210194):
    pk1 = pk1 * 2448427
    pk1 = pk1 % 20201227
print(pk)