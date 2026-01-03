## Sets are collection which is unordered , unindexed and does not allow duplicate values

Set1={"a","b","c"}
Set2={"a","b","c","d","e","f","g"}
Set3={"h","i","j","k"}

Set1.add("d")
for x in Set1:
    print(x)  ## Here the output will be printed as unsorted manner. As because A set stores elements using a hash table
              ## Elements are placed based on their hash values, not insertion order

## To print in the sorted order for Sets
print("In the sorted way::")
for x in sorted(Set1):
    print(x)

print(" The union of Set1 and Set2 is:")  ## Here the union method also removed duplicates
print(Set1.union(Set2))

print(" The intersection of Set1 and Set2 is:")
print(Set1.intersection(Set2))  ## Intersection prints common values

