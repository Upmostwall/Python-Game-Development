sample_list = [1,1,2,2,3,3]
sample_set = set(sample_list)

print(sample_set)

if 4 in sample_set:
    print("Yes")
else:
    print("No")

my_set = set([])
my_set.add(1)
my_set.add(2)
my_set.add(3)
my_set.add(3)

print(my_set)

my_set.remove(2)
print(my_set)

a = {1, 2 ,3}
b = {3, 4, 5}

print(a.union(b))
print(a | b)

print(a.intersection(b))
print(a & b)

print(a.difference(b))
print(a - b)

print(a.symmetric_difference(b))
print(a ^ b)