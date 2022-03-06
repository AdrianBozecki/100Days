# def add(*args):
#     sum = 0
#     for n in args:
#         sum += n
#     return print(sum)
#
# add(1,2,3,4,5,6,7,8)

def calculate(n, **kwargs):
    # for key, value in kwargs.items():
    #     print(value)

    n *= kwargs['multiply']
    print(n)

calculate(2, add=3, multiply=5)

class Car:

    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.color = kw.get("color")

my_car = Car(make="Nissan", color="Green")
print(my_car.color)
