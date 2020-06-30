import random

print random.random()
print random.randint(10,100)
print random.randrange(500)
print random.randrange(15,95,10)

print random.choice([10,120,167,2465])
print random.choice("Apoorv Harsh")

print random.uniform(10,100)

list1=[67,654,987,342,54,6524]
random.shuffle(list1)
print list1
