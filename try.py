# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 01:49:21 2023

@author: user
"""
"""
Write a function that returns true if a list is already sorted in increasing 
order.
"""
def main():
    def isSorted(lst):
# i <= i+1 -> ascending
# i >= i+1 -> descending
        return all(lst[i] <= lst[i+1] for i in range(len(lst)-1))
    
    lst = [int(x) for x in input("Enter a list of integers: ").split()]
    
    if isSorted(lst):
        print("Sorted")
    else:
        print("Not sorted")

main()

"""
Write a complete program that prints numbers 1 - 50, but if the numbers are
multiples of 5, print HiFive, else if the numbers are divisible bt 2, print
HiTwo, and else if numbers that are divisible by 3 or 7, print HiThreeorSeven.
"""
def numbers():
    for i in range(1,51):
        if i % 5 == 0:
            print("HiFive")
        elif i % 2 == 0:
            print("HiTwo")
        elif i % 3 ==0 or i % 7 ==0:
            print("HiThreeorSeven")
        else:
            print("zonk that")

numbers()

"""
Write a function rarest-age that accepts as a parameter a dictionary from
students names(string) to their ages(integer) and returns the least frequently
occuring age.
"""
from collections import Counter

def rarest_age(students):
    ageCount = Counter(students.values())
    rarestAge = min(ageCount, key=ageCount.get)
    return rarestAge

students = {
    "Alyssa": 22,
    "Char": 25,
    "Dan": 25,
    "Jeff": 20,
    "Kasey": 20,
    "Kim": 20,
    "Morgan": 25,
    "Ryan": 25,
    "Steff": 22,
    }
rarest = rarest_age(students)
print(f"{rarest} is the least occuring age")

"""
Write a function range that accepts a list of lists as a parameter and that 
returns the range of values contained in the list of lists which is defined as
1 more than the difference between the largest and the smallest elements.
"""
def getRange(lst):
    newlist = [xsub for y in lst for xsub in y]
    return (max(newlist) - min(newlist) + 1)

lst = [[18, 14, 29], [12, 7, 25], [2, 22, 5]]
ans = getRange(lst)
print(ans)
"""
An extra day is added to the calendar almost every four years as February 29,
 and the day is called a leap day. 
It corrects the calendar for the fact that our planet takes approximately 365.25
 days to orbit the sun. A leap year contains a leap day.
In the Gregorian calendar, three conditions are used to identify leap years:
The year can be evenly divided by 4, is a leap year, unless:
The year can be evenly divided by 100, it is NOT a leap year, unless:
The year is also evenly divisible by 400. Then it is a leap year.
This means that in the Gregorian calendar, the years 2000 and 2400 are leap
 years, while 1800, 1900, 2100, 2200, 2300 and 2500 are NOT leap years
"""
def is_leap(year):
    leap = False
    
    if year % 4 == 0 and year % 100 !=0:
        leap = True
        return leap
    
    elif year % 400 == 0 and year % 100 == 0:
        leap = True
        return leap
        
    else:
        leap = False
        return leap    

year = int(input("Enter the year: "))
ans = is_leap(year)
print(ans)

"""
Solving a system of linear equations using matrices
"""
from scipy import linalg
import numpy as np

a = np.array([[1, 3, 5], [2, 5, 1], [2, 3, 8]])
b = np.array([10, 8, 3])

result = linalg.solve(a, b)
print(result)

"""
The Bank acount
"""
class BankAccount(object):
    interest_rate = 0.3
    def __init__(self, name, number, balance):
        self.name = name
        self.number = number
        self.balance = balance
        
        return
    def deposit(self):
        depo = int(input("Enter the amount you want to deposit: "))
        self.balance = self.balance + depo
        print(f"Account balance: {self.balance}")
    def withdraw(self):
        withD = int(input("Enter the amount you want to withdraw: "))
        
        if withD <= self.balance:
            self.balance = self.balance - withD
            print(f"{self.balance} has been withdrawn.")
            print(f"Account balance: {self.balance}")
        else:
            print("Insufficient funds!!!!")
    def add_interest(self):
        self.balance = self.balance + (self.balance * BankAccount.interest_rate)
        print(f"New balance: {self.balance}")
        
class StudentAccount(BankAccount):
    overLimit = 1000
    
    def __init__(self, name, number, balance):
        self.name = name
        self.number = number
        self.balance = balance
        
        return
    
    def deposit(self):
        depo = int(input("Enter the amount you want to deposit: "))
        self.balance = self.balance + depo
        print(f"Account balance: {self.balance}")
    def withdraw(self):
        withDrawable = self.balance + StudentAccount.overLimit
        withD = int(input("Enter the amount you want to withdraw: "))
        
        if withD <= withDrawable:
            self.balance = self.balance - withD
            print(f"{withD} has been withdrawn.")
            print(f"Account balance: {self.balance}")
        else:
            print("Insufficient funds!!!!")
        
                                                           

myObj = BankAccount("Allan", 10, 0)
obj2 = StudentAccount("Allan", 11, 0)
obj2.deposit()
obj2.withdraw()
myObj.add_interest()

from scipy.integrate import quad

def f(x):
    return x**2

area = quad(f, 0, 2)
print(area)


def recur_fibo(n):
    if n <= 1:
        return n
    else:
        return (recur_fibo(n-1) + recur_fibo(n-2))
    
nterms = int(input("Enter number of terms: "))

if nterms <= 0:
    print("Enter a positive number!!!")
else:
    print("Fibo fucking sequence ->")
    for i in range(nterms):
        print(recur_fibo(i))




















