# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.

# Create a tuple
fruits = ("Apples", "Oranges", "Grapes")
# fruits2 = tuple(("Apples", "Oranges", "Grapes"))

# Single value needs trailing comma
fruits2 = ("Apple")
fruits3 = ("Apple",)

# Get value
print(fruits[1])

# Can't change value
# fruits[0] = "Pears"

# Delete tuple
del fruits2

# Get length
print(len(fruits))

# A Set is a collection which is unordered and unindexed. No duplicate members.

# Create set
fruits_set = {"Apples", "Oranges", "Mango"}

# Check if in set
print("Apples" in fruits_set)

# Add to set
fruits_set.add("Grape")

# Remove from set
fruits_set.remove("Grape")

# Add duplicate to set
fruits_set.add("Apples")  # No error, just won't add twice

# Clear set
fruits_set.clear()

# Delete set
del fruits_set
