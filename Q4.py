# Q 4. Write a python script to calculate sum of first N odd natural numbers

odd_sum = 0
for element in range ( 1 , 2 * int ( input ( 'enter number :' ) ) , 2 ) : odd_sum = odd_sum + element
print ( 'the sum of odd numbers is ' , odd_sum )