import random



# Dictionary to store information about my favorite book
favorite_book = {
    "title": "To Kill a Mockingbird",
    "author": "Harper Lee",
    "genre": "Fiction"
}
print(favorite_book["title"])
print(favorite_book.get("author"))
print(favorite_book.keys())
print(favorite_book.values())
print(favorite_book.items())
favorite_book["year"] = 1960
print(favorite_book)
favorite_book.pop("genre")
print(favorite_book)


# List to store names of my favorite fruits
favorite_fruits = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]
print(favorite_fruits[0])
print(favorite_fruits[::-1])
print(favorite_fruits[1:4])
favorite_fruits.append("Fig")
print(favorite_fruits)
favorite_fruits.insert(2, "Grape")
print(favorite_fruits)
favorite_fruits.remove("Cherry")
print(favorite_fruits)

# Program to generate a random set of numbers between 1 and 10
random_numbers1 = random.sample(range(1, 11), 5)
random_numbers2 = random.sample(range(1, 11), 5)

print("Random set of numbers:", random_numbers1)
print("Random set of numbers:", random_numbers2)

# Set operations
union = list(set(random_numbers1) | set(random_numbers2))
print("Union of numbers:", union)
intersection = list(set(random_numbers1) & set(random_numbers2))
print("Intersection of numbers:", intersection)
difference = list(set(random_numbers1) - set(random_numbers2))
print("Difference of numbers:", difference)



