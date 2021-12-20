"""
blah = True
while 1:
    if blah:
        break
    print("inside while loop")
print("outside loop")
"""

blah = True
while True:
    for i in range(0, 5):
        print("still inside for")
        breaknt("outside of while")