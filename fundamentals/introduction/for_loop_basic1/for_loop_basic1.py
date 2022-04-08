#Basic:
for num in range (0, 100, 1):
    print (num)

#Multiples of 5:
for num in range (0, 1000, 5):
    print (num)

#Counting the Dojo way:
for num in range (1, 100):
    print (num)
    if num % 5 == 0:
        print('Coding')
    if num % 10 == 0:
        print('Coding Dojo')

#Whoa. That Sucker's Huge:
for num in range (1, 500000, 2):
    sum = int(num) + 2
    print("The sum is: ", sum)

#Countdown by Fours:
for num in range (2018, 0, -4):
    print (num)

#Flexible Counter:
lowNum = 0
highNum = 50
multNum = 3
for int in range (lowNum, highNum, multNum):
    print (int)