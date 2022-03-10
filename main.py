#COMPOUND INTEREST FORMULA = (P(1 + r/100)^n) - Principal
import os

os.system('clear')

p = int(input('Please enter your Principal - '))
r = int(input('Please enter your rate - '))
n = int(input('Please enter the amount of years - '))
ci = p * (1 + r/100) ** n


print('The Amount will be', ci)
print('The Compound Interest would be', ci - p)
