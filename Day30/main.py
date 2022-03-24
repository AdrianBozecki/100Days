# Error handling and catching exceptions
# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key": 'value'}
#     print(a_dictionary["key"])
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist")
# else:
#     content = file.read()
#     print(content)
# finally:
#     raise KeyError
#

# height = float(input("Height: "))
# weight = int(input("Weight: "))
#
# if height > 3:
#     raise ValueError("Human height should not be over 3 meters")
#
# bmi = weight / height ** 2
# print(bmi)

# Exercise

# fruits =["Apple", "Pear", "Orange"]
#
#
# def make_pie(index):
#     try:
#         fruit = fruits[index]
#     except IndexError:
#         print("Fruit pie")
#     else:
#         print(fruit + " pie")
#
#
# make_pie(0)

# Excercise 2

facebook_posts = [
    {'Likes': 21, 'Comments': 2},
    {'Likes': 27, 'Comments': 2, 'Shares': 1},
    {'Likes': 23, 'Comments': 1, 'Shares': 3},
    {'Comments': 2, 'Shares': 3},
    {'Likes': 21, 'Comments': 7},
    {'Likes': 2, 'Comments': 2},
]

total_likes = 0

for post in facebook_posts:
    try:
        total_likes = total_likes + post['Likes']
    except KeyError:
        pass

print(total_likes)