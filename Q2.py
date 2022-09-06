# Q 2. Write a python script to calculate sum of squares of first N natural numbers

square_sum = 0
for element in range ( 1 , int ( input ( 'enter number :' ) ) + 1 ) : square_sum = square_sum + element * element
print ( square_sum )