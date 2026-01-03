## Dictionary is an unordered collection of unique key value pairs.fast because they use hashing.

person = {
    "name": "Kailash",
    "age": 30,
    "city": "Bangalore"
}
print (person["name"])

## Dictionaries preserve insertion order unlike sets
print (person.items())

## Retrieve value
print (person.get("name"))

## Updating existing values which states it is immutable
person.update({"name":"KKailash"})
print (person)

## Removes the Key value pair of the Key name
del person["name"]
print(person)

## Adding a new Key Value pair
person.update({"Height":"45"})
print(person)