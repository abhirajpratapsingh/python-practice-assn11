# Q5. Write a python script to calculate sum of first N even natural numbers

even_sum = 0
for element in range ( 2 , 2 * int ( input ( 'enter number :' ) ) + 1 , 2 ) : even_sum = even_sum + element
print ( even_sum )
