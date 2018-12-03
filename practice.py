import numpy as np
import random


'''
EX.1 @ practivepython.org

name=input("What is your name?")
age=input("How old are you?")

age_in_100_years=(2018-int(age))+100

print("Hello {}! You will turn 100 years old in {}".format(name,age_in_100_years))



EX.2 @ practivepython.org

num=input("Please enter a number: ")

if int(num)%2==0:
	print("This number is even :)")
else:
	print("This number is odd :(")

if int(num)%4==0:
	print("Also, this number is a multiple of 4!")
else:
	print("I checked if this was also a multiple of 4... it isn't.")



EX.3 @ practivepython.org

nums = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
nums_less=[]
num_pick=input("Pick a number: ")



for n in nums:
	if n < int(num_pick):
		nums_less.append(n)
	else:
		print("No number in this list was greater than {}".format(num_pick))
print(nums_less)

#one_line=[print(n) for n in nums if n<5 ]


EX.4 @ practivepython.org

l=[]
i=input("Please enter a number: ")
print('Here are all the divisors of {}.'.format(i))
for n in range(1,1000):
	if n%int(i)==0:
		l.append(n)
	else:
		pass
print(l)



#EX.5 @ practivepython.org
# Have to come back to this for random number generation.
# l=[]
for n in range(1,31):
	l.append(random.randint(0,2001))
print(l)

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c=[]
d=random.sample(xrange(1,101),20)
e=random.sample(xrange(1,101),25)
print(d)
print(e)
for i in d:
	if i not in e:
		#print(str(i) + " is not in b")
		c.append(i)
	else:
		pass
print(c)

'''
'''
#EX. 7 @ practivepython.org

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
b=[print(n) for n in a if int(n)%2==0]


#EX. 8 @ practivepython.org

GAMES=5
P1_LIST=[]
P2_LIST=[]

print("\nThis game will be best of {} \n".format(GAMES))

while GAMES > 0:
	p1=input("The choice is yours, Player 1. Enter rock, paper, or scissors: \n")
	P1_LIST.append(p1)
	p2=input("The choice is now yours, Player 2. Enter rock, paper, or scissors: \n")
	P2_LIST.append(p2)
	if p1==p2:
		print('It is a draw!')
		GAMES-=1
	elif p1 == 'scissors' and p2 != 'rock':
		print('Player 1 wins!')
		GAMES-=1
	elif p1 == 'rock' and p2 != 'paper':
		print('Player 1 wins!')
		GAMES-=1
	elif p1 == 'paper' and p2 != 'scissors':
		print('Player 1 wins!')
		GAMES-=1
	else:
		print('Player 2 wins!')
		GAMES-=1
if GAMES <=0:
	print("GAME OVER!")

print('The plays\n')

print('Player 1 played: '+ str(P1_LIST))
print('Player 2 played: '+ str(P2_LIST))
''' 



