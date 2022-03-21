## Numpy Exercise 2
import numpy as np

## This array documnets the last 5 sales for each of Superstore's four cash registers. 
salesArray = np.array([[150.68,207.99,107.88,58.99,60.59],[20.89,98.99,258.62,19.76,101.59],[70.66,190.10,134.54,200.14,15.59],[10.52,201.59,140.55,13.99,45.98]])

## Step 1: Print the total sales for the store.
print("-----------------------------------------------   STEP ONE   -----------------------------------------------")

step_one = np.sum(salesArray)
print("Total sales for the store is: ", step_one)

## Step 2: What was Superstore's smallest and largest sale? Print them.
print("-----------------------------------------------   STEP TWO   -----------------------------------------------")

smallest = np.min(salesArray)
largest = np.max(salesArray)
print("Smallest: ", smallest, "\n", "Largest: ", largest)

## Step 3: Print an array that will show which sales are greater than or equal to $100.
print("-----------------------------------------------   STEP THREE  -----------------------------------------------")

print(salesArray[salesArray >= 100])
print()


## Step 4: Print the total sales for each register.
print("-----------------------------------------------   STEP FOUR   -----------------------------------------------")

print(np.sum(salesArray[0]))
print(np.sum(salesArray[1]))
print(np.sum(salesArray[2]))
print(np.sum(salesArray[3]))


## Step 5: Superstore is a cashless store and needs to calculate their owed credit card fees. Each sale is subject to a 2% credit card fee.
#           Using the salesArray, create a new array that stores the 2% fee for each sale and register. Print the array and then print the total fees.
print("-----------------------------------------------   STEP FIVE  -----------------------------------------------")

credit_card_fee = 0.02
transaction_fees = [[i * credit_card_fee for i in row] for row in salesArray]
total_fees = np.sum(transaction_fees)

print("The sale fee is: ", transaction_fees)
print("Total fees are equal to: ", total_fees)


## Step 6: Using your fee array and salesArray, calculate how much profit Superstore made for each sale after paying credit card fees. Store this in a new array and print it.
print("-----------------------------------------------   STEP SIX  -----------------------------------------------")

profits = salesArray - transaction_fees
print("Profits are equal to: ", profits)


## Step 7: Print the sales only for the second and forth cash register
print("-----------------------------------------------   STEP SEVEN  -----------------------------------------------")

print(salesArray[[1,3]])
print()

## Step 8: Superstore has added a 5th cash register who's data is stored in the array newRegister. Add the new register to the original array. Print the updated salesArray.
print("-----------------------------------------------   STEP EIGHT  -----------------------------------------------")

newRegister = np.array([17.89,13.59,107.89,176.88,56.78])
salesArray = np.vstack((salesArray, newRegister))
print("The updates sales array is: ", salesArray)


## Step 9: Register #3 had an error and recorded it's fourth sale ($200.14) incorrectly. The sale should have been $20.14. Update the array to correct this error.
#           Print the array before and after the update to see the change.
print("-----------------------------------------------   STEP NINE  -----------------------------------------------")

print("The array before the error is: ", salesArray)

salesArray[2,3] = 20.14
print("The corrected error is: ", salesArray)


