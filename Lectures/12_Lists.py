List1=["Apples","Bananas",12.5,12,"Oranges"]
print(List1)

for x in List1:
    print(x)

List1.append("Grapes")  ## appends the element at the alst
print(List1)

List1.insert(2,"Pineapples")  ##inserts at the specified indexed position
print(List1)

List1.remove(12)  ##Removes the element at the specified index
print(List1)

print(List1.count("Grapes")) ##Counts the presence of that element in the list

### 2D - List os lists -- MultiDimensional Lists
Fruits=["Apples","Bananas","Pineapples"]
Desserts=["Icecream","Sweets Bar"]
Drinks=["Coke","ThumsUp","Mirinda"]

Food=[Fruits,Desserts,Drinks]  ## This is a 2D list
print(Food)

## Now if i want to access the "Apples" from Fruits list from this Food list
print(Food[0][0])

## Now if i want to access the "Thumsup" from Drinks list from this Food list
print(Food[2][1])