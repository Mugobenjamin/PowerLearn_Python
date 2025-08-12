# -------------------------
# Task 1: List of integers & sum
# -------------------------
numbers = input("Enter integers separated by spaces: ")
numbers_list = [int(num) for num in numbers.split()]
print("Sum of integers:", sum(numbers_list))

# -------------------------
# Task 2: Tuple of favorite books
# -------------------------
favorite_books = ("The High Driud", "200", "One piece", "Dune", "War of Ice and Fire")
print("\nMy favorite books:")
for book in favorite_books:
    print(book)

# -------------------------
# Task 3: Dictionary with user info
# -------------------------
person = {}
person['name'] = input("\nEnter your name: ")
person['age'] = int(input("Enter your age: "))
person['favorite_color'] = input("Enter your favorite color: ")
print("\nPerson Information:", person)

# -------------------------
# Task 4: Sets and intersection
# -------------------------
set1 = set(map(int, input("\nEnter integers for set 1 (space-separated): ").split()))
set2 = set(map(int, input("Enter integers for set 2 (space-separated): ").split()))
common_elements = set1 & set2
print("Common elements:", common_elements)

# -------------------------
# Task 5: List comprehension for odd-length words
# -------------------------
words = ["apple", "banana", "grape", "kiwi", "orange", "fig", "watermelon"]
odd_length_words = [word for word in words if len(word) % 2 != 0]
print("\nWords with odd number of characters:", odd_length_words)
