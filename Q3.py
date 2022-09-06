# Q 3. Write a python script to calculate sum of cubes of first N natural numbers

cubes_sum = 0
for element in range ( 1 , int ( input ( 'enter number :' ) ) + 1 ) : cubes_sum = cubes_sum + element ** 3 
print ( cubes_sum )