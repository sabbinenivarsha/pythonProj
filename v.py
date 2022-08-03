import random
n=random.randbytes(3)
print(n)
print(random.randrange(1,8))
print(random.randrange(100,211))
mylist=["sue","varsha","veda","sanjana","sai","chinni"]
mylist1={"sue","varsha","veda","sanjana","sai","chinni"}
print(random.choice(mylist))
#print(random.choice(mylist1))
random.shuffle(mylist)
print(mylist)