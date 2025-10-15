# LISTS IN PYTHON
# Lists store multiple values in one variable.
# They are ordered, mutable (changeable), and allow duplicates.
print()
print("--- Lists in Python ---")

animals = ["donkey", "pangolin", "blobfish"]
numbers = [2, 4, 6, 8, 10]
mixed = ["piffle", 42, True, 9.99]

print(animals)
print(numbers)
print(mixed)

print()
print()
print()
print("--- Indexing: how to access the elements of a list ---")
print("First Element:", animals[0])
print("Second element:", animals[1])
print("Last element:", animals[-1])

print()
print("--- Modifying Lists ---")
animals[0] = "babirusa"
print(animals)

# add elemnt at end:
animals.append("glass frog")
print(animals)

# insert element at specific index
animals.insert(3, "aye-aye")
print("Inserted one animal:", animals)
animals.insert(1, "camel")
print("Inserted another animal:", animals)

animals.remove("babirusa")
print(animals)

last_animal = animals.pop()
print("Removed animal:", last_animal)
print("Remaining animals:", animals)

print()
print("--- Useful List Functions ---")

new_list = animals.replace("pangolin")

