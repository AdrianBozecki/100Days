
# Write your code above 👆


with open("file1.txt") as file1:
    file1_list = (file1.read().split("\n"))

with open("file2.txt") as file2:
    file2_list = (file2.read().split("\n"))

result = [n for n in file1_list if n in file2_list]
print(result)

