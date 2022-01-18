# Write your code below this line 👇

def prime_checker(number):
    if number < 2:
        return False
    else:
        for i in range(2, number, ):
            if number % i == 0:
                return False
        return True



# Write your code above this line 👆

# Do NOT change any of the code below👇
n = int(input("Check this number: "))
if prime_checker(number=n):
    print('Number is prime')
else:
    print("Number isn't prime")

