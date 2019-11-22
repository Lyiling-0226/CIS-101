import random
a = random.randint(1,20)
print(a)
b = random.randint(1,20)
print(b)
c = a*b
print(c)
if c > 100:
    print("the room is huge")
elif c < 100:
    print("the room is small")
else:
    print("its just right")
