## Note :- List is mutable and flexible; Tuple is immutable, faster, and memory-efficient.

my_list=[1,2,3,4,5]
my_tuple=(1,2,3,4,5,6,5)

print(my_list)
print(my_tuple)

my_list[0]=6
print(my_list)  ## This will work
##my_tuple[0]=100
##print(my_tuple)  ## This will throw error

print(my_tuple.count(5))  ## Counts the instances of element 5 present in the tuple
print(my_tuple.index(5))  ## Returns the index position where the element is present in the tuple
