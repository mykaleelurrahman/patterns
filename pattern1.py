#!/usr/bin/python

steps = input("Enter the Number of Steps: ")
for i in range(steps+1):
	print(' ' * i + (steps-i) * '*' ) 
