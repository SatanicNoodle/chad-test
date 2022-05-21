
import random
from tkinter import Y 

print('Pick A Number From 1 To 10:')
x = int(input())

y = random.randint(1, 2)




if x == y:
	print("nice one chuckle nuts, you're correct its %d"%(y))


else:
	print("it was actually %d ya silly goof"%(y))

