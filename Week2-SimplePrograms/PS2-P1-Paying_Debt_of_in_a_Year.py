# Problem 1 - Paying Debt off in a Year

# Write a program to calculate the credit card balance after one year if a person only pays the minimum monthly payment required by the credit card company each month.
# The following variables contain values as described below:
# 1.	balance - the outstanding balance on the credit card
# 2.	annualInterestRate - annual interest rate as a decimal
# 3.	monthlyPaymentRate - minimum monthly payment rate as a decimal
# For each month, calculate statements on the monthly payment and remaining balance. At the end of 12 months, print out the remaining balance. Be sure to print out no more than two decimal digits of accuracy - so print
# Remaining balance: 813.41
# instead of
# Remaining balance: 813.4141998135
# So your program only prints out one thing: the remaining balance at the end of the year in the format:
# Remaining balance: 4784.0
# A summary of the required math is found below:
# Monthly interest rate= (Annual interest rate) / 12.0
# Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)
# Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
# Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)
# We provide sample test cases below. We suggest you develop your code on your own machine, and make sure your code passes the sample test cases, before you paste it into the box below.
# Test Cases to Test Your Code With. Be sure to test these on your own machine - and that you get the same output! - before running your code on this webpage!
# Click to See Problem 1 Test Cases
# Test Cases:
# 1.		      # Test Case 1:
# 2.		      balance = 42
# 3.		      annualInterestRate = 0.2
# 4.		      monthlyPaymentRate = 0.04
# 5.
# 6.		      # Result Your Code Should Generate Below:
# 7.		      Remaining balance: 31.38
# 8.
# 9.	          # To make sure you are doing calculation correctly, this is the
# 10.	          # remaining balance you should be getting at each month for this example
# 11.	            Month 1 Remaining balance: 40.99
# 12.	            Month 2 Remaining balance: 40.01
# 13.	            Month 3 Remaining balance: 39.05
# 14.	            Month 4 Remaining balance: 38.11
# 15.	            Month 5 Remaining balance: 37.2
# 16.	            Month 6 Remaining balance: 36.3
# 17.	            Month 7 Remaining balance: 35.43
# 18.	            Month 8 Remaining balance: 34.58
# 19.	            Month 9 Remaining balance: 33.75
# 20.	            Month 10 Remaining balance: 32.94
# 21.	            Month 11 Remaining balance: 32.15
# 22.	            Month 12 Remaining balance: 31.38
# 23.
# 24.
# 25.
# 26.		      Test Case 2:
# 27.		      balance = 484
# 28.		      annualInterestRate = 0.2
# 29.		      monthlyPaymentRate = 0.04
# 30.
# 31.		      Result Your Code Should Generate Below:
# 32.		      Remaining balance: 361.61

#Hints
#Only two decimal digits of accuracy?
#Use the round function at the end of your code!
#How to think about this problem?
#To help you get started, here is a rough outline of the stages you should probably follow in writing your code:
#•	For each month:
#•	Compute the monthly payment, based on the previous month’s balance.
#•	Update the outstanding balance by removing the payment, then charging interest on the result.
#•	Output the month, the minimum monthly payment and the remaining balance.
#•	Keep track of the total amount of paid over all the past months so far.
#•	Print out the result statement with the total amount paid and the remaining balance.
#Use these ideas to guide the creation of your code.

#balance - saldo
#gks - godisnja kamatna stopa /annual interest rate
#mps - mjesecna stopa placanja / monthly payment rate


def oneYearCCBalance(startBalance, annualInterestRate, monthlyPaymentRate):
    for month in range(12):
        endBalance = (startBalance * annualInterestRate/12 + startBalance) - ((startBalance * annualInterestRate/12 + startBalance) * monthlyPaymentRate)
        endBalance = round(endBalance, 2)
        print ("Month ", month+1, " Remaining balance:", endBalance)
        startBalance=endBalance

oneYearCCBalance(42, 0.2, 0.04)
print("")
oneYearCCBalance(484, 0.2, 0.04)
