# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 10:42:03 2019

@author: rdrucker
"""
# Problem 1 with test case
balance = 484
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

month = 1

monthlyInterestRate = annualInterestRate / 12.0

while month <= 12:
    min_payment = balance * monthlyPaymentRate
    balance -= min_payment
    balance += balance * monthlyInterestRate
    balance = round(balance, 2)
    month += 1

print('Remaining balance: ' + str(balance))

# Problem 2 with test case
balance = 3926
annualInterestRate = 0.2

monthlyPayment = 0
monthlyInterestRate = annualInterestRate /12
newbalance = balance
month = 0

while newbalance > 0:
    monthlyPayment += 10
    newbalance = balance

    for month in range(1,13):
        newbalance -= monthlyPayment
        newbalance += monthlyInterestRate * newbalance
        month += 1

print("Lowest Payment: " + str(monthlyPayment))

# Problem 3 with test case
balance = 320000
annualInterestRate = 0.2
epsilon = 0.03

init_balance = balance
monthlyInterestRate = annualInterestRate / 12
lower = init_balance / 12
upper = (init_balance * (1 + monthlyInterestRate) ** 12) / 12.0

while abs(balance) > epsilon:
    monthlyPaymentRate = (upper + lower)/2
    balance = init_balance
    for i in range(12):
        balance = balance - monthlyPaymentRate + ((balance - monthlyPaymentRate) * monthlyInterestRate)
    if balance > epsilon:
        lower = monthlyPaymentRate
    elif balance < -epsilon:
        upper = monthlyPaymentRate
    else:
        break

print('Lowest Payment: ' + str(round(monthlyPaymentRate, 2)))