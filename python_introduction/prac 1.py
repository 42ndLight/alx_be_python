def greet(name):
    print(f"Hello {name}")

greet("Ken")



area = lambda l, w: l * w
result = area(4, 3)
print(result)

def area1(length, width):
    ans = length * width
    return ans

ans = area1(8, 5)
print(ans)


def find_even(number):
    if number % 2 == 0:
        print(f"The number is Even")
    elif number % 2 == 1:
        print(f"The number is Odd")

find_even(30)
find_even(5)
find_even(85644)
find_even(642116214421423)
