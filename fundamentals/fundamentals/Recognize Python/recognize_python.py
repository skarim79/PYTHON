#variable declaration:
num1 = 42
num2 = 2.3

#data type boolean:
boolean = True

#data type string:
string = 'Hello World'

#list initialize:
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']

#dictionary initialize:
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}

#tuple initialize:
fruit = ('blueberry', 'strawberry', 'banana')

#type check:
print(type(fruit))

#log statement:
print(pizza_toppings[1])
pizza_toppings.append('Mushrooms')
print(person['name'])
person['name'] = 'George'
person['eye_color'] = 'blue'
print(fruit[2])

#conditional:
#conditional if:
if num1 > 45:
    print("It's greater")

#conditional else:
else:
    print("It's lower")

#conditional if:
if len(string) < 5:
    print("It's a short word!")

#conditional elif:
elif len(string) > 15:
    print("It's a long word!")

#conditional else:
else:
    print("Just right!")

#for loop:
#for loop start:
for x in range(5):
#for loop stop:
    print(x)
#for loop start:
for x in range(2,5):
#for loop stop:
    print(x)
#for loop start:
for x in range(2,10,3):
#for loop stop:
    print(x)

#while loop:
x = 0
#while loop start:
while(x < 5):
#while loop stop:
    print(x)
#while loop increment:
    x += 1



pizza_toppings.pop()
pizza_toppings.pop(1)

print(person)
person.pop('eye_color')
print(person)

#for loop:
#for loop start:
for topping in pizza_toppings:
#for loop continue:
    if topping == 'Pepperoni':
        continue
#for loop sequence:
    print('After 1st if statement')
#for loop break:
    if topping == 'Olives':
        break

#function:
#function parameter:
def print_hello_ten_times():
#function argument:
    for num in range(10):
#function return:
        print('Hello')

print_hello_ten_times()

#function:
#function parameter:
def print_hello_x_times(x):
#function argument:
    for num in range(x):
#function return:
        print('Hello')

print_hello_x_times(4)

#function:
#function parameter:
def print_hello_x_or_ten_times(x = 10):
#function argument:
    for num in range(x):
#function return:
        print('Hello')

print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)

#comment multi line
"""
Bonus section
"""
#comment single line
# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)